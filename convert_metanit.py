#!/usr/bin/env python3
import os
import re
import requests
from bs4 import BeautifulSoup
import time

# Base paths
BASE_WIKI_PATH = "/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C#/Графические программы"
BASE_URL = "https://metanit.com"

# Guide configurations
GUIDES = {
    "Руководство по GTK": {
        "url_base": "/sharp/gtk/",
        "chapters": {
            1: {"name": "Глава 1. Введение в GTK", "articles": ["1.1", "1.2", "1.3", "1.4"]},
            2: {"name": "Глава 2. Определение интерфейса в XML", "articles": ["2.1", "2.2", "2.3"]},
            3: {"name": "Глава 3. Макет и позиционирование", "articles": ["3.1", "3.2", "3.3", "3.4"]},
            4: {"name": "Глава 4. Виджеты", "articles": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9", "4.10", "4.11"]},
            5: {"name": "Глава 5. Списки", "articles": ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7", "5.8", "5.9", "5.10", "5.11"]}
        }
    },
    # Other guides will be added here
}

def fetch_page(url):
    """Fetch a page and return BeautifulSoup object"""
    try:
        response = requests.get(url, timeout=30)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_article_content(soup):
    """Extract article content from metanit page"""
    # Find the main content area
    content_div = soup.find('div', class_='content')
    if not content_div:
        content_div = soup.find('article')
    if not content_div:
        content_div = soup.find('main')
    
    if not content_div:
        return None, None
    
    # Extract title
    title = None
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)
    
    # Extract content (simplified - would need more sophisticated parsing)
    content = content_div.get_text(separator='\n', strip=True)
    
    return title, content

def create_wiki_article(title, content, guide_name, chapter_name, article_name, source_url):
    """Create wiki-formatted article"""
    # Breadcrumbs
    breadcrumbs = f"[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/{guide_name}|{guide_name}]] / [[Языки программирования/C#/Графические программы/{guide_name}/{chapter_name}|{chapter_name}]] / {article_name}"
    
    # Navigation (simplified - would need actual prev/next logic)
    navigation = f"[[Языки программирования/C#/Графические программы/{guide_name}/{chapter_name}|Содержание]]"
    
    # Date
    date_line = "**Дата написания:** 05.09.2026"
    
    # Source
    source_line = f"**Источник:** [{source_url}]({source_url})"
    
    # Combine into wiki format
    wiki_content = f"""# {title}

{breadcrumbs}

{navigation}

{date_line}

{content}

{source_line}
"""
    return wiki_content

def create_guide_index(guide_name, chapters):
    """Create index file for a guide"""
    index_content = f"""# {guide_name}

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / {guide_name}

## Главы

"""
    for chapter_num, chapter_info in chapters.items():
        chapter_name = chapter_info["name"]
        index_content += f"- [[Языки программирования/C#/Графические программы/{guide_name}/{chapter_name}|{chapter_name}]]\n"
    
    return index_content

def create_chapter_index(guide_name, chapter_name, articles):
    """Create index file for a chapter"""
    index_content = f"""# {chapter_name}

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/{guide_name}|{guide_name}]] / {chapter_name}

## Уроки

"""
    for article_id in articles:
        # This would need actual article titles
        index_content += f"- [[Языки программирования/C#/Графические программы/{guide_name}/{chapter_name}/Article_{article_id}|Article {article_id}]]\n"
    
    return index_content

def main():
    print("Starting metanit.com to Obsidian wiki converter...")
    
    # Create base directory
    os.makedirs(BASE_WIKI_PATH, exist_ok=True)
    
    # Process each guide
    for guide_name, guide_info in GUIDES.items():
        print(f"\nProcessing guide: {guide_name}")
        
        # Create guide directory
        guide_path = os.path.join(BASE_WIKI_PATH, guide_name)
        os.makedirs(guide_path, exist_ok=True)
        
        # Create guide index
        guide_index = create_guide_index(guide_name, guide_info["chapters"])
        with open(os.path.join(guide_path, "Оглавление.md"), 'w', encoding='utf-8') as f:
            f.write(guide_index)
        
        # Process each chapter
        for chapter_num, chapter_info in guide_info["chapters"].items():
            chapter_name = chapter_info["name"]
            print(f"  Processing chapter: {chapter_name}")
            
            # Create chapter directory
            chapter_path = os.path.join(guide_path, chapter_name)
            os.makedirs(chapter_path, exist_ok=True)
            
            # Process each article
            for article_id in chapter_info["articles"]:
                article_url = f"{BASE_URL}{guide_info['url_base']}{article_id}.php"
                print(f"    Fetching article: {article_url}")
                
                soup = fetch_page(article_url)
                if soup:
                    title, content = extract_article_content(soup)
                    if title and content:
                        # Create wiki article
                        wiki_content = create_wiki_article(
                            title, content, guide_name, chapter_name, 
                            f"Article_{article_id}", article_url
                        )
                        
                        # Save article
                        article_filename = f"{title}.md"
                        article_path = os.path.join(chapter_path, article_filename)
                        with open(article_path, 'w', encoding='utf-8') as f:
                            f.write(wiki_content)
                        
                        print(f"      Created: {article_filename}")
                
                # Be polite to the server
                time.sleep(1)
            
            # Create chapter index
            chapter_index = create_chapter_index(guide_name, chapter_name, chapter_info["articles"])
            with open(os.path.join(guide_path, f"{chapter_name}.md"), 'w', encoding='utf-8') as f:
                f.write(chapter_index)
    
    print("\nConversion completed!")

if __name__ == "__main__":
    main()
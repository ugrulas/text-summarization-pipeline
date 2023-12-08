import requests
import os
import shutil
from bs4 import BeautifulSoup
import PyPDF2
from io import BytesIO
from abc import ABC, abstractmethod
from datetime import datetime
import argparse 

DATA_DIR = 'data/pfizer'

def parse_args():
    parser = argparse.ArgumentParser(description="Scrape Pfizer website")
    parser.add_argument("--year", type=int, default=datetime.now().year, help="Year to scrape")
    parser.add_argument("--month", type=int, default=datetime.now().month, help="Month to scrape")
    return parser.parse_args()


class PfizerScraper(ABC):
    def __init__(self, base_path,year=datetime.now().year,month= datetime.now().month,items=48,link_filter=[]):
        self.base_url = 'https://www.pfizer.com'
        self.base_path = base_path
        self.year = year
        self.month = month
        self.query = f'?press_release_date_year[{year}]={year}&press_release_date_month[{month}]={month}&items_per_page={items}'
        self.link_filter = link_filter
        self.save_folder = os.path.join(DATA_DIR, f'{self.year}_{self.month}/{self.base_path.split("/")[-1]}')
        if os.path.exists(self.save_folder):
            shutil.rmtree(self.save_folder)
        os.makedirs(self.save_folder)
        
    def fetch_page(self, path='',query=''):
        url = self.base_url + path + query
        response = requests.get(url)
        return response.text if response.status_code == 200 else None

    def extract_links(self, html, patterns=[]):
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if not patterns or any(pattern in href for pattern in patterns):
                links.append(href)
        return links

    def extract_pdf_content(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            file = BytesIO(response.content)
            reader = PyPDF2.PdfFileReader(file)
            content = ''
            for page in range(reader.numPages):
                content += reader.getPage(page).extractText()
            return content
        return None
        
    def extract_article(self, path):
        full_url = self.base_url + path
        response = requests.get(full_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find_all('h1', attrs={'class': 'article-title'})[0].get_text(strip=True)
            specific_divs = soup.find_all('div',  attrs={'class': None, 'id': None})
            p_elements = []
            text_elements = []
            for div in specific_divs:
                p_elements.extend(div.find_all(['p','li'], attrs={'class': None, 'id': None}))
            for p in p_elements:
                text = p.get_text()
                if 'About Pfizer: Breakthroughs That Change Patients’ Lives' in text:
                    text_elements.append(text.split("About Pfizer: Breakthroughs That Change Patients’ Lives")[0])
                    break
                if 'DISCLOSURE NOTICE' in text.upper():
                    text_elements.append(text.split("References")[0])
                    break
                if 'References' in text:
                    text_elements.append(text.split("References")[0])
                    break
                text_elements.append(text) 
            text_elements = list(dict.fromkeys(text_elements)) 
            title_text = title + '\n'
            full_article_text = '\n'.join([para for para in text_elements])
            return title_text + full_article_text
        return None
        
    def write_to_file(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    
    def scrape(self):
       
        html_content = self.fetch_page(self.base_path,self.query)
        links = self.extract_links(html_content,self.link_filter)
        print(f'Found {len(links)} links for {self.base_path}')
        for index, link in enumerate(links):
            file_name = link.split('/')[-1]
            if '.pdf' in link:
                pdf_content = self.extract_pdf_content(link)
                if pdf_content:
                    self.write_to_file(os.path.join(self.save_folder,f'{file_name}.txt'), pdf_content)
            else:
                article_content = self.extract_article(link)
                if article_content:
                    self.write_to_file(os.path.join(self.save_folder,f'{file_name}.txt'), article_content)     


def main():
    args = parse_args()
    announcement_scraper = PfizerScraper('/stories/announcements', year=args.year, month=args.month, link_filter=['/news/announcements'])
    press_release_scraper = PfizerScraper('/newsroom/press-releases', year=args.year, month=args.month, link_filter=['news/press-release'])
    update_scraper = PfizerScraper('/newsroom/updates-and-statements', year=args.year, month=args.month, link_filter=['/news/announcements'])

    announcement_scraper.scrape()
    press_release_scraper.scrape()
    update_scraper.scrape()

if __name__ == "__main__":
    main()
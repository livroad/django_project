from django.shortcuts import render
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup

def scrape_and_save(request):
    url = 'https://example.com'  # スクレイピング対象のURLを設定
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # スクレイピングしたデータを取得
        title = soup.find('title').text
        content = soup.find('p').text

        # データベースに保存
        scraped_data = ScrapedData(title=title, content=content)
        scraped_data.save()

        return render(request, 'scraping_app/display_data.html', {'scraped_data': scraped_data})

    else:
        return render(request, 'scraping_app/error.html')

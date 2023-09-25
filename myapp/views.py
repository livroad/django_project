from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import ScrapedData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def scrape_and_save(request):
    url = 'https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html'  # スクレイピング対象のURLを指定
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # ページから必要な情報を抽出
    data = soup.find('div', class_='target-element').text

    # データベースに保存
    scraped_data = ScrapedData(content=data)
    scraped_data.save()

    return HttpResponse(f'Successfully scraped and saved: {data}')

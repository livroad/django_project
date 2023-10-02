from django.http import HttpResponse
from django.shortcuts import render
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup
import json

def index(request):
    return HttpResponse("hello")

def scrape_and_save(request):
    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'
    headers = {
        'content-type': 'application/json',
    }
    params = {
        'format': 'json',
        'categoryId': '38',
        'applicationId': '1082202931688861826',
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        nickname = data["result"][0]["nickname"]
        recipeTitle = data["result"][0]["recipeTitle"]
        recipeDescription = data["result"][0]["recipeDescription"]
        recipeMaterial = data["result"][0]["recipeMaterial"]

        scraped_data = ScrapedData(
            title=recipeTitle,
            content=f"Nickname: {nickname}\nDescription: {recipeDescription}\nMaterial: {recipeMaterial}"
        )
        scraped_data.save()

        return render(request, 'myapp/display_data.html', {'scraped_data': scraped_data})

    else:
        return render(request, 'myapp/error.html')

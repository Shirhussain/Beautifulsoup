import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus

def home(request):

    return render(request, "scrap/home.html", {})
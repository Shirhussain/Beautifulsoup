from django.shortcuts import  render
import requests
from bs4 import BeautifulSoup
from time import sleep

url = requests.get("https://divar.ir/s/tehran").text
soup = BeautifulSoup(url, 'lxml')

posts = soup.find_all('div',class_='post-card-item')



def home(request):
    final_post = []
    for post in posts:
        slug = post.find('a').get('href')
        try:
            subtitle = post.find(class_="post-card__title").text
        except expression as identifier:
            None
        try:
            description = post.find(class_="post-card__description").text
        except:
            description = ""
        time = post.find(class_="post-card__info-label").text
        try:
            img_src = post.find('img').get('src')
        except:
            img_src = "https://www.vermeer.com.au/wp-content/uploads/2016/12/attachment-no-image-available.png"
        
        if post.find(class_="post-card__info-urgent"):
            urgent = post.find(class_="post-card__info-urgent").text
        else:
            urgent = ""
        final_post.append((img_src,subtitle, description, time,slug, urgent))
    
    context = {
        'final_post':final_post
    }
    return render(request, "scrap/home.html", context)
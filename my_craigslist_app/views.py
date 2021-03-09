import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models            # import database

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://newyork.craigslist.org/d/for-sale/search/sss?query={}&sort=rel'

BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# renders the home page for the site
def home (request):
    return render (request, 'base.html')


# New Serach gets the name of the query item and goes to craigslist website and retrievs that data
def new_search (request):
    
    search = request.POST.get ('search')
    models.Search.objects.create (search = search)          # creates a search object with a DB model
    query_url = BASE_CRAIGSLIST_URL.format (quote_plus (search))
    response = requests.get (query_url)
    data = response.text
    
    # Passing the src code to Beautiful Soup to create a Beautiful object for it
    soup = BeautifulSoup (data, features = 'html.parser')
    
    # Extracting all the <li> tags whose class name is 'result-row' into a list 
    post_listings = soup.find_all('li', {'class': 'result-row'})
    
   
    final_postings = []

    for post in post_listings:
        post_title = post.find (class_ = 'result-title').text
        post_url = post.find ('a').get ('href')
        if post.find (class_ = 'result-price'):
            post_price = post.find (class_ = 'result-price').text
        else:
            post_price = 'N/A'   

        if post.find (class_ = 'result-image').get ('data-ids'):
            post_image_id = post.find (class_ = 'result-image').get ('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format (post_image_id)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'


        final_postings.append ((post_title, post_url, post_price, post_image_url))

            
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings
    }
    return render (request, 'my_craigslist_app/new_search.html', stuff_for_frontend)
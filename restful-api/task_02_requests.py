#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url)
    print(f"Status Code: {reponse.status_code}")

    if reponse.status_code == 200:
        post = reponse.json()
        for post in post:
            print(post["title"])    

    else:
        print("Error:", reponse.status_code)

    
        
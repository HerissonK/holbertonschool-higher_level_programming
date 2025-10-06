#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    url = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {url.status_code}")

    if url.status_code == 200:
        post = url.json()
        for post in post:
            print(post["title"])    

    else:
        print("Error fetching posts:", reponse.status_code)

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        post = reponse.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in post
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

        print("posts.csv successfully created!")
    else:
        print("Error fetching posts:", reponse.status_code)
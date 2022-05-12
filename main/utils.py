import json
from exceptions import *


def load_posts_from_json(path):
    try:
        with open(path, "r", encoding="UTF-8") as posts_list:
            return json.load(posts_list)
    except(FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded




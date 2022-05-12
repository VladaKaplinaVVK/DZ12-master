from flask import Blueprint, render_template, request
import logging
from config import POST_PATH
from main.utils import load_posts_from_json, search_posts
from exceptions import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template('index.html')


@main_blueprint.route("/search")
def page_search():
    s = request.args.get("s", "")
    logging.info("Поиск выполнение")
    try:
        posts = load_posts_from_json(POST_PATH)
    except DataJsonError:
        return "Проблема с  открытием файлов постов"
    filter_posts = search_posts(posts, s)
    return render_template('post_list.html', posts=filter_posts, s=s)

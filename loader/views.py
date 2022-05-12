
from flask import Blueprint, render_template, send_from_directory, request, json
import logging

from exceptions import WrongImgType
from loader.utils import save_picture, add_post
from config import POST_PATH
from main import utils
import json

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=['GET'])
def create_new_post():
    return render_template('post_form.html')




@loader_blueprint.route("/post", methods=['POST'])
def create_new_post_by_user(picture_path=None):
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутсвует часnь данных")
        return "Отсутствует часть данных"

    posts = utils.load_posts_from_json(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        return "Неверный тип изображения"
    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)

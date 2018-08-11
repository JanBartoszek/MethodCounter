from flask import request
import server


get_count = 0
post_count = 0


def count_gets():
    if request.method == 'GET':
        global get_count
        get_count += 1


def count_posts():
    if request.method == 'POST':
        global post_count
        post_count += 1

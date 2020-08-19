from flask import Response, render_template, redirect, url_for, request
import random
from application import app

@app.route('/')

@app.route('/get/animal', methods=['GET'])
def get_animal():

    animals = ['cow', 'cat', 'dog', 'lion']
    chosen = random.choice(animals)
    return Response(chosen, mimetype='text/plain')


@app.route('/post/animal', methods=['POST'])
def post_animal():
    data_sent = request.data.decode('utf-8')
    if data_sent == 'cow':
        sound = 'moo'
    elif data_sent == 'lion':
        sound = 'roar'
    elif data_sent == 'cat':
        sound = 'meow'
    elif data_sent == 'dog':
        sound = 'ruff'
    else:
        sound = 'We dont know that animal'
    return Response(sound, mimetype='text/plain')

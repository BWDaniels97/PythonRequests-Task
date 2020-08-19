from flask import render_template, redirect, url_for, request
from application import app
import requests


@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')



@app.route('/generate')
def generate():

    return render_template('generate.html', title='Generate')


@app.route('/generate/animal')
def generateanimal():
    animal = requests.get('http://35.189.107.29:5001/get/animal')
    sound = requests.post('http://35.189.107.29:5001/post/animal', data=animal.text)
    
    return render_template('generate.html', title='Generate', animal=animal.text, sound=sound.text )

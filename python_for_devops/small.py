#!/usr/bin/env python3

"""
Small Flask application
"""
from flask import Flask, redirect, request

app = Flask('basic app')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        redirect('https://www.google.com/search?q=%s' % request.args['q'])
    else:
        return '<h1>GET request from Flask!</h1>'

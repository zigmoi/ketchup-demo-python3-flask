#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    print("Received request.")
    return 'Hello World!'


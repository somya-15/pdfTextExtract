
import math
import os
# Importing the statistics module
import statistics
from os.path import dirname, join, realpath
from time import time
import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
import PyPDF2
from flask import (Flask, Response, flash, redirect, render_template, request,
                   url_for)
from flask import request
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage



app=Flask(__name__,template_folder='templates')
# importing required modules


# Upload folder
# UPLOAD_FOLDER = 'static/files'
# app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
app.config["UPLOAD_FOLDER"] = "static/"

# creating a pdf file object



@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        # file = open(,"r")
        pdfFileObj = open(app.config['UPLOAD_FOLDER'] + filename, 'rb')
	
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
        content = pageObj.extractText()
        return render_template('content.html', content=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

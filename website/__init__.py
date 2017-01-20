from flask import Flask
import os
import time

# Openshift defualts to GMT
time.tzset()

app = Flask(__name__)
import website.views

from flask import Flask
import os
import time

# Openshift defualts to GMT
os.environ['TZ'] = "America/New_York"
time.tzset()

app = Flask(__name__)
import website.views

from flask import Flask

app = Flask(__name__)
from video_annotator_generic import routes

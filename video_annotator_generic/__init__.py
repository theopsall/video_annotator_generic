from flask import Flask
from flask_login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.secret_key = "a2f8a7fa-fb61-11ea-8c89-0f4248d2074f"

from video_annotator_generic import routes

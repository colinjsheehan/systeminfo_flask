from flask import Flask

app = Flask(__name__,template_folder='templates')
app.debug=False
from app import views
from app import templates

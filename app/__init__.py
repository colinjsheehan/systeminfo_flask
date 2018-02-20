from flask import Flask

app = Flask(__name__,template_folder='/systeminfo_flask/app/templates')
app.debug=False
from app import views

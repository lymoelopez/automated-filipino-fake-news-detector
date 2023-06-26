from flask import Flask
from extension_webPage import webPage


app = Flask(__name__)
app.register_blueprint(webPage, url_prefix='/')

if __name__ == '__main__':
    app.run()


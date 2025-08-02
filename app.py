from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('pagina-web.html')

if __name__ == '__main__':
    app.run()
    
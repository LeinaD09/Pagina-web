from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¿Aceptas los términos y condiciones?'

if __name__ == '__main__':
    app.run()
    

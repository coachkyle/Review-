app = Flask(__Review__)

@app.route('/')
def home():
    return "Hello, this is your Flask app!"

if __Review__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print("Hello world!")
    return "say hello to yourself as euron"

@app.route('/msg', methods=['GET', 'POST'])
def printing_msg():
    return "print something about me"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, Response, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to home of flask"

@app.route('/cal', methods=['POST'])
def calculator():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        if num2!=0:
            return str(num1 / num2)
        else:
            return "Cannnot divide by zero"

# Using web-browser sample code
@app.route('/cal_browser', methods=['GET'])
def calculator_browser():
  
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        if num2!=0:
            return str(num1 / num2)
        else:
            return "Cannnot divide by zero"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
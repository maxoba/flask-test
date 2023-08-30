from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('result.html', result=result)
    return render_template('add_numbers.html')

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)

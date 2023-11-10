from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/toupper', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    error_message = None
    if request.method == 'POST':
        try:
            input_radius = float(request.form['radius'])
            result = input_radius * input_radius * 3.14
        except ValueError:
            error_message = "Please input valid numbers."
    return render_template('circle.html', result=result, error_message=error_message)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def triangle():
    result = None
    error_message = None
    if request.method == 'POST':
        try:
            input_height = float(request.form['height'])
            input_base = float(request.form['base'])
            result = (input_height * input_base) / 2
        except ValueError:
            error_message = "Please input valid numbers."
    return render_template('triangle.html', result=result, error_message=error_message)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def russian():

    if request.method == 'GET':
        return render_template('russian.html')

@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        word = "делаю"
        form_input = request.form['input']

        if word == form_input:
            return render_template('index.html',
                               form_input="正解！")
        else:
            return render_template('index.html',
                               form_input= "惜しい！正解は'делаю'です")

app.run(port=int(os.environ['PORT']))
if __name__ == '__main__':
    app.run(debug=True)

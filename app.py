from flask import Flask, request, render_template
import ru_func
import os
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def russian():
    if request.method == 'GET':
        return render_template('russian.html')

@app.route('/verb', methods=['GET'])
def verb():
    if request.method == 'GET':
        return render_template('verb.html')

@app.route('/verb/do_f', methods=['GET', 'POST'])
def do_f():
    if request.method == 'GET':
        return render_template('verb/do_f.html')
    else:
        # 活用形を入力する
        form_input = request.form['input']
        sql_verb = ru_func.verb_f()
        if sql_verb == form_input:
            return render_template('verb/do_f.html',
                               form_input="正解！")
        else:
            return render_template('verb/do_f.html',
                               form_input= "惜しい！正解は <" + sql_verb + "> です")

if __name__ == '__main__':
    app.run(debug=True)

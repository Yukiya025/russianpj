from flask import Flask, request, render_template
import ru_func
import random
import os
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def russian():
    if request.method == 'GET':
        return render_template('russian.html')

@app.route('/verb', methods=['GET'])
def verb():
    verb = ru_func.verb_p()
    return render_template("verb_p.html",
                            verb=verb)

@app.route('/verb/do_f', methods=['GET'])
def do_f():
    exs_l1, exs_l2, exs_l3 = ru_func.practice()
    ex0 = exs_l1[0]
    ex1 = exs_l2[0]
    ex2 = exs_l3[0]
    if request.method == 'GET':
        return render_template('verb/do_f.html',
                                ex0=ex0,
                                ex1=ex1
                                )
    return ex0, ex1, ex2

@app.route('/verb/do_f', methods=['POST'])
def do_fp():
    get1, get2, get3 = do_f()
    # 活用形を入力する
    form_input = request.form['input']
    if get3 == form_input:
        return render_template('verb/do_f.html',
                            ex0=get1,
                            ex1=get2,
                            form_input= "正解！<" + get3 + ">です。")
    else:
        return render_template('verb/do_f.html',
                            ex0=get1,
                            ex1=get2,
                            form_input= "正解は <" + get3 + "> です。もう一度してみてね。")

if __name__ == '__main__':
    app.run(debug=True)

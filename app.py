from flask import Flask, session, request, render_template
import ru_func
import random
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/', methods=['GET'])
def russian():
    if request.method == 'GET':
        return render_template('russian.html')


@app.route('/verb', methods=['GET'])
def verb():
    """
    動詞<<делать>>現在活用文法表表示
    """
    # question_no = random.randint(0, 5)
    session['secret_text']  = random.randint(0, 5)
    verb = ru_func.verb_p()
    return render_template("verb_p.html",
                            verb=verb)


@app.route('/verb/do_f', methods=['GET'])
def do_f():
    exs_l1, exs_l2, exs_l3 = ru_func.practice()
    question_no = session['secret_text']
    ex0 = exs_l1[question_no]
    ex1 = exs_l2[question_no]
    ex2 = exs_l3[question_no]
    if request.method == 'GET':
        return render_template('verb/do_f.html',
                                    ex0=ex0,
                                    ex1=ex1,
                                    question_no=question_no
                                    )
    return ex0, ex1, ex2, question_no


@app.route('/verb/do_f/<int:question_no>', methods=['POST'])
def do_fp(question_no):
    """
    ---form_inputコピペ用---
    делаю
    делаешь
    делает
    делаем
    делаете
    делают
    """
    get1, get2, get3, question_no = do_f()
    form_input = request.form['input']
    if request.method == 'POST':
        if get3 == form_input:
            return render_template('verb/do_f.html',
                                    ex0=get1,
                                    ex1=get2,
                                    form_input= "正解！<" + get3 + ">です。",
                                    question_no=question_no)
        else:
            return render_template('verb/do_f.html',
                                    ex0=get1,
                                    ex1=get2,
                                    form_input= "正解は <" + get3 + "> です。もう一度してみてね。",
                                    question_no=question_no)

if __name__ == '__main__':
    app.run(debug=True)

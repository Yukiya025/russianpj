# -*- coding: utf-8 -*-
import sqlite3
def verb_f():
    """
    1. データベースrucon_forms_lab.dbを開く
    2. 任意の人称代名詞の活用形を返す

    テーブル名を変数渡しにして使えるようにしたい
    """
    conn = sqlite3.connect('rucon_forms_lab.db')
    c = conn.cursor()

    ppnoun = ["я", "ты", "он", "мы", "вы", "они"]
    cor_ans = c.execute('SELECT ' + ppnoun[0] + ' FROM verbs WHERE id = 1') # s > cor_ans
    cor_ans = cor_ans.fetchone()
    return cor_ans[0] # cor_ans = cor_ans[0]

    """
    if cor_ans == "делаю":
        print("OK")
    else:
        print("No")
    """

def practice():
    conn = sqlite3.connect('rucon_forms_lab.db')
    c = conn.cursor()
    """

    """
    prac = c.execute('SELECT vb_y_id, firstpart, lastpart, я FROM vb_y WHERE id = 1')
    prac = prac.fetchone()
    print(str(prac[0]) + ". " + prac[1] + " " + prac[3] + " " + prac[2])
practice()

# -*- coding: utf-8 -*-
import sqlite3
import random
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

def practice():
    import random
    conn = sqlite3.connect('rucon_forms_lab.db')
    c = conn.cursor()
    """
    活用形を回答する問題を乱数表示
    """
    vbid_l = ["vb_y_id", "vb_t_id", "vb_o_id", "vb_mi_id", "vb_v_id", "vb_oni_id", "vb_m_id", "vb_fm_id", "vb_n_id", "vb_p_id"] # 0-9, i
    yap_l = ["я", "ты", "он", "мы", "вы", "они", "m", "f", "n", "p"] # 0-9, i
    vbtable_l = ["vb_y", "vb_t", "vb_o", "vb_mi", "vb_v", "vb_oni", "vb_m", "vb_fm", "vb_n", "vb_p"] # 0-9, i
    exs_l1 = [] # 例文前半を収録
    exs_l2 = [] # 例文後半を収録
    exs_l3 = [] # 例文解答を収録
    for i in range(len(vbid_l)):
        prac = c.execute('SELECT ' + vbid_l[i] + ', firstpart, lastpart, ' + yap_l[i] + ' FROM ' + vbtable_l[i] + ' WHERE id = 1')
        prac = prac.fetchone()
        ex1 = str(i) + ". " + prac[1] + " "
        ex2 = " " + prac[2]
        ex3 = prac[3]
        exs_l1.append(ex1)
        exs_l2.append(ex2)
        exs_l3.append(ex3)
    return exs_l1, exs_l2, exs_l3
"""
def do_f():
    exs_l1, exs_l2, exs_l3 = practice()
    a = exs_l1[3]
    b = exs_l2[3]
    c = exs_l3[3]
    return a, b, c
    ex0 = exs_l1[k]
    ex1 = exs_l2[k]
    ex2 = exs_l3[k]
"""    
def testinput():
    import random
    a, b, c = practice()
    j = random.randint(0, 5)
    print(a[j], b[j], c[j])
    d = input("russian: ")
    print(a[j], b[j], c[j])
    if d == c[j]:
        print("正解！")
    else:
        print("不正解")
# testinput()
def verb_p():
    conn = sqlite3.connect('rucon_forms_lab.db')
    c = conn.cursor()

    ppnoun = ["verb", "я", "ты", "он", "мы", "вы", "они"] # 0-6
    ppn_l = []
    for i in range(len(ppnoun)):
        cor_ans = c.execute('SELECT ' + ppnoun[i] + ' FROM verbs WHERE id = 1') # s > cor_ans
        cor_ans = cor_ans.fetchone()
        ppn_l.append(cor_ans[0])
    return ppn_l
    # print(ppn_l) # 7つの要素

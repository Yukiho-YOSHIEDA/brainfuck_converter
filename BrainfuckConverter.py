# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:39:35 2017

@author: saeyuki
"""

""" GUIモジュール """
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
""" ファイル入力モジュール """
import glob

""" 対応言語用クラス """
class langConfig:
    langName = ""
    extension = ""
    orders = []

    def __init__(self, langName, extension, orders):
        self.langName = langName
        self.extension = extension
        self.orders = orders

""" メインウィンドウの生成 """
form = tk.Tk()
form.title("Brainf*ck Converter")
form.geometry("600x400")

""" 対応言語読み込み """
path = glob.glob("./lang/*.txt") # pathの読み込み
langs = []

for var in path:
    langName = ""
    extension = ""
    orders = []

    f = open(var, 'r', encoding="utf-8")
    lines = f.readlines()
    f.close()

    for (i,line) in enumerate(lines):
        if i == 0:
            langName = line
        elif i == 1:
            extension = line
        elif i == 2:
            orders = line.split(",")

    langs.append(langConfig(langName, extension, orders))

print(langs[1].langName)

""" ボタンが押されたときの挙動設定群 """
def convert():
    print("convert")

def inputFile():
    print("inputFile")

def outputFile():
    print("outputFile")

""" ソースファイル入力画面の生成 """
inputTextBox = st.ScrolledText(form)
outputTextBox = st.ScrolledText(form)
inputTextBox.place(relheight = 0.6, relwidth = 0.4, relx = 0.01, rely = 0.05)
outputTextBox.place(relheight = 0.6, relwidth = 0.4, relx = 0.6, rely = 0.05)

""" コンバートボタンの生成 """
convertButton = tk.Button(form, text = "=>", command = convert)
convertButton.place(relheight = 0.1, relwidth = 0.1, relx = 0.45, rely = 0.3)

""" 拡張子選択 """
inputExtension = ttk.Combobox(form, )

""" ファイル入力ボタンの生成 """
inputFileButton = tk.Button(form, text = "参照", command = inputFile)
inputFileButton.place(relheight = 0.1, relwidth = 0.15, relx = 0.1, rely = 0.7)

""" ファイル出力ボタンの生成 """
outputFileButton = tk.Button(form, text = "出力", command = outputFile)
outputFileButton.place(relheight = 0.1, relwidth = 0.15, relx = 0.7, rely = 0.7)

""" メインウィンドウを表示 """
form.mainloop()
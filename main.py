from http.client import responses
from logging import root
from re import search
from tkinter import *
from turtle import title
from unittest import result
import requests
from tkinter import messagebox

root = Tk()
root.title('News App')
root.geometry('1700x500')


def fetchnews():
    country = country_text.get().lower()
    cc = 'none'
    country_code_api = 'https://api.printful.com/countries'
    country_code = requests.get(country_code_api)
    country_code_data = country_code.json()
    results = country_code_data['result']
    for r in results:
        if country == r['name'].lower():
            cc = r['code']
    if cc == 'none':
        messagebox.showerror('Error', 'country not found {}'.format(country))
    custom_link = 'https://newsapi.org/v2/top-headlines?country=' + \
        cc.lower()+'&apiKey=3ed8c02dfc00453fa5ec3d4960e8dfeb'
    responses = requests.get(custom_link)
    data = responses.json()
    myarticles = data['articles']
    mytitles = ''
    c = 1
    for a in myarticles:
        mytitles = mytitles+str(c)+' . '+a['title']+'\n'
        c = c+1
    title_news.config(text=mytitles)


country_text = StringVar()
country_text = Entry(root, textvariable=country_text)
country_text.pack()
search_button = Button(root, text='Get News', width=12, command=fetchnews)
search_button.pack()
title_news = Label(root, text='', font=('bold', 11))
title_news.pack()
root.mainloop()

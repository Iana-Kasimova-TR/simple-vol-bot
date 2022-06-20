# -*- coding: utf-8 -*-
import telebot
import config
import requests
import os
import re
import datetime
import json
import pygsheets
import pandas as pd
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#uri = os.getenv("DATABASE_URL")  # or other relevant config var
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)

#app = Flask('bot')    
#app.config['SQLALCHEMY_DATABASE_URI'] = uri
#db = SQLAlchemy(app)

#class Address:
#    def __init__(self, street, house, flat):
#        self.street = street
#        self.house = house
#        self.flat = flat



#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    userchatid = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String, nullable=False)
#    usersurname = db.Column(db.String, nullable=False)
#    street = db.Column(db.String, nullable=False)
#    house = db.Column(db.Integer, nullable=False)
#    flat = db.Column(db.Integer, nullable=False)

#authorization
gc = pygsheets.authorize(service_file='food-353617-6839c9bc6774.json')
sh = gc.open('food')

df = pd.DataFrame(columns=['Name', 'Surname'])

bot = telebot.TeleBot('5420433351:AAHxEwFYSn-6_Ld1mm_ujEVJbUx62rtpP5s')


@bot.message_handler(commands=['start'])
def start_command(message):
   print('I got the message') 
   bot.send_message(
       message.chat.id,
       'Hello!.\n' +
       'We are here to help you.'
   )

#if lambda is true we send a message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)

    # select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 

    words = message.text.split()

    if (len(words) != 2):
        bot.reply_to(message, "Please put correct information! Name and Surname")
    else:
        df.append({'Name':'Iana', 'Surname':'Kasimova'}, ignore_index=True)
        wks.set_dataframe(df,(1,1))
        bot.reply_to(message, "Thank you!")


#start the bot
bot.infinity_polling()    
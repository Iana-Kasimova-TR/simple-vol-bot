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
#gc = pygsheets.authorize(service_file='/Users/erikrood/desktop/QS_Model/creds.json')

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
#sh = gc.open('PY to Gsheet Test')


df = pd.DataFrame(columns=['Name', 'Surname', 'Adress'])

#select the first sheet #
#wks = sh[0]                                                                                                                                                                                                                 

#update the first sheet with df, starting at cell B2. 
#wks.set_dataframe(df,(1,1))


bot = telebot.TeleBot('5420433351:AAHxEwFYSn-6_Ld1mm_ujEVJbUx62rtpP5s')


@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Hello!.\n' +
       'We are here to help you.'
   )

#if lambda is true we send a message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


#start the bot
bot.infinity_polling()    
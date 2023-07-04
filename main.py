import telebot
from Server import Server 
API_KEY = '<ADD_YOUR_APIKEY'
bot = telebot.TeleBot(API_KEY)
#Hello Cmd
@bot.message_handler(commands=['Hello'])
def hello(message):
   bot.send_message(message.chat.id, 'Hello! It,s My Project.\n It,s My Bot.\n I,m still Building it.\n commands you can check\n /Hello\n /Greet\n /Help\n /Howoldareyou\n /Wallpaper\n /YTChannel\n /Bye\n Simply click on them')

#Greet Cmd
@bot.message_handler(commands=['Greet'])
def greet(message):
   bot.reply_to(message, 'Hey! hows it going')

@bot.message_handler(commands=['Help'])
def help(message):
  bot.send_message(message.chat.id, 'How can I help you')

@bot.message_handler(commands=['Howoldareyou'])
def old(message):
  bot.send_message(message.chat.id, 'I was created on 15-05-2022 By Aishwary Gathe. \nLinkedin : https://www.linkedin.com/in/aishwarygathe/ ')

@bot.message_handler(commands=['Wallpaper'])
def wp(message):
  bot.send_message(message.chat.id, 'I suggest you to visit this website \n>> https://www.pexels.com/search/desktop%20wallpaper/')

@bot.message_handler(commands=['YTChannel'])
def yt(message):
  bot.send_message(message.chat.id, 'Visit Our Youtube Channel \n>>https://www.youtube.com/channel/UC6Qx8SefRWMnibG8jxSLZTQ')
  
@bot.message_handler(commands=['Bye'])
def bye(message):
  bot.send_message(message.chat.id, 'Good Bye. Have a great day')
Server()
bot.polling()
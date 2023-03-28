import os
import telebot
import requests
import json
import csv

from apiomdb import get_movie_info
# TODO: 1.1 Get your environment variables
# yourkey = os.getenv()
# bot_id = os.getenv()

# bot = telebot.TeleBot('5692998061:AAGtgjoVQ_5HjmogooewO11ikj1HYFUS-sA')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, "Hey buddy" + "\N{grinning face with smiling eyes}" + "What can I get for you???\n"
                 """You can use "/assist" command if you need any help in searching with the bot.""")


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    with open('Search-List.csv', 'w', newline='') as file:
            file.write('')



@bot.message_handler(func=lambda message: botRunning, commands=['assist'])
def helpProvider(message):
    bot.reply_to(message,
                 '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    bot.send_message(message.chat.id, 'Movie found!')

    movie_name = message.text

    movie = movie_name.split(' ', 1)[1]
    print(movie)

    movie_info = get_movie_info(movie)
    print(movie_info)

    if movie_info:
        rating_string = f"IMDb Rating: {movie_info['imdb_rating']}\n"
        for rating in movie_info['ratings']:
            rating_string += f"{rating['Source']}: {rating['Value']}\n"

        message_text = (f"poster\n{movie_info['poster']}\n\n" +
                        f"Title: {movie_info['title']}\n\n" +
                        f"IMDB Rating: {movie_info['imdb_rating']}\n\n" +
                        f"Year of Release: {movie_info['year']}\n\n")
        print(movie_info)
        print(rating_string)
        print(message_text)

        # @bot.message_handler(content_types=['document', 'audio'])
        # def handle_docs_audio(message):
        #     bot.reply_to(message,f"Plot:\n{movie_info['Poster']}\n\n")

        # bot.reply_to(message,message_text)
        bot.send_message(message.chat.id, message_text)

        movie = [[movie_info['title'], movie_info['year'], movie_info['imdb_rating']]]
        print(movie)
    # TODO: 1.2 Get movie information from the API


    # TODO: 1.3 Show the movie information in the chat window
 
    # TODO: 2.1 Create a CSV file and dump the movie information in it
        movie=[[movie_info['title'] ,movie_info['year'],movie_info['imdb_rating']]]
        fields = ['Title', 'Year of Release', 'IMDb Rating' ] 

        with open("Search-List.csv", 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(movie)
        csvfile.close()
        
    else:{
        bot.reply_to(message, "Movie Not Found...")
    }  

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating your search list...')
    with open("Search-List.csv", 'r') as csvfile:
        
        bot.send_document(message.chat.id,csvfile)
        csvfile.close()
    
    # TODO: 2.2 Send downlodable CSV file to telegram chat


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand ' + '\N{confused face}')


bot.infinity_polling()
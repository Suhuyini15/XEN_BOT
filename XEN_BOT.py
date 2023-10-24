import os 
from dotenv import load_dotenv,find_dotenv
from langchain.llms import openai
from telegram import Update
from telegram.ext import CallbackContext, Filters,  MessageHandler, Updater
from langchain.chat_models import ChatOpenAI

#load environment from .env file
load_dotenv(find_dotenv(), inplace = True)

llm = ChatOpenAI(openai_api_key=os.getenv("AI_API"))

#Define to handle messages from users
def ai_messages(update:Update ,context:CallbackContext):
    message = update.message.text
    response = llm.predict(message)
    update.message.reply_text(response)



def main():
    # Initialize the Telegram Updater
    api_key = os.getenv("BOT_API")
    updater = Updater(api_key, use_context= True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    #Resgister a message handler for messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,ai_messages))

    updater.start_polling()

    updater.idle()

main()    

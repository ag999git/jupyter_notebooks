#  Author:- Anurag Gupta # email:- 999.anuraggupta@gmail.com
from telegram.ext import Updater, CommandHandler
# For token use your token
my_updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)
my_dispatcher = my_updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id # Get id of the chat. 
    f_name = update.effective_chat.first_name # First name of bot user
    l_name = update.effective_chat.last_name # Last name of bot user
    full_name = f_name + '' + l_name  # Full name of bot user
    out_text = 'Hi {0} {1} from bot'.format(f_name, l_name)
    # The print functions are to show the contents of the variables
    # You can remove the print functions 
    print(update)
    print('effective_chat ->',update.effective_chat)
    print('chat_id->', chat_id)
    print('bot->', context.bot)
    
    my_bot = context.bot  # my_bot is an object of type telegram.Bot
    # print(my_bot)
    my_bot.send_message(chat_id, text= out_text)


start_handler = CommandHandler('start', start)
my_dispatcher.add_handler(start_handler)


# my_updater.start_polling() starts the bot, and the bot begins 
# to start polling Telegram for any chat updates.  
# The bot has its own separate threads so it wont halt your Python script.
my_updater.start_polling()
# my_updater.idle() command is used to block the script until 
# the user sends a command to break from the Python script such as ctrl-c on windows
my_updater.idle()



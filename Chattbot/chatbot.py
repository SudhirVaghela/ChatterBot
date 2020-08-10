from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('xox')
# bot_response = bot.get_response("hi")
# print(bot_response)

trainbot = ListTrainer(bot)
con = open('convo.txt')
trainbot.train(con.readlines())

print('start to chat.....')
print('hey sudhir')

while True:
    user = input()
    bot_response = bot.get_response(user)
    print(bot_response)


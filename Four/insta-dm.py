#code based on Youtube video by Coding 101 with Steve : https://www.youtube.com/watch?v=5qkc0ybtu6k

#importing library
from time import sleep
from instabot import Bot

#initialize bot
myinstabot = Bot()

#logging into carsoncodes 🤖
myinstabot.login(username ='carsoncodes.py', password='-')

#getting a list of engaged followers from a profile similar to mine

target_users = myinstabot.get_user_likers("python.hub")

for count, user in enumerate(target_users):
    if count > 120:
        break
    message = """Hi! I’m trying to relearn how to code in python through the
    100daysofcode challenge, check out my page and follow to show support! <3 """
    myinstabot.send_message(message, [user])
    sleep(20)

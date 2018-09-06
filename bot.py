# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['656850436:AAEoqPS-nJ3OM8eok1gWOks5ny7whGLodoQ']
some_api_token = os.environ['656850436:AAEoqPS-nJ3OM8eok1gWOks5ny7whGLodoQ']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

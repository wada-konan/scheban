# -*- coding: utf-8 -*-
from slackbot.bot import respond_to


@respond_to('(.*)')
def tell_schedule(message, something):
    body = message.body
    text, ts, user_id = body['text'], body['ts'], body['user']
    reply_message = ''
    message.reply(reply_message)

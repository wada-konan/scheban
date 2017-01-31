# -*- coding: utf-8 -*-
import sys
from slackbot.bot import respond_to
sys.path.append('..')
from google_calendar import get_upcoming_events, events2text


@respond_to('今後の予定を教えて')
def respond_schedule(message):
    calendar_id = 'tdauvvfdl5rvamauvfg1hc555k@group.calendar.google.com'
    reply_message = events2text(calendar_id=calendar_id)
    message.reply(reply_message)

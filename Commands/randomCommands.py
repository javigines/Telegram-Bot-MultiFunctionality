#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging												## System module
log = logging.getLogger(__name__)

import Functions.randomFunctions as rf

import Functions.basicData as bd
import Functions.message as ms										    ## Own module


#Command /flip
def flip(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=rf.flipCoinFunction() , reply_to_message_id=bd.message.message_id)

# Forward Message
def getInfo(bot, update):
	bd.startWithCommand(bot, update)
	
	bot.sendMessage(chat_id=bd.chat_id, text=rf.forwardedMessageFunction(bd.message) , reply_to_message_id=bd.message.message_id)


#Command /random
def randomNumer(bot, update, args=None):
	bd.startWithCommand(bot, update)

	try:
		if args is None or args == '' or args == []:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.numberAnswer.replace("$args1", str(rf.randomNumberFunction())), reply_to_message_id=bd.message.message_id)
		else:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.numberAnswer.replace("$args1", str(rf.randomNumberFunction(int("".join(args))))) , reply_to_message_id=bd.message.message_id)
	except ValueError as e:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.noNumber , reply_to_message_id=bd.message.message_id)


#Command /remindMe
def remindMe(bot, update, args=None):
	bd.startWithCommand(bot, update)

#Command /stopwatch
def stopwatch(bot, update):
	bd.startWithCommand(bot, update)

#Command /newVote
def newVote(bot, update):
	bd.startWithCommand(bot, update)

#Command /secretMessage
def secretMessage(bot, update, args=None):
	bd.startWithCommand(bot, update)

#Command /anonymousMessage
def anonymousMessage(bot, update, args=None):
	bd.startWithCommand(bot, update)

#Command /case
def case(bot, update):
	bd.startWithCommand(bot, update)

#Command /imgur
def imgur(bot, update):
	bd.startWithCommand(bot, update)

#Command /shortLink
def shortLink(bot, update):
	bd.startWithCommand(bot, update)

#Command /note
def note(bot, update):
	bd.startWithCommand(bot, update)




log.info('RandomCommands Module Loaded.')

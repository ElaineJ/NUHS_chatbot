#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from RasaNLU import interpreter
import NewConditionQuestions as cd

import logging
import time
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

AGE, CHECKSURGERY, CHECKSURGERYTYPE, CHECKCONDITION, CHECKSIMILAR, CHECKREOCCURENCE, FLACC1, FLACC2, FLACC3, FLACC4, FLACC5, TOCIRCUMBILLARY, TOCIRCUMPUS, TOPAINKILLER, ENDOFCIRCUMCISION, TOBILLARYSTRING, BILLARYDRAINAGEEND, PROCESSCONDITIONSTART, PROCESSCONDITION1, HELPFUL = range(20)


# def start(bot, update):
#     reply_keyboard = [['Boy', 'Girl', 'Other']]

#     update.message.reply_text(
#         'Hi! My name is Professor Bot. I will hold a conversation with you. '
#         'Send /cancel to stop talking to me.\n\n'
#         'Are you a boy or a girl?',
#         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

#     return GENDER

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])

def start(bot,update):
    reply_keyboard = [['0-3mths', '3-6mths', '6-12mths'],['12-24mths','2-5yrs','5-10yrs'],['More than 10yrs']]
    update.message.reply_text(
        "Sorry, the doctor is not in at the moment, my name is Docs,"
        "I am here to help you understand your child's symptoms better."
        "Can you tell me how old your child is ?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return AGE

def CheckSurgery(bot, update,user_data):
    reply_keyboard = [['Yes', 'No']]
    user = update.message.from_user #user idea
    text = update.message.text #text from previous state
    user_data["age"]=text #store age for later use
    
    user_data["helpfulness"]=1
    if text!="Yes" and text!="No":
        logger.info("Child's age %s: %s", update.message.text)
        update.message.reply_text('Did your child just undergo a surgery recently? ',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    elif text=="Yes":
        logger.info("Child's age %s: %s", update.message.text)
        update.message.reply_text('Did your child just undergo a surgery recently? ',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    elif text=="No":
        return ConversationHandler.END

    return CHECKSURGERY

def CheckSurgeryType(bot, update,user_data):
    #print (update)
    reply_keyboard = [['Circumcision', 'Billary Drainage']]
    reply_keyboard2 = [['Yes', 'No']]
    
    
    user = update.message.from_user
    text = update.message.text
    logger.info("Child undergone surgery %s: %s", update.message.text)
    
    
    if text == 'Yes':
        user_data["helpfulness"]=0 #to control whether we should touch helpful count in processcondition
        try:    
            user_data["helpfulcount"]+=1
        except KeyError:
            user_data["helpfulcount"]=0
        update.message.reply_text('What surgery? ',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    elif text == 'No':
        update.message.reply_text('Has your child been admitted to hospital recently? ',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True))

    return CHECKSURGERYTYPE

# def checkSurgeryType(bot, update):
#     #print (update)

#     user = update.message.from_user
#     textSurgery = update.message.text
#     logger.info("Child undergone %s surgery", update.message.text)


#     return CHECKSURGERYTYPE,textSurgery

def Flacc1(bot,update,user_data):

    reply_keyboard = [['1','2','3']]

    user = update.message.from_user
    text = update.message.text
    user_data['surgery']=text

    update.message.reply_text("Observing your child's expression he/she shows signs of:  "
                              "\n1. smiling or showing no particular expression"
                              "\n2. shows the occasional grimice or frown or is withdrawn or uninterested "
                              "\n3. Is frequently quivering his/her chin or is clenching his/her jaw", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
#    update.message.reply_text("Observing your child's leg movements he/she shows signs of:  "
#                              "\n1. Normal position or relaxed"
#                              "\n2. Uneasiness, restless or tense "
#                              "\n3. Kicking, or legs drawn up", 
#                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    





    return FLACC1

def Flacc2(bot,update,user_data):
    reply_keyboard = [['1','2','3']]
    
    user = update.message.from_user
    text = update.message.text
    user_data['score']=int(text)-1
    update.message.reply_text("Observing your child's leg movements he/she shows signs of:"
                              "\n1. Normal position or relaxed"
                              "\n2. Uneasiness, restless or tense "
                              "\n3. Kicking, or legs drawn up", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))




    return FLACC2

def Flacc3(bot,update,user_data):
    reply_keyboard = [['1','2','3']]
    
    user = update.message.from_user
    text = update.message.text
    
    #score=Flacc2[1]
    user_data['score']=int(text)-1+user_data['score']   


    update.message.reply_text( "Observing your child's body behaviour he/she shows signs of: "
                              "\n1. Lying quietly, normal position, moves easily"
                              "\n2. Squirming, shifting, back and forth, tense "
                              "\n3. Arched in pain, rigid or jerking", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))




    return FLACC3

def Flacc4(bot,update,user_data):
    reply_keyboard = [['1','2','3']]
    
    user = update.message.from_user
    text = update.message.text
    #logger.info("Child had done surgery: %s: %s", update.message.text)
    user_data['score']=int(text)-1+user_data['score']
    
    update.message.reply_text("Observing your child's cry he/she shows signs of:   "
                              "\n1. Not crying"
                              "\n2. Moaning or whimpering; occasional complaint "
                              "\n3. Crying steadily, screams or sobs, frequent complaints", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return FLACC4

def Flacc5(bot,update,user_data):
    reply_keyboard = [['1','2','3']]
    
    user = update.message.from_user
    text = update.message.text
    #logger.info("Child had done surgery: %s: %s", update.message.text)

    user_data['score']=int(text)-1+user_data['score']
    score=user_data['score']


    update.message.reply_text("How consolable is your child? he/she is: "
                              "\n1. Content, relaxed"
                              "\n2. Reassured by occasional touching, hugging or being talked to, distractible "
                              "\n3. Difficult to console or comfort ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FLACC5

def ToCircumBillary(bot,update,user_data):
    reply_keyboard = [['Bleeding','Not Bleeding']]
    reply_keyboard1 = [['Yes','No']]
    user = update.message.from_user
    text = update.message.text
    #logger.info("Child had done surgery: %s: %s", update.message.text)

    user_data['score']=int(text)-1+user_data['score']
    score=user_data['score']
    surgery=user_data['surgery']
    

    if score<6:
        if surgery=="Circumcision":
            update.message.reply_text("Is there any bleeding? ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        elif surgery=="Billary Drainage":
            update.message.reply_text("Is there any fluid coming out of drain? ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True))
    elif score>=6:
        update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    return TOCIRCUMBILLARY

def ToCircumPus(bot,update,user_data):
    reply_keyboard = [['Yes','No']]
    
    user = update.message.from_user
    text = update.message.text
    user_data["bleed?"]=text###to store from previous question
    update.message.reply_text("Is there any pus around the wound? ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return TOCIRCUMPUS

def ToPainKiller(bot,update,user_data):
    reply_keyboard = [['Yes','No']]
    
    user = update.message.from_user
    text = update.message.text
    if text=="Yes":
        update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Does giving the child prescribed pain medication help? ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return TOPAINKILLER

def EndOfCircumcision(bot,update,user_data):
    reply_keyboard = [['Yes','No']]
    reply_keyboardH=[[ "Helpful", "Not Helpful"]]
    user = update.message.from_user
    text = update.message.text
    if user_data["bleed?"]=="Bleeding" and text=="No":
        update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Educational resource on wound dressing")
        time.sleep(10)
        update.message.reply_text("Was this helpful?", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboardH, one_time_keyboard=True))
    return ENDOFCIRCUMCISION

def ToBillaryString(bot,update,user_data):
    reply_keyboard = [['Yes','No']]
    
    user = update.message.from_user
    text = update.message.text
    if text=="No":
        update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    elif text=="Yes":
        update.message.reply_text("Is the string around the drain intact? ", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return TOBILLARYSTRING

def BillaryDrainageEnd(bot,update,user_data):
    reply_keyboard = [['Yes','No']]
    reply_keyboardH=[[ "Helpful", "Not Helpful"]]
    user = update.message.from_user
    text = update.message.text
    if text=="Yes":
        update.message.reply_text("Educational resource on Billary Drainage ") 
        time.sleep(10)
        update.message.reply_text("Was this helpful?", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboardH, one_time_keyboard=True))
    elif text=="No":
        update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    return BILLARYDRAINAGEEND


def CheckCondition(bot, update, user_data):
    reply_keyboard = [['Asthma','Gastroenteritis','Severe Infection','Fits']]
    user = update.message.from_user
    text = update.message.text
    
    user_data["helpfulness"]=0 #to control whether we should touch helpful count in processcondition
    try:    
        user_data["helpfulcount"]+=1
    except KeyError:
        user_data["helpfulcount"]=0
    #logger.info("Child admitted to hospital recently? %s: %s", update.message.text)
    if text == 'Yes':
        update.message.reply_text("Was your child admitted for the following conditions? ",
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    else:
        update.message.reply_text("Alright, What seems to be the problem")

    return CHECKCONDITION

def CheckSimilar(bot, update, user_data):
    reply_keyboard=[[ "Yes", "No"]]
    
    user = update.message.from_user
    text = update.message.text
    user_data["Past Symptoms"]=text
    
    update.message.reply_text('Are the symptoms similar to the previous admission? ',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return CHECKSIMILAR

def CheckReoccurence(bot, update, user_data):
    
    user = update.message.from_user
    text = update.message.text
    
    if text=="Yes" or text=="No":
        previous=user_data["Past Symptoms"]
    
    if text=="Yes":
        update.message.reply_text('A reoccurence of '+previous+" can have serious implications. Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
        return ConversationHandler.END
    elif text=="Stop":
        update.message.reply_text("Okay, please bring your child to A&E asap for assistance!")
        return ConversationHandler.END
    else:
        update.message.reply_text("Alright, What seems to be the problem")
    return CHECKREOCCURENCE
 
###PROCESS CONDITION##########
def ProcessConditionStart(bot, update, user_data):
    reply_keyboard=[[ "Yes", "No"]]
    reply_keyboardC=[["0","1","2",">3"]]
    reply_keyboardD=[["0-3","3-6",">6"]]
    reply_keyboardV=[["0-3",">3"]]
    user = update.message.from_user
    text = update.message.text
    if user_data["helpfulness"]==1:
        try:    
            user_data["helpfulcount"]+=1
        except KeyError:
            user_data["helpfulcount"]=0
    else:
        pass
    #initialise all my counts
    user_data["SequenceCount"]=0
    user_data["CorrectCount"]=0
    user_data["Start"]=1 #needed to count number of Questions asked.
    Dictionary=interpreter.parse(text)
    user_data["Dictionary"]=Dictionary  
    user_data["Dictionary"]=Dictionary 
    if Dictionary["entities"]==[]:
        user_data["entity"]=[]
    else:
        user_data["entity"]=Dictionary["entities"][0]["entity"]
    
    
    if user_data["entity"]=="Constipation":
        user_data["value"]=Dictionary["entities"][0]["value"]
        
        #output relevant keyboard
        if user_data["Start"]==1:
            output=cd.ConstipationQuestion(user_data["value"],user_data["SequenceCount"],user_data["Start"])       
            question=output[0]
            user_data["Start"]+=1
            user_data["SequenceCount"]=output[1]
            if user_data["SequenceCount"]==1: #speical markup for how many times pass motion
                update.message.reply_text(question,
                                          reply_markup=ReplyKeyboardMarkup(reply_keyboardC, one_time_keyboard=True))
            else: # everything else
               update.message.reply_text(question,
                                         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    elif user_data["entity"]=="Gastroenteritis":
        user_data["value"]=Dictionary["entities"][0]["value"]
        if user_data["Start"]==1:
            output=GastroenteritisQuestion(user_data["value"],user_data["SequenceCount"],user_data["Start"])
            question=output[0]
            user_data["Start"]+=1
            user_data["SequenceCount"]=output[1]
            if user_data["SequenceCount"]==1: #speical markup for Diarrhea
                update.message.reply_text(question,
                                          reply_markup=ReplyKeyboardMarkup(reply_keyboardD, one_time_keyboard=True))
            else: # everything else
               update.message.reply_text(question,
                                         reply_markup=ReplyKeyboardMarkup(reply_keyboardV, one_time_keyboard=True))
        
    elif user_data["entity"]==[]:
        update.message.reply_text("Sorry, i cannot understand, can you tell me your problem again? if i still cant understand you after many tries, please seek help at A&E")          
    
    return PROCESSCONDITIONSTART

def ProcessCondition1(bot, update, user_data):
    reply_keyboard=[[ "Yes", "No"]]
    reply_keyboardC=[["0","1","2",">3"]]
    reply_keyboardD=[["0-3","3-6",">6"]]
    reply_keyboardV=[["0-3",">3"]]
    reply_keyboardH=[["Helpful","Not Helpful"]]
    
    user = update.message.from_user
    text = update.message.text
    
    Dictionary=user_data["Dictionary"]
    
    
    #from processtart, the first correctcount process, processess with the original sequence count
    #after that it is from original sequence count+1
    
    
    #For constipation
    if user_data["entity"]=="Constipation":
        #Process redflag
        redflag=[3,6]
        if user_data["SequenceCount"] in redflag:
            if text=="Yes":
                update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
                return ConversationHandler.END
            else:
                user_data["CorrectCount"]=cd.CorrectCount(user_data["entity"],user_data["value"],text,user_data["CorrectCount"],user_data["SequenceCount"])
        else:
            user_data["CorrectCount"]=cd.CorrectCount(user_data["entity"],user_data["value"],text,user_data["CorrectCount"],user_data["SequenceCount"])
        
        #asking questions
        if user_data["CorrectCount"]<3 and user_data["Start"]<7:
            #Where i output my sequence and correct count
            output=cd.ConstipationQuestion(user_data["value"],user_data["SequenceCount"],user_data["Start"])       
            question=output[0] #i get the question
            user_data["Start"]+=1 #i change this to not starting anymore
            user_data["SequenceCount"]=output[1]
            user_data["value"]=text
            if user_data["SequenceCount"]==1: #special markup for how many times pass motion
                user_data["SequenceCount"]=output[1]
                update.message.reply_text(question,
                                          reply_markup=ReplyKeyboardMarkup(reply_keyboardC, one_time_keyboard=True))
            else: # everything else
                user_data["SequenceCount"]=output[1]
                update.message.reply_text(question,
                                          reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        elif user_data["CorrectCount"]>=3:
            update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
            return ConversationHandler.END
        elif user_data["Start"]>=7:
            update.message.reply_text("Constipation education resource")
            time.sleep(10)
            update.message.reply_text("Was this helpful?",
                                      reply_markup=ReplyKeyboardMarkup(reply_keyboardH, one_time_keyboard=True))
    
    elif user_data["entity"]=="Gastroenteritis":
        #Process redflag
        redflag=[2,4,5,6]
        redflagage=['0-3mths', '3-6mths']
        redflaganswers=["3-6",">6",">3"]
        if user_data["SequenceCount"] in redflag :
            if text=="Yes":
                update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
                return ConversationHandler.END
            else:
                pass
        #Process redflag for that age group
        if user_data["Age"] in redflagage:
            if text in redflaganswers:
                update.message.reply_text("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
                return ConversationHandler.END
        #giving relevant advice
        Advice=""
        AdviceDict={'1':"Advice for diarrhea\n", '3':"Advice for vomit\n", '7':"Advice for drink water\n"}
        AdviceSequence=[1,3,7]
        if user_data["Sequencecount"] in AdviceSequence:
            Advice=AdviceDict[str(user_data["Sequencecount"])]

        
        #Asking Questions
        if user_data["Start"]<8:
            output=cd.ConstipationQuestion(user_data["value"],user_data["SequenceCount"],user_data["Start"])       
            question=Advice+output[0] #i get the question
            user_data["Start"]+=1 #i change this to not starting anymore
            user_data["SequenceCount"]=output[1]
            user_data["value"]=text
            if user_data["SequenceCount"]==1 or user_data["SequenceCount"]==3: #special markup for how many times pass motion
                user_data["SequenceCount"]=output[1]
                if user_data["SequenceCount"]==1:
                    update.message.reply_text(question,
                                              reply_markup=ReplyKeyboardMarkup(reply_keyboardD, one_time_keyboard=True))
                else:
                    update.message.reply_text(question,
                                              reply_markup=ReplyKeyboardMarkup(reply_keyboardV, one_time_keyboard=True))
            else:
                update.message.reply_text(question,
                                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        elif user_data["Start"]>=8:
            #update.message.reply_text("Constipation education resource")
            time.sleep(10)
            update.message.reply_text("Was this helpful?",
                                      reply_markup=ReplyKeyboardMarkup(reply_keyboardH, one_time_keyboard=True))
            
    return PROCESSCONDITION1    
    
def Helpful(bot,update,user_data):
    reply_keyboard = [['Try again','Stop']]
    
    user = update.message.from_user
    text = update.message.text
    user_data["helpful?"]=text###to store from previous question
    
    user_data["helpfulness"]=1
    if text=="Helpful":
        update.message.reply_text('Glad to be of service! ')
        return ConversationHandler.END
    elif text=="Not Helpful":
        if user_data["helpfulcount"]==0:
            update.message.reply_text("I am sorry :(,Would you like to try again?",
                                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
            
        else:
           update.message.reply_text("I am sorry, please bring your child to A&E asap to be seen by the doctor!") 
           return ConversationHandler.END
    return HELPFUL

# def photo(bot, update):
#     user = update.message.from_user
#     photo_file = bot.get_file(update.message.photo[-1].file_id)
#     photo_file.download('user_photo.jpg')
#     logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
#     update.message.reply_text('Gorgeous! Now, send me your location please, '
#                               'or send /skip if you don\'t want to.')

#     return LOCATION


# def skip_photo(bot, update):
#     user = update.message.from_user
#     logger.info("User %s did not send a photo.", user.first_name)
#     update.message.reply_text('I bet you look great! Now, send me your location please, '
#                               'or send /skip.')

#     return LOCATION


# def location(bot, update):
#     user = update.message.from_user
#     user_location = update.message.location
#     logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
#                 user_location.longitude)
#     update.message.reply_text('Maybe I can visit you sometime! '
#                               'At last, tell me something about yourself.')

#     #return BIO
#     return ConversationHandler.END

# def skip_location(bot, update):
#     user = update.message.from_user
#     logger.info("User %s did not send a location.", user.first_name)
#     update.message.reply_text('Thank you! I hope we can talk again some day.')

#     #return BIO
#     return ConversationHandler.END


# def skip_location(bot, update):
#     user = update.message.from_user
#     logger.info("User %s did not send a location.", user.first_name)
#     update.message.reply_text('You seem a bit paranoid! '
#                               'At last, tell me something about yourself.')

#     #return BIO
#     return ConversationHandler.END


# def bio(bot, update):
#     user = update.message.from_user
#     logger.info("Bio of %s: %s", user.first_name, update.message.text)
#     update.message.reply_text('Thank you! I hope we can talk again some day.')

#     return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("550344658:AAGg8R25ypC3ttgRCMFFBtDG5k9FS5RueK0")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            AGE: [RegexHandler('^(0-3mths|3-6mths|6-12mths|12-24mths|2-5yrs|5-10yrs|More than 10yrs)$', CheckSurgery,pass_user_data=True)],

            CHECKSURGERY: [RegexHandler('^(Yes|No)$', CheckSurgeryType,pass_user_data=True)],

            CHECKSURGERYTYPE: [RegexHandler('^(Circumcision|Billary Drainage)$', Flacc1,pass_user_data=True),
                               RegexHandler('^(Yes|No)$', CheckCondition,pass_user_data=True)],
            
            #for Surgery
            FLACC1 : [RegexHandler('^(1|2|3)$',Flacc2,pass_user_data=True)],
            FLACC2 : [RegexHandler('^(1|2|3)$',Flacc3,pass_user_data=True)],
            FLACC3 : [RegexHandler('^(1|2|3)$',Flacc4,pass_user_data=True)],
            FLACC4 : [RegexHandler('^(1|2|3)$',Flacc5,pass_user_data=True)],
            FLACC5 : [RegexHandler('^(1|2|3)$',ToCircumBillary,pass_user_data=True)],
            TOCIRCUMBILLARY:[RegexHandler('^(Bleeding|Not Bleeding)$',ToCircumPus,pass_user_data=True),
                             RegexHandler('^(Yes|No)$',ToBillaryString,pass_user_data=True)],
         #Circumcision
            TOCIRCUMPUS:[RegexHandler('^(Yes|No)$',ToPainKiller,pass_user_data=True)],
            TOPAINKILLER:[RegexHandler('^(Yes|No)$',EndOfCircumcision,pass_user_data=True)],
            ENDOFCIRCUMCISION:[RegexHandler('^(Helpful|Not Helpful)$',Helpful,pass_user_data=True)],
          #BillaryDrainage
            TOBILLARYSTRING:[RegexHandler('^(Yes|No)$',BillaryDrainageEnd,pass_user_data=True)],
            BILLARYDRAINAGEEND:[RegexHandler('^(Helpful|Not Helpful)$',Helpful,pass_user_data=True)],
        #admit to hospital
            CHECKCONDITION: [RegexHandler('^(Asthma|Gastroenteritis|Severe Infection|Fits)$', CheckSimilar, pass_user_data=True),
                             MessageHandler(Filters.text, ProcessConditionStart, pass_user_data=True)],
            CHECKSIMILAR: [RegexHandler('^(Yes|No)$', CheckReoccurence, pass_user_data=True)],
            CHECKREOCCURENCE: [MessageHandler(Filters.text, ProcessConditionStart, pass_user_data=True)],
            
            #To link to interpreter.
            PROCESSCONDITIONSTART: [RegexHandler('^(Yes|No)$', ProcessCondition1, pass_user_data=True),
                                    RegexHandler('^(0|1|2|>3)$', ProcessCondition1, pass_user_data=True),
                                    RegexHandler('^(0-3|3-6|>6)$', ProcessCondition1, pass_user_data=True),
                                    RegexHandler('^(0-3|>3)$', ProcessCondition1, pass_user_data=True),
                                    MessageHandler(Filters.text,ProcessConditionStart, pass_user_data=True)],
            PROCESSCONDITION1: [RegexHandler('^(Yes|No)$', ProcessCondition1, pass_user_data=True),
                                RegexHandler('^(0|1|2|>3)$', ProcessCondition1, pass_user_data=True),
                                RegexHandler('^(0-3|3-6|>6)$', ProcessCondition1, pass_user_data=True),
                                RegexHandler('^(0-3|>3)$', ProcessCondition1, pass_user_data=True),
                                RegexHandler('^(Helpful|Not Helpful)$', Helpful, pass_user_data=True)], 
            HELPFUL: [RegexHandler('^(Try again|Stop)$', CheckReoccurence, pass_user_data=True)]
                                
            # BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
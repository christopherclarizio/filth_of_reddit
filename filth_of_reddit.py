'''
Created on May 31, 2017

@author: Christopher Clarizio
'''

#===================================================================================#

import sys
import os
import re
import optparse
from watson_developer_cloud import ToneAnalyzerV3
import praw
import twitter

#===================================================================================#

def parse_command_line():
    usage = ("usage: %prog [options] USERNAME PASSWORD\n"
             "\tUSERNAME:    sets your username for the bot\n"
             "\tPASSWORD:    sets your password for the bot")
    
    parser = optparse.OptionParser(usage=usage)
    
    parser.add_option("-r", 
                      action="store", 
                      dest = "sub", 
                      default = "politics",
                      help = "subreddit to search")

    options, args = parser.parse_args()

    if len(args) != 0:
        parser.error("Invalid number of arguments provided.")

    return options

def analyze_comment_tone(comment):
    result = tone_analyzer.tone(text = comment)
    
    anger   = result["document_tone"]["tone_categories"][0]["tones"][0]["score"]
    disgust = result["document_tone"]["tone_categories"][0]["tones"][1]["score"]
    fear    = result["document_tone"]["tone_categories"][0]["tones"][2]["score"]
    joy     = result["document_tone"]["tone_categories"][0]["tones"][3]["score"]
    sadness = result["document_tone"]["tone_categories"][0]["tones"][4]["score"]
    
    '''
    print("commets: "       +comment)
    print("anger score: "   +str(anger))
    print("disgust score: " +str(disgust))
    print("fear score: "    +str(fear))
    print("joy score: "     +str(joy))
    print("sadness score: " +str(sadness))
    '''
    
    return anger

def format_comment(comment):
    formatted_comment = comment.replace('\n', ' ')
    formatted_comment = formatted_comment.encode('utf-8')
    formatted_comment = str(formatted_comment)
    formatted_comment = formatted_comment[2:len(formatted_comment)-1]
    formatted_comment = formatted_comment[:140]
    
    return formatted_comment

#===================================================================================#

#create instance of reddit
reddit = praw.Reddit(client_id = 'SYTLsPErdZx6IA',
                     client_secret = 'BCnhIarA9gcg7eQDOKLSyl4i0y0',
                     user_agent = 'filth_of_reddit:v0.0 (by /u/PID_ONE)')

#create instance of tone analyzer
tone_analyzer = ToneAnalyzerV3(
  version = "2017-06-04",
  username = "06ea1287-c7f8-4a49-82fc-c9b94a5fc9cb",
  password = "YbRJ7tY5esig")

#create instance of twitter
twitter = twitter.Api(consumer_key = '6LNKl5xPLUTLRJhiVTLFpsqpk',
                      consumer_secret  = 'R7uCotJ4G5lC8XP1Ncq1C8982mkxlq5hO11N5o7E9K8mOk8alX',
                      access_token_key = '872343913092325376-I7qdDATXj5A0bZbWR0IwaTJGwKVKhmw',
                      access_token_secret = 'zhKYBbmdBjohoBd5eq3ZGY2kO4YqOwbk3Bx7SXSDWu3k7')


#create instance of output file
out = open('out.txt', 'w')

#print welcome message
print('Welcome to the filth of Reddit \n--->Highlighting the worst Reddit has to offer\n')

#call function to parse command line options
options = parse_command_line()
sub = options.sub

#get instance of subreddit
subreddit = reddit.subreddit(sub)

#create dictionary to store comments and scores
scores = {}

print("analyzing comments...")

#iterate thrhough limit number of submissions in subreddit
for submission in subreddit.controversial(limit=10):
    submission.comments.replace_more(limit=0)
    print("submission title: "+submission.title.replace('\n', ' '), file = out)
    num = 0
    for comment in submission.comments.list():
        num = num + 1
        formatted_comment = format_comment(comment.body)
        #score = analyze_comment_tone(truncated_comment)
        score = 0 #test remove this
        scores[formatted_comment] = score
        print(formatted_comment, file = out)
        print(score, file = out)

print("finished analyzing comments")
print("sorting comments...")

sorted_scores = sorted(scores, key = scores.get)
sorted_scores.reverse()
worst = sorted_scores[0]

print("finished sorting comments")
print("posting worst to twitter")

twitter.PostUpdate(worst)

print("finished posting to twitter")
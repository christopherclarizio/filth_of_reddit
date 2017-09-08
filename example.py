'''
Created on May 31, 2017

@author: Christopher Clarizio
'''
from oauthlib.oauth1.rfc5849.endpoints import access_token

'''
import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
  version = "2017-06-04",
  username = "06ea1287-c7f8-4a49-82fc-c9b94a5fc9cb",
  password = "YbRJ7tY5esig"
)

comment = "For the one trillionth time, THIS is the end of Donald DRUMPF. Also, please raise your right hand if you are literally shaking right now."
result = tone_analyzer.tone(text = comment)
#print(json.dumps(result, indent = 2))
#print(result.items())

anger = result["document_tone"]["tone_categories"][0]["tones"][0]["score"]
disgust = result["document_tone"]["tone_categories"][0]["tones"][1]["score"]
fear = result["document_tone"]["tone_categories"][0]["tones"][2]["score"]
joy = result["document_tone"]["tone_categories"][0]["tones"][3]["score"]
sadness = result["document_tone"]["tone_categories"][0]["tones"][4]["score"]

print(comment)
print("anger score: "+str(anger))
print("disgust score: "+str(disgust))
print("fear score: "+str(fear))
print("joy score: "+str(joy))
print("sadness score: "+str(sadness))

#print(json.dumps(tone_analyzer.tone(text='Fuck this guy'), indent=2))

#print(tone_analyzer.tone(text="fuck you").items())
#print("anger score: "+str(tone_analyzer.tone(text="fuck you")["document_tone"]["tone_categories"][0]["tones"][0]["score"]))
#print("disgust score: "+str(tone_analyzer.tone(text="fuck you")["document_tone"]["tone_categories"][1]["tones"][0]["score"]))
#print("fear score: "+str(tone_analyzer.tone(text="fuck you")["document_tone"]["tone_categories"][0]["tones"][2]["score"]))
#print("joy score: "+str(tone_analyzer.tone(text="fuck you")["document_tone"]["tone_categories"][0]["tones"][3]["score"]))
#print("sadness score: "+str(tone_analyzer.tone(text="fuck you")["document_tone"]["tone_categories"][0]["tones"][4]["score"]))
'''
'''
dict = {'Fuck you':.999, 'Eat shit':.888, 'I hate you':.777, 'Get out!':.666, 'Go away!':.555}
sorted = sorted(dict, key = dict.get)
print(type(sorted))
sorted.reverse()
print(sorted)

for comment in dict:
    comment = comment.encode(encoding='utf_8', errors = 'strict')
    print(comment)

for comment in dict:
    comment = comment.replace('\n', ' ')
    #print(comment)
    comment = comment.encode('utf-8')
    #print(comment)
    comment = str(comment)
    #print(comment)
    comment = comment[2:len(comment)-1]
    print(comment)
'''
'''
sorted = sorted(scores, key = scores.get)
sorted.reverse()
print(sorted, file = out)
'''

'''
file = open('test.txt', 'w')
print('this is a test file', file = file)
'''
'''
import twitter
twitter = twitter.Api(consumer_key = '6LNKl5xPLUTLRJhiVTLFpsqpk',
                      consumer_secret  = 'R7uCotJ4G5lC8XP1Ncq1C8982mkxlq5hO11N5o7E9K8mOk8alX',
                      access_token_key = '872343913092325376-I7qdDATXj5A0bZbWR0IwaTJGwKVKhmw',
                      access_token_secret = 'zhKYBbmdBjohoBd5eq3ZGY2kO4YqOwbk3Bx7SXSDWu3k7')

twitter.PostUpdate('test update please ignore')
'''
import pandas as pn
import json
import matplotlib.pyplot as plt
import sys

print "Hello"
file_path = '/media/hishamsajid/Misc/Marketlytics/slack_data/slack.json'

#with open(file_path) as json_file:
#   json_data = json.load(json_file)

#print(json_data)

#pn.read_json()

logs = []
users = []
num_questions = []
num_emoji = []
time = []
message = []
channel = []
num_words = []
os = []

for line in open(file_path):
   log = json.loads(line)
   #print log.keys()
   #print log['event']
   #print log['properties']
   #log_data = log[0]
   #print log
   #print("___")
   #print log
   logs.append(log['properties'])
   users.append(log['properties']['user'])
   num_questions.append(log['properties']['num_questions'])
   num_emoji.append(log['properties']['num_emoji'])
   time.append(log['properties']['time'])
   message.append(log['properties']['message'])
   num_words.append(log['properties']['num_words'])
   channel.append(log['properties']['channel'])
   os.append(log['properties']['os'])

   #pn.DataFrame.from_dict(log['properties'])

#print logs
#print users
#print num_questions
#print num_emoji
#print time
#print message
#print num_words
#print channel

logs_dict = {'users':users,'message':message,'time':time,'channel':channel,
'num_words':num_words, 'num_emoji':num_emoji,'num_questions':num_questions,
'os':os}

logs_df = pn.DataFrame.from_dict(logs_dict)

print "hello world"

#logs_df.to_csv('logs.csv')
print logs_df.describe()
rslt = logs_df['channel'].value_counts()
rslt = logs_df['os'].value_counts()
print rslt

#rslt.columns = ['channel', 'frequency']
#rslt_1 = pn.DataFrame(rslt.values, columns {'channel','frequency'})


#slt.to_csv('frequent.csv')

#result2 = pn.read_csv('frequent.csv',names = ['channel', 'frequency'])
#print result2
#print result2.plot.bar()
#print rslt
#print rslt

#plt.plot(result2['channel'], result2['frequency'], color='green', marker='o', linestyle='solid')

    # add a title
#plt.title("Channels most used")

    # add a label to the y-axis
    #plt.ylabel("Billions of $")
#plt.show()


#plt.style.use('ggplot')
#plt.ylabel('Frequency')
#plt.xlabel('Channel')
#result2.plot.bar(x = 'channel', y = 'frequency' ,rot =0)
#plt.show()
#print num_questions

#print logs_df

import csv
# read csv file as a list of lists
with open('hacker_news.csv', 'r') as file:
    # pass the file object to reader() to get the reader object
    readFile = csv.reader(file)
    # Pass reader object to list() to get a list of lists
    hn = list(readFile)
    for i in hn[:6]:
        print()
        print(i)
        
     
     #  ´´´´´´´´´´´´´´´´´OUTPUT´´´´´´´´´´´´´´´´´´´´
['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at']

['12224879', 'Interactive Dynamic Video', 'http://www.interactivedynamicvideo.com/', '386', '52', 'ne0phyte', '8/4/2016 11:52']

['10975351', 'How to Use Open Source and Shut the Fuck Up at the Same Time', 'http://hueniverse.com/2016/01/26/how-to-use-open-source-and-shut-the-fuck-up-at-the-same-time/', '39', '10', 'josep2', '1/26/2016 19:30']

['11964716', "Florida DJs May Face Felony for April Fools' Water Joke", 'http://www.thewire.com/entertainment/2013/04/florida-djs-april-fools-water-joke/63798/', '2', '1', 'vezycash', '6/23/2016 22:20']

['11919867', 'Technology ventures: From Idea to Enterprise', 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429', '3', '1', 'hswarna', '6/17/2016 0:01']

['10301696', 'Note by Note: The Making of Steinway L1037 (2007)', 'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0', '8', '2', 'walterbell', '9/30/2015 4:12']
#Slice out headers row
headers=hn[0]
#Remove headers row from the datasest
hn=hn[1:]
print("HEADER COLUMNS")
print()
print(headers)
print()
print("5 rows of DATA")
print()
print(hn[:6])

ask_posts=[]
show_posts=[]
other_posts=[]
for row in hn:
    title=row[1]
    if(title.lower().startswith('ask hn') ):
        ask_posts.append(row)
    elif(title.lower().startswith('show hn')):
        show_posts.append(row)
    else:
        other_posts.append(row)
print('ASK POSTS TITLE COUNT ' +str(len(ask_posts)))
print('SHOW POSTS TITLE COUNT ' +str(len(show_posts)))
print('OTHER POSTS TITLE COUNT ' +str(len(other_posts)))

#output
ASK POSTS TITLE COUNT 1744
SHOW POSTS TITLE COUNT 1162
OTHER POSTS TITLE COUNT 17194

#we will find average number of posts with ask_posts title
tot_ask_comm = 0

for post in ask_posts:
    tot_ask_comm += int(post[4])
avg_ask_comm = tot_ask_comm/len(ask_posts)
print(avg_ask_comm)
#ouput
14.038417431192661

#we will find average number of posts with show_posts title
tot_show_comm = 0

for post in show_posts:
    tot_show_comm += int(post[4])
avg_show_comm = tot_show_comm/len(show_posts)
print(avg_show_comm)
10.31669535283993

#We will now try to determine if ask posts created at a certain time are receiving more comments.
import datetime as dt

#we will extract from the posts, the time the post was creaated and the num of comments for that post

result = []
print(ask_posts[0])

for post in ask_posts:
   result.append([post[6], int(post[4])])
print()
#print(result[:10])
counts_by_hour = {}
comments_by_hour = {}
format="%m/%d/%Y %H:%M" 
for item in result:
    hour=item[0]
    num_of_comments=item[1]
    time=dt.datetime.strptime(hour, "%m/%d/%Y %H:%M").strftime("%H")
    if time not in counts_by_hour:
        counts_by_hour[time] =1
        comments_by_hour[time] = int(num_of_comments)
    else:
        counts_by_hour[time]+=1
        comments_by_hour[time]+=int(num_of_comments)
print(counts_by_hour)
print(comments_by_hour)
    
#calculate the average num of psots
avg_by_hour = []

for hour in counts_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])
    
for post in avg_by_hour:
    print(post)
    
 #Finalizing results to a statement
swap_avg_by_hour= []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
for r in swap_avg_by_hour:
    print(r)
sorted_swap = sorted(swap_avg_by_hour, reverse=False)
print("Top 5 Hours for Ask Posts Comments")
for avg,hour in sorted_swap[:5]:
    time = dt.datetime.strptime(hour, "%H")
    req = time.strftime("%H:%M")
    print("At {} {:.2f} posts per day".format(req, avg))

    
 #output
[6.746478873239437, '22']
[7.985294117647059, '23']
[16.009174311926607, '21']
[13.440677966101696, '10']
[38.5948275862069, '15']
[13.20183486238532, '18']
[11.051724137931034, '11']
[8.127272727272727, '00']
[13.233644859813085, '14']
[9.022727272727273, '06']
[5.5777777777777775, '09']
[16.796296296296298, '16']
[10.08695652173913, '05']
[21.525, '20']
[7.796296296296297, '03']
[9.41095890410959, '12']
[7.170212765957447, '04']
[10.25, '08']
[11.383333333333333, '01']
[11.46, '17']
[7.852941176470588, '07']
[14.741176470588234, '13']
[10.8, '19']
[23.810344827586206, '02']
Top 5 Hours for Ask Posts Comments
At 09:00 5.58 posts per day
At 22:00 6.75 posts per day
At 04:00 7.17 posts per day
At 03:00 7.80 posts per day
At 07:00 7.85 posts per day

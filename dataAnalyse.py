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

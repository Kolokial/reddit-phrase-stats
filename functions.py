import praw
import json
import os
import re
from database_functions import *

file = open(os.path.dirname(os.path.abspath(__file__))+'/.credentials.remote.json')
credentials = json.load(file)

reddit = praw.Reddit(
    user_agent="PhraseStatsBot (by u/koloqial)",
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    username=credentials['username'],
    password=credentials['password']
)

subsList = [
    'askreddit',
    'outoftheloop'
    #"testingground4bots"
]

regexPatterns = [
    
]

regexPattern = re.compile(r'^(this is the way|this\^?|same|and my axe!?).?', re.MULTILINE)
submissions = reddit.subreddit("+".join(subsList))
results = list(get_posts_read_list())
readPosts = [r[0] for r in results]

def doesCommentMatchRegex(comment):
    if(regexPattern.search(comment.body.lower()) is not None):
        print("-----------------------------------")
        print("Comment written by :", comment.author)
        print("replies:", comment.replies.__len__())
        print("comment:", comment.body)
        print("Id:", comment.id)
    
    if(comment.replies.__len__()):
        for comment in comment.replies:
            doesCommentMatchRegex(comment)



print(readPosts)

for submission in submissions.new(limit=500):

    post = reddit.submission(submission.id)

    post.comments.replace_more(limit=None, threshold=0)
    #print(post.num_comments)
    if post.num_comments == 0 or post.stickied == True or readPosts.count(post.id) > 0:
        continue
    print("Looking in post: '", post.title)
    print("Number of comments: ", post.num_comments)
    print("Post Id: ",post.id)
    insert_into_post_read_table(post.id)
    for comment in post.comments:
        doesCommentMatchRegex(comment)
        # print("---------------------------------\n")
        # print("Comment written by :", comment.author)
        # print("replies:", comment.replies.__len__())
        # print("comment:", comment.body)
        # print("Id:", comment.id)
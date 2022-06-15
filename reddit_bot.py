import praw
import config
import time
import os
import requests

def bot_login():
    print("Logging in")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "BouncyK test v0.2"
            )
    print("Logged in")

    return r

def run_bot(r, comments_replied_to):
    print("Obtaing 5 comments")

    for comment in r.subreddit('ChuckNorrisJokes').comments(limit=5) :
        if "Chuck" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with joke found!")
            
            
            comment_reply = "You requested a Chuck Noris joke. Here it is:\n\n"

            joke = requests.get("http://api.icndb.com/jokes/random").json()['value']['joke']

            comment_reply += ">" + joke

            comment_reply += "\n\n This joke came from [ICNDb.com](http://api.icndb.com)"

            print("Replied to comment")

            comment.reply(body=comment_reply)
            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt","a") as f:
                f.write(comment.id + "\n")

    print("Sleeping for 5 minutes")
    # Sleeping for 5 minutes
    time.sleep(300)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = [] 
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()

while True: 
    run_bot(r, comments_replied_to)
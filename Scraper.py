#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import textwrap

reddit = praw.Reddit(client_id='b3r_DlEERM-ZjA', \
                     client_secret='SG7KKIVl3Z12CMeTsCqObZn7hqM', \
                     user_agent='UBC Scraper', \
                     username='ubcscraper', \
                     password='6047908866')



def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

while True:
    
    print("Hi! Please type in the course information you'd like to search about on Reddit.\n")
    print("Include spaces for the best results.")
    coursename = input()


    print("Reddit information on the course is as follows..\n\n\n\n\n")

    subreddit = reddit.subreddit("ubc")

    postcount = 1
    for submission in subreddit.search(coursename):
        print ("Reddit posting: " + str(postcount)+ "\n")
        postcount +=1
        text1 = textwrap.dedent(BMP(submission.selftext)).strip()
        print (textwrap.fill(text1, initial_indent='    ', subsequent_indent='    '))
        print ("\n")
        commentcount = 0
        for comment in submission.comments:
                commentcount +=1
                print("   comment " + str(commentcount))
                text2 = textwrap.dedent(BMP(comment.body)).strip()
                print (textwrap.fill(text2, initial_indent='        ', subsequent_indent='       '))
                print ("\n")
                commentforest = comment.replies
                commentforest.replace_more()
                for reply in commentforest.list():
                    commentcount +=1
                    print("   comment" + str(commentcount))

                    text3 = textwrap.dedent(BMP(reply.body)).strip()
                    print (textwrap.fill(text3, initial_indent='        ', subsequent_indent='        '))
                    print("\n")


CS1022/CS5222 2019-2020
(Lab) Assignment - Dictionaries 2
Exercise - Twitter
Exercise - Twitter
Suppose we want to create a Python program to implement a (simulated) simplified version of Twitter.
A Tweet is a brief text message (max 280 characters) that can include zero or more hashtags (a hashtag
is a word starting with the hash character #) and zero or more usernames (a username is a word stating
with the "at" character @). A Tweet has always an author (a username) and a date.
For example, this is a Tweet:
author: @UCCCS
date: Jan 15
message: "We in CSIT @ucc are looking forward to participating in the Careers Fair @gairmtreoir
#Yooni . Wishing all organisers well with the event."
The program simulates the social media by presenting the following menu to the user:
1. Login
The program asks the user to login by entering their username (to keep things simple, there is no need to
enter any password)
2. Make a new Tweet
The program asks to enter the date and the text of the Tweet (including hashtags and usernames, if any).
3. Search Tweets by username
The program asks to enter a username and finds all the Tweets in which that username is cited in the text
of the Tweet.
4. Search Tweets by hashtags
The program asks to enter one or more hashtags and prints all the Tweets in which those hashtags are
cited in the text of the Tweet.
5. See all the Tweet made by the user
The program prints all Tweets, ordered by date
When the program starts, no Tweet is available.
You can use functions, lists and dictionaries to solve the problem.

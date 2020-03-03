from datetime import date
from time import sleep

def tweetBase():
	#init database of tweets
	tweet = {"author":"@PW9", "date":"Feb 26", "message":"Welcome to twatter, Big Shout Out to my main man @PW9 #IfYourNotFirstYourLast"}
	tweetBase = [tweet]
	#init user database
	users = ["pw9","guest","ZB42","Mauman","Derek"] #not case sensitive
	print("fetching users...")
	return tweetBase, users

#Prints menu and returns option

def clear():
	print("-")
	sleep(.2)
	#print('\x1bc')

def readDate():
	date1 = str(date.today())
	months = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
	return date1[-2:] , months[int(date1[-5:-3])]




def search_tweets(user, symbol):
	if symbol == "@":
		username = input("Enter a username to search by \n\t@")
		print("searching tweets by @{username}")
	elif symbol == "#":
		trend = input("Enter a trend to search for \n\t#")
		print("Searching for tweets with trend #{trend}")



# Log in user and returns username or ""
def login(users):
	clear()
	print(f"{users}")
	id = input("\nType * to QUIT\nUser names are not case sensitive\n\tLog in:\n\tEnter your user name\n\t@").lower()
	# if id != "*":
	if id in users:

		return id

	else:
		print("Error, invalid user name.")

	return ""

#Displays menu loops if option not in 1-4, returns option
def menu():
	clear()
	c = input("""
		* to Quit.
		Options:
	1. Make a new Tweet.
	2. Search for Tweets by user name. @
	3. Search for Tweets by trend. #
	4. Log out. <

		Enter a number

	""")
	return c

	##returns undefined
	# if c == "*":
	# 	return False
	# try:
	# 	c = int(c)
	# 	if 1 >= c >= 4:
	# 		return c
	# 		print(f"Choice {c}")
	# except:
	# 	print("Error, invalid command.")
	menu()

def print_tweet(tweet_list):
	print("\nprinting tweets...")
	
	#only works if tweetlist is list
	for tweet in tweet_list:
		print(f"""
		@{tweet["author"]}
			{tweet["date"]}

		{tweet["message"]}
		""")

def make_tweet(user, tweets):
	clear()
	print("""
	Let's make a tweet!
	""")
	message = input("Enter you tweet here!\n\t")
	tweet = {"author":user, "date":readDate(), "message":message}
	print(f"\nHere is your tweet")
	print_tweet(tweet)
	opt = input("\nAre you happy with this tweet?\n\tY or N\n\t")
	if opt == "Y":
		tweets.append(tweet)
		print(tweets)
	elif opt == "N":
		make_tweet(user, tweets)

#Start of the  programme
def start_twatter():
	tweets, users = tweetBase()
	user = login(users)
	choice = int(menu())

	#main logic
	if choice == 1:
		tweet = make_tweet(user, tweets)
		#add way to display tweet

	elif choice == 2:
		search_tweets(user, "@")

	elif choice == 3:
		search_tweets(user, "#")

	elif choice == 4:
		user = False

	print("Good Bye!")

	clear()
	#start_twatter()

start_twatter()

def split_message(toChangeMessage, chars):
	message = toChangeMessage
	#find amount of lines
	lines = len(message)//chars
	if (len(message) % chars) >= 0:
		print("hello")
		lines += 1

	#split message to list of words
	message = message.split(" ")
	#make list of empty strings equal to amount of lines needed
	messLines = []
	for n in range(lines):
		messLines.append("")
		stop =  False
		while len(messLines[n]) < chars and not stop:
			for word in message:
				print(len(messLines[n]))
				#add words in message to messLines while they fit#
				#stalls at 22
				print(word)
				if len(messLines[n] + word)+1 < chars:
					messLines[n] += " " + word
					if len(message) > 1:
						print(f"popping {message[0]}")
						message.pop(0)

					else:
						message = []
				else:
					stop = True

	for line in messLines:
		print(line)
	# count = 0
	# word_count = 0
	#
	# for :
	# 	for word in message:
	# 		if len(messLines[count]) < chars:
	# 			messLines[count] += " "+word
	# 			print(f"removing {message[count]}")
	# 			message.pop(count)
	#
	# 			print(message)
	# 		print(f"word is {word}")
	# 		count +1
	# return messLines

split_message("Welcome to twatter, Big Shout Out to my main man @RickyBobby #IfYourNotFirstYourLast",25)



#
# def print_tweet(tweet_list):
# 	print("\nprinting tweets...")
#
# 	#only works if tweetlist is list
# 	for tweet in tweet_list:
# 		print(tweet)
#
# 		print(f"""
# 		{tweet["author"]}	-{tweet["date"]}
# 		""")
# 		message = tweet["message"]
# 		if len(message) > 10:
# 			message = split_message(message)
#

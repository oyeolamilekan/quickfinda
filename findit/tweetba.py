# import tweepy
# import threading
# import random
# def tweetbot():
# 	account_pickers = ['@iam_Davido','@wizkidayo','@justinbieber','@official2baba','@DONJAZZY','@lilkeshofficial','@olamide_YBNL']
# 	print(account_pickers)
# 	consumer_key = 'tiCC7e25VH5UtUccfEc2d8yOE'
# 	consumer_secret = 'n1jgPEOQI9ZCIAzEvlez11EoFHt3fmNR1hYhst0P7pUN3l8hg3'
# 	access_token = '875746526659842048-VBrsA9etYRtpKFU8Zkb9WiePXDIVZ7Z'
# 	access_token_secret = 'giBb6fUwbOvP83QSHFfiyWLBbq6bMpmyFSxZDoNAycfXe'

# 	# Set up OAuth and integrate with API
# 	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_token_secret)
# 	api = tweepy.API(auth)
# 	for i in range(15):
# 		random.shuffle(account_pickers)
# 		api.update_status(status='use quickfinda.com to compare prices from different stores %s %s %s'%(random.choice(account_pickers),random.choice(account_pickers),random.choice(account_pickers)))

# 	threading.Timer(3600.0,tweetbot).start()
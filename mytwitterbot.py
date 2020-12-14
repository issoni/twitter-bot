import sys
import time
import simple_twit
from datetime import date, datetime 

def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    simple_twit.version()
    
    # Project 04 Exercises
    
##    # Exercise 1 - Get and print 10 tweets from your home timeline
##    myTimeline = simple_twit.get_home_timeline(api, 10)
##    for tweet in myTimeline:
##        print(tweet.id)
##        print(type(tweet.user))
##        print(tweet.author.name)
##        print(tweet.user.name)
##        print(tweet.full_text)
##        print()
##    
##    # Exercise 2 - Get and print 10 tweets from another user's timeline
##    careBotTimeline = simple_twit.get_user_timeline(api,"tinycarebot", 10)
##    for tweet in careBotTimeline:
##        print(tweet.id)
##        print(type(tweet.user))
##        print(tweet.author.name)
##        print(tweet.user.name)
##        print(tweet.full_text)
##        print()
##    
##    # Exercise 3 - Post 1 tweet to your timeline.
##    myPost = simple_twit.send_tweet(api, "Exercise #3 on mytwitterbot.py (third run)")
##    print(type(myPost))
##    
##    # Exercise 4 - Post 1 media tweet to your timeline.
##    myMediaPost = simple_twit.send_media_tweet(api, "Exercise #4 on mytwitterbot.py", "cat.jpg")
##    print(type(myMediaPost))
    
    
    # YOUR BOT CODE BEGINS HERE
    



    while True:
        
        year = datetime.now()
        currentYear = year.year

        today = date.today()
        d = today.strftime("%B %d, %Y")
    
        present = datetime.now()
        future = datetime(currentYear, 1, 1, 12, 0, 0)
        difference = present - future 
        newDifference = 366 - difference.days
        
        
        tweet = "Today is " + str(d) + "."
        tweet2 = "Days left till " + str(currentYear + 1) + ": " + str(newDifference)

        if newDifference == 0:
            finalTweet = "HAPPY NEW YEAR!"
        else:
            finalTweet = tweet+ "\n"+ tweet2

        print(finalTweet)

        myPost = simple_twit.send_tweet(api, finalTweet)
        print(type(myPost))
        time.sleep(86400)
        
        



    
    
# end def main()

if __name__ == "__main__":
       main()


import re
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

track = "Your search terms"
pattern = re.compile('The exact pattern you want matched in tweets you RT')

tweets_in_a_row = 3
wait = 600
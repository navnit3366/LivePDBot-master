import praw, users
from praw.models import Message

#reddit instance setup
reddit = praw.Reddit(client_id=users.client_id,
                     client_secret=users.client_secret,
                     user_agent=users.user_agent,
                     username=users.username,
                     password=users.password)

messages = []
while True:
    for message in reddit.inbox.stream():
        this = reddit.inbox.message(message)
        print("\nNEW REDDIT MESSAGE FROM {}:".format(this.author))
        print("> {} <".format(this.subject))
        print(this.body)
        
        if isinstance(message, Message):
            reddit.inbox.message(message).reply(
                "This account is not monitored.  Contact /u/Me on Reddit or Me#1234 on Discord @ link.")
            messages.append(message)
        else:
            pass
    reddit.inbox.mark_read(messages)

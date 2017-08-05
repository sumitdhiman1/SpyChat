from datetime import datetime

class Spy():

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage():

    def __init__(self, message, sent_by_me):
       self.message = message
       self.time = datetime.now()
       self.sent_by_me = sent_by_me



spy = Spy('Sumit', 'Mr.', 21, 5.0)

friend_one = Spy('Sahil', 'Mr.', 4.6, 21)
friend_two = Spy('Sandeep', 'Mr.', 4.35, 21)
friend_three = Spy('Arjun', 'Mr..', 4.32, 21)

FRIENDS = [friend_one, friend_two, friend_three]







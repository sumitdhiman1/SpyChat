from spy_details import spy, Spy, ChatMessage, FRIENDS

from steganography.steganography import Steganography

import datetime

#starting a spychat project

spy_status="what,s up doc?"

STATUS_MESSAGES = ["what,s up doc?", "busy. ", "Available ."]

print "Let's get started"

# String Concatenation using + symbol

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "

existing = raw_input(question)

#function for updating a status

def add_status(current_status_message):

    if current_status_message != None:
        print "Your current status message is" + current_status_message
    else:
        print "You dont have any status message currently"

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    if default.upper() == "Y":
        print "What status message do you want to choose? "
        item_position = 1
        for e in STATUS_MESSAGES:
            print str(item_position) +". " + e
            item_position = item_position + 1

        status_choice = raw_input("What do you want to set? ")
        if int(status_choice) > len(STATUS_MESSAGES):
            print "BUZZZZZ!"

        if len(STATUS_MESSAGES) >= int(status_choice):
            updated_status_message = STATUS_MESSAGES[int(status_choice) - 1]
            print "Your status message is: %s" % (updated_status_message)
            return updated_status_message

#function for adding a new friend

def add_friend():

    new_friend = Spy('', '', 0, 0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    # String Concatenation using + symbol
    # Variable has been updated

    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        FRIENDS.append(new_friend)
        print "Friend Added"
    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"
    return len(FRIENDS)

#function for selecting a friend

def select_a_friend():

    item_position = 1
    for friend in FRIENDS:
        print '%d. %s aged %d with rating %.2f is online' % (item_position , friend.name, friend.age, friend.rating)
        item_position = item_position + 1

    friend = raw_input("Choose a friends from the above list")
    friend = int(friend)
    return friend - 1

#function for sending a secret message

def send_message():

    friend = select_a_friend()

    original_image = raw_input("What is the name of the image?")

    output_path = "C:\Users\com\Desktop\secret\output.jpg"

    text = raw_input("What do you want to say? ")

    new_chat = ChatMessage(text, True)

    Steganography.encode(original_image, output_path, text)

    FRIENDS[friend].chats.append(new_chat)


def get_now():

    return datetime.datetime.now()

#function for reading a secret message

def read_message():

    sender = select_a_friend()

    secret_text = Steganography.decode("C:\Users\com\Desktop\secret\output.jpg")

    new_chat = ChatMessage(secret_text, False)

    FRIENDS[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

#function for reading a chat history

def read_chat_history():

   read_for = select_a_friend()

   for chat in FRIENDS[read_for].chats:

       if chat.sent_by_me:

           print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)

       else:

           print "[%s] %s said: %s" % (chat.time.strftime("%d %B %Y"), FRIENDS[read_for].name, chat.message)


#function for starting a chat
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        # String Concatenation using + symbol

        print "Authentication complete. Welcome " + spy.name + " age: "  + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:

           menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"

           menu_choice = raw_input(menu_choices)

           # Nested if

           if len(menu_choice) > 0:

               menu_choice = int(menu_choice)

               if menu_choice == 1:
                   spy.current_status_message = add_status(spy_status)
               elif menu_choice == 2:
                   number_of_friends = add_friend()
                   print 'You have %d friends' % (number_of_friends)
               elif menu_choice == 3:
                   send_message()
               elif menu_choice == 4:
                   read_message()
               elif menu_choice == 5:
                    read_chat_history()
               else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

#condition for continue with the default user or create their own.

if existing.upper() == "Y":

    start_chat(spy)

else:

    spy = Spy('', '', 0, 0.0)

#Ask the user for spy name

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:

        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")

        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")

        spy.rating = float(spy.rating)

        start_chat(spy)

    else:

        print 'Please add a valid spy name'







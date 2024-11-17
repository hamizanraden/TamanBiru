from chat.message import message

def reply_message(reply):
    if reply :
        message.append(reply)
        print("Message replied")
    else:
        print("No message to reply")

def display_reply():
    if message:
        for i, reply in enumerate(message, 1):
            print (f"Reply {i}: {reply}")
    else:
        print("No messages to display")

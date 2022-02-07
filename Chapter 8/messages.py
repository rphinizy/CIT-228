
messages=["Good Morning","Good Eveneing", "Good Night","Have a Great Day"]
sent_messages=[]

def show_messages(messages):
    for message in messages:
        msg=f"Message says: {message.title()}"
        print(msg)

def send_messages(message):
      for message in messages:
        msg=f"Sending Message: {message.title()}"
        print(msg)
        sent_messages.append(message)

print("*****AVAILABLE MESSAGES*********")
show_messages(messages)
print("********************************\n")
print("*******SENDING MESSAGES*********")
send_messages(messages)
print("********************************\n")
print("*************SENT***************")
for sent in sent_messages:
    print("SUCCESS!",sent)
print("********************************\n")
print("**********USE A COPY************")
send_messages(messages[:])
print("**********Messages List************")
print(messages)
print("**********Sent Messages List************")
print(sent_messages)


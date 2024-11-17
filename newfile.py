#A simple spam indicator using list

spam_messages = [
    "subscribe to us",
    "buy premium fast just at 199",
    "make money at home",
    "download quick",
    "click fast",
    "Buy this course"
]

Message = input ("Ennter your message ").lower()
is_a_spam =any(spam in Message for spam in spam_messages)

if is_a_spam:
  print("warning : the message is spam")
else:
  print("All good")


#A simple spam filter using saperate strings

sm1= "subscribe to us"
sm2= "buy premium fast just at 199"
sm3= "make money at home "
sm4= " download quick"
sm5= "click fast"
sm6 = "buy this course "


ALLMessages = input("Enter the message ").lower()

if (sm1 in ALLMessages) or (sm2 in ALLMessages) or (sm3 in ALLMessages) or (sm4  in ALLMessages) or (sm5 in ALLMessages)or (sm6 in ALLMessages) :
  print("Warning : The Message is spam ")
else :
  print ("All clear")






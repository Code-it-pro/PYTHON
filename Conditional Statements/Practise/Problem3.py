p1 = "Make a lot of money" 
p2 = "Buy now"
p3 = "subscribe now"
p4 = "click here"

message = input("Enter the message: ")

if p1 in message or p2 in message or p3 in message or p4 in message:
    print("This is a spam message.")
else:    print("This is not a spam message.")
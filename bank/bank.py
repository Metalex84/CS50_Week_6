reply = input("Greeting: ")

if reply.lower().strip().startswith("hello", 0):
    print("$0")
elif reply[0].lower() == "h":
    print("$20")
else:
    print("$100")

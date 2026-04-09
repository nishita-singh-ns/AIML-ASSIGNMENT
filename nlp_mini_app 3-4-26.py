print("Chatbot Started (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")
    elif user == "how are you":
        print("Bot: I'm fine! 😊")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I didn't understand that.")
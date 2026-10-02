# Rule-Based Chatbot
# This chatbot responds to users using predefined keywords and rules.

print("===================================")
print("      🤖 RULE-BASED CHATBOT")
print("===================================")
print("Bot: Hello! I am a simple chatbot.")
print("Bot: You can ask me simple questions.")
print("Bot: Type 'bye' to exit.\n")


# Keep the chatbot running until the user says "bye"
while True:

    # Get input from the user
    user_input = input("You: ")

    # Convert the input to lowercase
    # This allows "Hello", "HELLO", and "hello" to be treated similarly.
    user_input = user_input.lower()

    # Rule 1: Handle greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hi! Nice to meet you. How can I help you?")

    # Rule 2: Respond to "how are you"
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    # Rule 3: Tell the chatbot's name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a Rule-Based Chatbot.")

    # Rule 4: Explain what the chatbot can do
    elif "what can you do" in user_input:
        print("Bot: I can respond to greetings and some simple questions.")

    # Rule 5: Respond to thanks
    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")

    # Rule 6: Exit the chatbot
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    # Fallback response when no rule matches
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
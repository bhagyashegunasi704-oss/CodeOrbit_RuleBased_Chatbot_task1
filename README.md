# Rule-Based Chatbot

## Project Overview

This project is a simple **Rule-Based Chatbot** developed using Python. The chatbot interacts with the user through the terminal and responds to user messages based on predefined keywords and rules.

The chatbot uses basic `if-elif-else` conditional logic to identify the user's input and provide an appropriate response.

## Objective

The main objective of this project is to understand the basic working of a rule-based chatbot, including:

* Taking input from the user
* Processing user input
* Identifying predefined keywords
* Providing appropriate responses
* Handling unknown inputs with a fallback response
* Maintaining a continuous conversation until the user exits

## Technologies Used

* **Programming Language:** Python
* **Concepts:**

  * Variables
  * User Input
  * Strings
  * Conditional Statements (`if`, `elif`, `else`)
  * Loops
  * Keyword Matching
  * Comments

## Features

### 1. Greeting Recognition

The chatbot responds to common greetings such as:

* Hello
* Hi
* Hey

### 2. Common Questions

The chatbot can respond to simple questions such as:

* How are you?
* What is your name?
* Who are you?
* What can you do?

### 3. Thank You Response

The chatbot recognizes expressions such as:

* Thank you
* Thanks

and responds appropriately.

### 4. Fallback Response

If the chatbot does not recognize the user's input, it provides a default response instead of remaining silent.

Example:

```text
You: What is machine learning?
Bot: Sorry, I don't understand that. Please try another question.
```

### 5. Exit Option

The user can end the conversation by entering:

* Bye
* Exit

## How It Works

The chatbot follows these basic steps:

```text
User enters a message
        ↓
Convert the message to lowercase
        ↓
Check predefined rules and keywords
        ↓
Find a matching rule
        ↓
Generate the appropriate response
        ↓
Continue the conversation
```

If no rule matches the user's input, the chatbot provides a fallback response.

## Example Interaction

```text
===================================
      🤖 RULE-BASED CHATBOT
===================================

Bot: Hello! I am a simple chatbot.
Bot: You can ask me simple questions.
Bot: Type 'bye' to exit.

You: hello
Bot: Hi! Nice to meet you. How can I help you?

You: how are you?
Bot: I'm doing great! Thanks for asking.

You: what is your name?
Bot: I am a Rule-Based Chatbot.

You: what can you do?
Bot: I can respond to greetings and some simple questions.

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a nice day.
```

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Open the Project

Open the project folder in Visual Studio Code or a terminal.

### Step 3: Run the Program

Open the terminal inside the project folder and run:

```bash
python chatbot.py
```

If `python` does not work, try:

```bash
py chatbot.py
```

### Step 4: Interact with the Chatbot

Enter messages in the terminal and the chatbot will respond according to its predefined rules.

## Project Structure

```text
CodeOrbit_Task_1_Rule_Based_Chatbot/
│
├── chatbot.py
├── README.md
└── output.png
```

## Limitations

This chatbot is rule-based and does not use machine learning or natural language processing models. It can only respond to inputs for which predefined rules have been created.

It does not learn from conversations or generate new responses dynamically.

## Conclusion

This project demonstrates the basic concept of a rule-based chatbot using Python. It provides a simple introduction to conversational programs and demonstrates how predefined rules and keyword matching can be used to process user input and generate responses.

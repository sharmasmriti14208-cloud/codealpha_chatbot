# Simple Rule-Based Chatbot

A beginner-friendly, interactive rule-based chatbot written in Python.

## Core Python Concepts Used

1. **Functions (`def`)**:
   - `get_response(user_input)`: Encapsulates the logic of matching user input against rules.
   - `start_chat()`: Encapsulates the interactive conversation flow.
2. **Conditional Statements (`if-elif-else`)**:
   - Evaluates user input against predefined phrases and handles unrecognized queries with a friendly fallback.
3. **Loops (`while True`)**:
   - Keeps the conversation going interactively until the user chooses to exit.
4. **Input and Output (`input()` / `print()`)**:
   - Interacts directly with the user via the console.
5. **String Methods (`.strip()`, `.lower()`, `.rstrip()`):**
   - Normalizes text so variations like `"Hello"`, `"HELLO!"`, or `"how are you?"` work smoothly.

---

## How to Run the Chatbot

Make sure you have Python installed, then run:

```bash
python chatbot.py
```

To run the unit tests:

```bash
python -m unittest test_chatbot.py
```

---

## Example Interaction

```text
=============================================
       Welcome to Simple Python Chatbot!      
=============================================
Chatbot: Hello! Type 'bye' at any time to exit.

You: hello
Chatbot: Hi!

You: how are you?
Chatbot: I'm fine, thanks!

You: help
Chatbot: You can say 'hello', ask 'how are you', ask 'what is your name', or type 'bye' to exit.

You: bye
Chatbot: Goodbye!

Chatbot has ended the conversation. Have a great day!
```

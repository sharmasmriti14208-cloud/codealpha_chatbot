"""
Simple Rule-Based Chatbot in Python
-----------------------------------
A beginner-friendly interactive chatbot using:
- Functions (def)
- Loops (while True)
- Conditional statements (if-elif-else)
- Input and Output (input, print)
"""


def get_response(user_input: str) -> str:
    """
    Takes the user's input, normalizes it, and returns
    a predefined response based on if-elif conditions.
    """
    # Clean the input: convert to lowercase, trim whitespace and trailing punctuation (? ! .)
    cleaned_input = user_input.strip().lower().rstrip("?!.")

    # Rule 1: Greetings
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi!"

    # Rule 2: Inquiring about well-being
    elif cleaned_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"

    # Rule 3: Chatbot's identity
    elif cleaned_input in ["what is your name", "who are you"]:
        return "I am a simple rule-based Python chatbot."

    # Rule 4: Help command
    elif cleaned_input in ["help", "what can you do"]:
        return "You can say 'hello', ask 'how are you', ask 'what is your name', or type 'bye' to exit."

    # Rule 5: Farewell / Exit
    elif cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"

    # Fallback for unrecognized inputs
    else:
        return "I'm sorry, I don't understand that. Type 'help' for things you can ask me!"


def start_chat():
    """
    Main function to run the chatbot interaction loop.
    """
    print("=" * 45)
    print("       Welcome to Simple Python Chatbot!      ")
    print("=" * 45)
    print("Chatbot: Hello! Type 'bye' at any time to exit.\n")

    # Interactive conversation loop
    while True:
        # Prompt user for input
        user_message = input("You: ")

        # Skip empty inputs
        if not user_message.strip():
            print("Chatbot: Please type something so we can chat!\n")
            continue

        # Get response using our rule-based function
        bot_response = get_response(user_message)

        # Output the chatbot's response
        print(f"Chatbot: {bot_response}\n")

        # Check for exit condition
        cleaned_msg = user_message.strip().lower().rstrip("?!.")
        if cleaned_msg in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot has ended the conversation. Have a great day!")
            break


if __name__ == "__main__":
    start_chat()

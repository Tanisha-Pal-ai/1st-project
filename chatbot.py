import random

# Define a function that handles the bot's responses
def respond(message):
    # Dictionary of possible responses
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you?": "I'm good, thank you!",
        "default": "Sorry, I don't understand. Can you please rephrase?",
    }
    
    # Convert the message to lowercase
    message = message.lower()
    
    # Check if the message is in the responses dictionary
    if message in responses:
        return responses[message]
    else:
        return responses["default"]

# Main function to run the chatbot
def main():
    print("Welcome to the chatbot!")
    print("You can start chatting with the bot. Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        
        # Check if the user wants to exit
        if user_message.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        
        # Get the bot's response
        bot_response = respond(user_message)
        print("Bot:", bot_response)

# Run the main function
if __name__ == "__main__":
    main()

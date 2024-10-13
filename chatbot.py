from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Train the chatbot with the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Function to get response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Chatbot interface
def chatbot_interface():
    print("Welcome to SimpleBot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("SimpleBot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"SimpleBot: {response}")


chatbot_interface()

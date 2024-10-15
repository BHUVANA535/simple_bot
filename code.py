class SimpleChatbot:
    def __init__(self):
        self.context = {}
    
    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"
    
    def farewell(self):
        return "Goodbye! Feel free to chat with me again anytime."
    
    def respond_to_question(self, question):
        if "name" in question.lower():
            return "I'm just a chatbot, so I don't have a name. What can I help you with?"
        elif "how are you" in question.lower():
            return "I'm just a computer program, so I don't have feelings, but thanks for asking!"
        elif "weather" in question.lower():
            return "I'm sorry, I don't have real-time information. You might want to check a weather website."
        elif "programming" in question.lower():
            return "I'm knowledgeable about programming. What specific information are you looking for?"
        elif "thanks" in question.lower():
            return "You're welcome! If you have more questions, feel free to ask."
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"
    
    def ask_user_questions(self):
        questions = ["What's your name?", "How can I assist you today?", "Tell me something about yourself."]
        for question in questions:
            user_response = input(question + " ")
            self.context[question] = user_response
    
    def chat(self):
        print(self.greet())
        self.ask_user_questions()
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print(self.farewell())
                break
            else:
                response = self.respond_to_question(user_input)
                print("Bot:", response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()

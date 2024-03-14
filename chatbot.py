import random

# Dictionary of responses
responses = {
    "admissions": "For admissions-related queries, please visit the official website of IIT Bhilai or contact the admissions office.",
    "courses": "IIT Bhilai offers undergraduate, postgraduate, and doctoral programs in various fields such as engineering, science, and humanities. You can find detailed information about each program on the official website of IIT Bhilai.",
    "facilities": "The campus of IIT Bhilai provides state-of-the-art facilities including academic buildings, laboratories, hostels, sports facilities, and more.",
    "placements": "IIT Bhilai has a dedicated placement cell that facilitates the placement process for students. For detailed information, you can visit the official website or contact the placement cell directly.",
    "campus_life": "IIT Bhilai offers a vibrant campus life with various clubs, societies, cultural events, and sports activities to engage students outside of academics.",
    "contact": "You can contact IIT Bhilai through their official website or directly reach out to their administration office for any queries or assistance.",
    "greetings": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Nice to meet you!"],
     "farewells": ["Goodbye!", "Farewell!", "See you later!", "Take care!"],
    "default": "I'm sorry, I couldn't understand that. Could you please rephrase your query?"
}

# Function to handle queries
def respond_to_query(query):
    query = query.lower()
    for key in responses:
        if key in query:
            return responses[key]
    return responses["default"]

# Main loop
print("Welcome to IIT Bhilai Chatbot!")
print("Ask me anything about IIT Bhilai.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = respond_to_query(user_input)
    print("Bot:", response)

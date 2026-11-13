responses = {
    "hello": "Hello! Nice to hear from you.",
    "hi": "Hey! How are you?",
    "good morning": "Good morning! How can i help?"
}

def get_response(message):
    message = message.lower()
    words = message.split()
    for keyword in responses:
        if keyword in words:
            return responses.get(keyword)
    return "I'm still learning. Can you tell me more?"
print(get_response("good morning"))
print(get_response("How are you?"))
print(get_response("hello echo"))
print(get_response("hello, good morning"))
print(get_response("this is a history lesson"))
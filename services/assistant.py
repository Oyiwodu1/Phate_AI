def get_response(message):
    message = message.lower()
    if message == "hello" or message == "hi":
        return "Hello! Nice to hear from you."
    else:
        return "I'm still learning. Can you tell me more?"
from little_functions import *

def handle_dialog(request, response, user_storage):
    output_message = "Hello, world."
    return message_return(response, user_storage, output_message)

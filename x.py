import requests
import json
 
# DeepSeek API key
api_key = "api"
 
# Base URL of the DeepSeek API
base_url = "https://api.deepseek.com/v1/chat/completions"
 
# API endpoint for chat completions
endpoint = "/chat/completions"
 
# Headers with the API key for authorization
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
 
def get_assistant_response(messages):
    """
    Send a request to the DeepSeek API and get the assistant's response.
    """
    # Data to send to the API in JSON format
    data = {
        "model": "deepseek-coder",
        "messages": messages
    }
 
    # Make a POST request to the API
    response = requests.post(base_url + endpoint, headers=headers, json=data)
 
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        response_data = response.json()
        # Extract the assistant's response from the JSON
        if 'choices' in response_data and response_data['choices']:
            assistant_response = response_data['choices'][0]['message']['content']
            return assistant_response
        else:
            print("No valid response received from the API.")
            return None
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
 
def main():
    # Start the conversation with a system message
    system_message = {"role": "system", "content": "You are a helpful assistant."}
    messages = [system_message]
 
    print("Welcome to the DeepSeek AI Assistant! Type 'quit' to end the conversation.")
 
    while True:
        # Get user input
        user_input = input("You: ")
 
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Conversation ended. Goodbye!")
            break
 
        # Add the user's message to the messages
        messages.append({"role": "user", "content": user_input})
 
        # Get the assistant's response
        assistant_response = get_assistant_response(messages)
        if assistant_response:
            # Print the assistant's response
            print(f"Assistant: {assistant_response}")
            # Update the system message if the assistant asks for assistance with a code snippet
            if assistant_response.lower().startswith("do you need help with a code"):
                system_message["content"] = "You are a helpful assistant specializing in coding."
            # Add the assistant's message to the messages
            messages.append({"role": "assistant", "content": assistant_response})
        else:
            print("Failed to get a response from the assistant.")
            break
 
if __name__ == "__main__":
    main()

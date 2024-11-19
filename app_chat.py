import streamlit as st
import openai

# OpenAI API key input
api_key = st.text_input("OpenAI API Key", type='password')

# Setting the OpenAI API key
if api_key:
    openai.api_key = api_key

# Initialize session state for tracking conversation
if "thread" not in st.session_state:
    st.session_state.thread = []  # This will store the conversation thread (messages)
    st.session_state.assistant = None  # This stores the assistant's unique ID (if any)

# Function to create a new assistant and thread
def create_new_assistant_and_thread():
    # Assuming the model is "gpt-3.5-turbo" or "gpt-4" (note that "gpt-4o-mini" isn't a real model)
    try:
        # Create a new assistant (a thread creation step)
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Adjust the model as necessary
            messages=[{"role": "system", "content": "You are a helpful assistant."}],
        )
        st.session_state.thread = [{"role": "system", "content": "You are a helpful assistant."}]
        st.session_state.assistant = response['id']
    except Exception as e:
        st.error(f"Error creating assistant: {e}")

# Function to send a message to the assistant and get a response
def get_response_from_assistant(message):
    try:
        # Add user message to the conversation thread
        st.session_state.thread.append({"role": "user", "content": message})
        
        # Send the conversation to the model
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the model you prefer
            messages=st.session_state.thread
        )
        
        # Get assistant's reply
        assistant_reply = response['choices'][0]['message']['content']
        
        # Add assistant's reply to the conversation thread
        st.session_state.thread.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    except Exception as e:
        return f"Error: {e}"

# Function to clear the conversation and create a new thread
def clear_conversation():
    st.session_state.thread = []
    st.session_state.assistant = None
    create_new_assistant_and_thread()

# UI for input and response
st.title("Chat with OpenAI Assistant")

# Display the conversation history
if st.session_state.thread:
    for msg in st.session_state.thread:
        if msg['role'] == 'user':
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Assistant:** {msg['content']}")

# Input field for user's message
user_message = st.text_input("Your Message:")

# Button for generating a response
if st.button("Send Message"):
    if user_message:
        if not st.session_state.assistant:
            create_new_assistant_and_thread()  # Ensure a new assistant is created when starting the conversation
        
        response = get_response_from_assistant(user_message)
        st.text_area("Assistant Response", value=response, height=150, max_chars=1000)
    else:
        st.warning("Please enter a message.")

# Button to clear the conversation
if st.button("Clear Conversation"):
    clear_conversation()
    st.success("New conversation started!")

# Button to exit the conversation (terminate assistant/thread)
if st.button("Exit Chat"):
    st.session_state.thread = []
    st.session_state.assistant = None
    st.success("Conversation ended.")

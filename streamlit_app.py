import streamlit as st
import openai

# Initialize OpenAI client
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set up Streamlit page
st.title("AI Assistant with Suggested Questions")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything:")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get AI response and suggestions in a single API call
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide a response and suggest 3 related follow-up questions."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        
        # Extract AI response and suggested questions
        ai_response = response.choices[0].message["content"]
        response_content, suggested_questions_block = ai_response.split("Suggested questions:") if "Suggested questions:" in ai_response else (ai_response, "")
        suggested_questions = [q.strip("- ").strip() for q in suggested_questions_block.strip().split("\n") if q.strip()]
        
        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(response_content.strip())
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content.strip()})
        
        # Display suggested questions as buttons
        if suggested_questions:
            st.write("Suggested follow-up questions:")
            for question in suggested_questions:
                if st.button(question):
                    st.session_state.messages.append({"role": "user", "content": question})
                    st.experimental_rerun()
    except Exception as e:
        st.error(f"Error generating response or suggestions: {e}")

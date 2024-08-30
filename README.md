 Emerge Tech Chatbot with Suggested Questions
A Streamlit app that demonstrates how to build a chatbot using OpenAI's GPT-3.5, with the added functionality of generating and displaying dynamic follow-up questions.



Features
Interactive Chatbot: Powered by OpenAI's GPT-3.5 model, capable of engaging in dynamic conversations.
Suggested Follow-Up Questions: The chatbot not only responds to user inputs but also suggests follow-up questions to continue the conversation seamlessly.
How to Run It on Your Own Machine
Install the Requirements

Make sure you have the necessary dependencies installed by running:

bash
Copy code
pip install -r requirements.txt
Run the App

Launch the Streamlit app using the following command:

bash
Copy code
streamlit run streamlit_app.py
Key Changes Implemented
Unified API Call: The chatbot now generates both the main response and suggested follow-up questions in a single API call to OpenAI's GPT-3.5 model. This ensures a smooth and immediate display of suggestions right after the assistant's response.

Enhanced User Interaction: Suggested questions are displayed as clickable buttons. When a button is clicked, the conversation continues with the selected question, and the app's state is refreshed to maintain a seamless user experience.

Error Handling: Improved error handling to catch and display any issues that may arise during API calls, ensuring that the app remains user-friendly even when encountering problems.

Example Workflow
User Input: The user enters a question in the chat input field.
AI Response: The chatbot generates a response using GPT-3.5.
Suggested Questions: Along with the response, the chatbot suggests related follow-up questions.
User Interaction: The user can either type a new question or click on one of the suggested questions to continue the conversation.

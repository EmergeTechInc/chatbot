Emerge Tech Chatbot with Suggested Questions and Graph Visualization
A Streamlit app that demonstrates how to build a chatbot using OpenAI's GPT-3.5, with added functionality for generating dynamic follow-up questions and visualizing chat interactions as a graph.

Features

Interactive Chatbot: Powered by OpenAI's GPT-3.5 model, capable of engaging in dynamic conversations.

Suggested Follow-Up Questions: The chatbot suggests follow-up questions to continue the conversation seamlessly.

Graph Visualization: Displays the flow of conversation using D3.js, where nodes represent chat exchanges and edges represent the interaction path.

Key Changes Implemented
Unified API Call: The chatbot generates both the main response and suggested follow-up questions in a single API call to OpenAI's GPT-3.5 model, ensuring a smooth and immediate display of suggestions.
Enhanced User Interaction: Suggested questions are displayed as clickable buttons. When a button is clicked, the conversation continues with the selected question, and the app's state is refreshed.
Graph Visualization: The app visualizes the conversation flow in real-time using D3.js, making it easier to track how the conversation evolves.
Error Handling: Improved error handling to catch and display any issues that may arise during API calls, ensuring a user-friendly experience.

Workflow
User Input: The user enters a question in the chat input field.
AI Response: The chatbot generates a response using GPT-3.5.
Suggested Questions: Along with the response, the chatbot suggests related follow-up questions.
User Interaction: The user can either type a new question or click on one of the suggested questions to continue the conversation.
Visualization: The conversation flow is visualized in real-time, with nodes representing the chat exchanges and edges representing the interaction path.
How to Use the Graph Visualization
Nodes: Represent individual chat exchanges.
Edges: Show the flow of the conversation between user inputs and AI responses.
Interaction: The graph updates dynamically as the conversation progresses, offering a clear visual representation of the dialogue structure.

This README should effectively introduce users to the chatbot's features and guide them on how to run and use the app, including the new graph visualization feature.
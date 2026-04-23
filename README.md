# Learn-Worlds-render-backend

This repo serves as the backend for [Learn-Worlds-Chatbot-Development](https://github.com/GVSUProjectGrandPath/Learn-Worlds-Chatbot-Development). The repo is hosted on a Render free plan to which the [front end](https://github.com/GVSUProjectGrandPath/Learn-Worlds-Chatbot-Development) can make a POST request to the render endpoint and get an OpenAI LLM response. 

## main.py

This file handles the endpoint connection receiving and sending information. It keeps track of all of the chat history for the specific thread Id. 
- **receives:** the user's most recent message and the tool their using
- **returns:** LLM response given the whole chat context and the tool being used

## backend.py

This file formats all the information for the LLM and makes the call to the LLM with all the given context. It tells the LLM the following information:
- It's a financial literacy chatbot for Rep4FinLit
- To Format all messages in HTML (so that chatbot can make line breaks, bold text, etc.)
- (some formatting specifications)
- There is a tool system and when the user selects a tool your goal is to help lead them to the tool's goal
- (Only when a tool is selected) "help me {tool-name}" so for example the LLM may get "help me create-a-budget"
from flask import Flask, request, jsonify
import requests
import uuid

app = Flask(__name__)

# Configuration
OLLAMA_API_BASE = "http://localhost:11434/api"
MODEL_NAME = "my-assistant"  # Replace with your model name

# Store conversations
conversations = {}

@app.route('/chat/new', methods=['GET'])
def new_conversation():
    chat_id = str(uuid.uuid4())
    conversations[chat_id] = []
    return jsonify({"chat_id": chat_id})

@app.route('/chat/<chat_id>', methods=['POST'])
def chat(chat_id):
    # Check if conversation exists
    if chat_id not in conversations:
        return jsonify({"error": "Conversation not found"}), 404
    
    # Get the message from the request
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Get conversation history
    history = conversations[chat_id]
    
    # Format the context with history
    context_messages = []
    for entry in history:
        if entry["role"] == "user":
            context_messages.append(f"Human: {entry['content']}")
        else:
            context_messages.append(f"Assistant: {entry['content']}")
    
    # Add the current message
    full_prompt = "\n".join(context_messages)
    if full_prompt:
        full_prompt += f"\nHuman: {user_message}"
    else:
        full_prompt = user_message
    
    # Prepare the request for Ollama
    ollama_payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }
    
    # Send request to Ollama
    try:
        response = requests.post(
            f"{OLLAMA_API_BASE}/generate", 
            json=ollama_payload
        )
        response.raise_for_status()
        
        # Extract the response
        ollama_response = response.json()
        assistant_message = ollama_response.get('response', '')
        
        # Update conversation history
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": assistant_message})
        conversations[chat_id] = history
        
        return jsonify({
            "response": assistant_message
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with Ollama: {str(e)}"}), 500

@app.route('/chat/<chat_id>/history', methods=['GET'])
def get_history(chat_id):
    # Check if conversation exists
    if chat_id not in conversations:
        return jsonify({"error": "Conversation not found"}), 404
    
    return jsonify({"history": conversations[chat_id]})

@app.route('/chat/list', methods=['GET'])
def list_conversations():    
    return jsonify({"conversations": list(conversations.keys())})

@app.route('/chat/<chat_id>/delete', methods=['DELETE'])
def delete_conversation(chat_id):
    # Check if conversation exists
    if chat_id not in conversations:
        return jsonify({"error": "Conversation not found"}), 404
    
    # Delete the conversation
    del conversations[chat_id]
    return jsonify({"message": f"Conversation {chat_id} deleted successfully"})

@app.route('/chat', methods=['DELETE'])
def delete_conversations():
    # Check if there are any conversations to delete
    if not conversations:
        return jsonify({"error": "No conversations to delete"}), 404
    
    # Clear all conversations
    conversations.clear()
    return jsonify({"message": "All conversations deleted successfully"})

@app.route('/chat/<chat_id>/clear', methods=['POST'])
def clear_conversation(chat_id):
    # Check if conversation exists
    if chat_id not in conversations:
        return jsonify({"error": "Conversation not found"}), 404
    
    # Clear the conversation history
    conversations[chat_id] = []
    return jsonify({"message": f"Conversation {chat_id} cleared successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5099)
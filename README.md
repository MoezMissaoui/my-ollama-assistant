# My Assistant

A custom AI assistant built with Ollama, Python, and Flask that provides intelligent responses using local language models.

## Description

This project implements a custom AI assistant that leverages:
- Ollama for local language model inference
- Flask for the web API interface
- Python for backend processing

## Prerequisites

- Python 3.9 or higher
- Ollama installed and running locally
- Required Python packages:
  - Flask
  - requests
  - python-dotenv
  - urllib3

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/my-assistant.git
cd my-assistant
```

2. Create and activate a virtual environment
```bash
python -m venv myworld
# Windows
myworld\Scripts\activate
# Unix/MacOS
source myworld/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
Create a `.env` file with your configuration:
```env
OLLAMA_API_URL=http://localhost:11434
MODEL_NAME=your_model_name
```

## Usage

1. Start the Ollama server
```bash
ollama serve
```

2. Run the Flask application
```bash
flask run
```

## API Endpoints

- `POST /chat` - Send messages to the assistant
- `GET /models` - List available models
- `GET /health` - Check service health

## Project Structure

```
my-assistant/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── services/
├── tests/
├── .env
├── README.md
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Ollama](https://ollama.ai/) for the local LLM capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework
- All other open-source contributors

# Ollama Chat API

A Flask-based REST API wrapper for Ollama chat interactions.

## Configuration

- Default Port: 5099
- Ollama API Base: http://localhost:11434/api
- Model Name: my-assistant

## API Endpoints

### Create New Conversation
```http
GET /chat/new
```
Returns a new chat ID for starting a conversation.

### Send Message
```http
POST /chat/{chat_id}
```
Send a message to a specific conversation.

**Request Body:**
```json
{
    "message": "Your message here"
}
```

### Get Conversation History
```http
GET /chat/{chat_id}/history
```
Retrieves the complete history of a specific conversation.

### List All Conversations
```http
GET /chat/list
```
Returns a list of all active conversation IDs.

### Delete Specific Conversation
```http
DELETE /chat/{chat_id}/delete
```
Deletes a specific conversation by ID.

### Delete All Conversations
```http
DELETE /chat
```
Deletes all existing conversations.

### Clear Conversation History
```http
POST /chat/{chat_id}/clear
```
Clears the history of a specific conversation while maintaining the chat ID.

## Error Responses

The API may return the following error status codes:

- `400`: Bad Request - When no message is provided
- `404`: Not Found - When accessing a non-existent conversation
- `500`: Server Error - When there's an error communicating with Ollama

## Running the Server

To start the server:

```bash
python ollama_api.py
```

The server will run on `http://0.0.0.0:5099` by default.
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
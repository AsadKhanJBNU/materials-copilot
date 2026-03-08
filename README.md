# Materials Copilot

A simple chat-based web application powered by a Large Language Model (LLM). Ask about DFT setups, materials science, k-points, functionals, or any related topic. The UI includes topic shortcuts (DFT & Computation, Materials, General) and suggestion cards that fill the input.

## Architecture

```
┌─────────────┐     GET /         ┌─────────────┐     POST /api/prompt
│   Browser   │ ◄───────────────► │   Flask     │ ◄─────────────────────►  LLMInterface
│  (chat UI)  │                   │   app.py    │      prompt (string)        (Gemini)
└─────────────┘                   └──────┬─────┘      response (string)
                                         │
                                         ▼
                                  ┌──────────────┐
                                  │  Gemini API  │
                                  └──────────────┘
```

- **Frontend:** Single-page chat UI (`templates/index.html`) with sidebar topics, suggestion cards, and a message list. All messages go to `POST /api/prompt`.
- **Backend:** Flask app (`app.py`) serves the page and the prompt API. Uses `llm_interface.py` to call Google Gemini.

## Tools and stack

| Component   | Technology     |
|------------|----------------|
| Web server | Flask (Python) |
| LLM        | Google Gemini API |
| Frontend   | HTML, CSS, JS |

## Run the app

### 1. Install dependencies

```bash
cd materials-copilot
pip install -r requirements.txt
```

### 2. Set your Gemini API key

$env:GEMINI_API_KEY = "your-gemini-api-key"

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 3. Start the server

```bash
python app.py
```

Open **http://127.0.0.1:5000/** in your browser and use the chat.

## API

- **`POST /api/prompt`**  
  - **Body (JSON):** `{ "prompt": "your question or message" }`  
  - **Response:** `{ "response": "LLM reply text" }` or `{ "error": "...", "details": "..." }` on failure.

## Project layout

```
materials-copilot/
├── app.py              # Flask app: GET /, POST /api/prompt
├── llm_interface.py     # Gemini client
├── templates/
│   └── index.html      # Chat UI
├── requirements.txt
└── README.md
```

# Materials Copilot Video 



https://github.com/user-attachments/assets/1e028736-4792-4d41-9b47-40f102a391f7





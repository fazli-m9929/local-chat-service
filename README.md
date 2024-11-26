# Chat Generation Service with FastAPI and Local Model

This project provides a simple FastAPI-based service for generating chat responses using a locally hosted model. It includes APIs to send messages and get responses, leveraging Hugging Face's Transformers library.

## Features

- Host a local chat model (e.g., `Dorna-Llama3-8B-Instruct`).
- REST API endpoint for generating chat responses.
- Python client to interact with the chat service.

---

## Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/fazli-m9929/local-chat-service.git
   cd chat-service
   ```

2. **Install Dependencies**

   Ensure you have Python 3.8 or later installed. Install dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

3. **Download or Place the Model**

   Place your model files (e.g., `Dorna-Llama3-8B-Instruct`) in the `app/model/` directory. The directory should contain all necessary files for the model, including tokenizer and weights.

4. **Run the Server**

   Start the FastAPI server:

   ```
   python main.py
   ```

   The API will be available at `http://127.0.0.1:7000`.

---

## API Usage

### POST /chat/

Send a JSON payload to the `/chat/` endpoint to generate a response.

**Request Body**:

   ```json
   {
     "messages": [
       {"role": "system", "content": "just say hello in Persian"},
       {"role": "user", "content": "سلام"}
     ],
     "temperature": 0.01,
     "max_new_tokens": 1
   }
   ```

**Response**:

   ```json
   {
     "role": "assistant",
     "response": "سلام"
   }
   ```

---

## Python Client Usage

You can interact with the service programmatically via Python:

### Using `ChatService` Directly

   ```python
   from app.services.chat_service import ChatService

   client = ChatService('./app/model/Dorna-Llama3-8B-Instruct/')
   response = client.chat(
       messages=[
           {"role": "system", "content": "just say hello in Persian"},
           {"role": "user", "content": "سلام"},
       ],
       temperature=0.01,
       max_new_tokens=1,
   )
   print(response)
   ```

### Using HTTP Requests

   ```python
   import requests

   payload = {
       "messages": [
           {"role": "system", "content": "just say hello in Persian"},
           {"role": "user", "content": "سلام"}
       ],
       "temperature": 0.01,
       "max_new_tokens": 1
   }

   response = requests.post('http://127.0.0.1:7000/chat/', json=payload).json()
   print(response['response'])
   ```

---

## Project Structure

   ```
   .
   ├── app/
   │   ├── api/
   │   │    ├── chat.py                     # FastAPI chat endpoint
   │   │    └── __init__.py
   │   ├── model/                      # Directory for storing the local model
   │   │   └── Dorna-Llama3-8B-Instruct/
   │   ├── services/
   │   │   ├── __init__.py
   │   │   ├── chat_service.py         # Handles chat generation logic
   │   │   └── model_service.py        # Manages model loading and inference
   │   └── main.py                         # Entry point for running the server
   ├── requirements.txt                # List of dependencies
   └── README.md                       # Documentation
   ```

---

## Requirements

The following packages are required to run the service:

   ```
      fastapi
      uvicorn
      torch
      torchvision
      torchaudio
      transformers
   ```

Install these via `pip install -r requirements.txt`.

---

## Notes

1. Ensure you have GPU support with CUDA installed for optimal performance.
2. The model directory should contain all files required by the `transformers` library, including the tokenizer and model weights.
3. Customize parameters like `temperature` and `max_new_tokens` in the request payload as needed.

---

## License

This project is open-source and licensed under the MIT License.

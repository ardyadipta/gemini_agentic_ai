# Gemini - Agentic AI Research Assistant

author: Ardya Dipta Nandaviri ([GDE in AI/ML](https://g.dev/ardyadipta)) | date: Feb 20, 2025


## Overview
This project implements an **Agentic AI Research Assistant** using **Google Generative AI** and **Retrieval-Augmented Generation (RAG)**. The system first checks if an answer exists in a **FAISS vector database** before searching the web for new information. If a match is found, the stored response is returned. Otherwise, the assistant performs a web search, summarizes the results, and stores the new information for future use.

## Features
- **AI-Powered Summarization**: Uses Google Generative AI to extract key points.
- **FAISS Vector Database**: Stores and retrieves knowledge efficiently.
- **Streamlit UI**: Provides an easy-to-use web interface.
- **Web Search Integration**: Uses SerpAPI for dynamic knowledge retrieval.

## Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **Google Generative AI (Gemini)**
- **FAISS (Facebook AI Similarity Search)**
- **SerpAPI**
- **dotenv** (for API key management)

## Installation
### 1. Clone the repository
```sh
git clone https://github.com/your-username/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant
```

### 2. Set up a virtual environment (optional but recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project directory and add the following:
```
GOOGLE_API_KEY=your-google-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```

### 5. Run the application
```sh
streamlit run app.py
```

## Usage
1. Open the Streamlit web interface.
2. Enter a research query in the text input field.
3. The AI will first check the FAISS vector database.
4. If the answer is found, it will be retrieved and displayed.
5. If not, the AI will search the web, summarize the findings, and store them in the database for future use.

## File Structure
```
agentic-ai-research-assistant/
│── app.py                # Main application file
│── requirements.txt       # Python dependencies
│── .env                  # API keys (excluded from GitHub)
│── README.md             # Project documentation
│── faiss_index_store/     # Stored knowledge base (create this directory)
```

## Contributing
Pull requests are welcome! If you'd like to contribute:
1. Fork the repo.
2. Create a feature branch.
3. Make changes and commit.
4. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries, please contact [ardyadipta@gmail.com].


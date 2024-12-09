# Chromebook LLM Chatbot

A Streamlit-based chatbot application that uses OpenAI's GPT-4 to generate responses with different personalities.

## Features

- Multiple personality modes (Normal, Brainy, Mean, Cat)
- Adjustable response creativity using temperature slider
- Simple and intuitive user interface
- Powered by OpenAI's GPT-4

## Setup

1. Clone the repository:
```bash
git clone https://github.com/DeVReV27/chromebook-llm-chatbot.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Select a personality from the sidebar
2. Adjust the response creativity using the temperature slider
3. Type your message in the input field
4. Get AI-generated responses based on your selected personality

## Technologies Used

- Python
- Streamlit
- OpenAI API
- python-dotenv

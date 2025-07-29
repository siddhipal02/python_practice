
from dotenv import load_dotenv
load_dotenv()  
import base64
import os
import sys
from google import genai
from google.genai import types

ALLOWED_FIELDS = ["Artificial Intelligence", "Deep learning", "machine learning"]
field_keywords = {
    "artificial intelligence": ["ai", "artificial intelligence", "neural", "intelligent systems"],
    "deep learning": ["deep learning", "neural network", "cnn", "rnn", "lstm"],
    "machine learning": ["machine learning", "ml", "regression", "classification", "supervised", "unsupervised"],
}

def is_question_valid_for_field(question, field):
    keywords = field_keywords.get(field.lower(), [])
    return any(keyword.lower() in question.lower() for keyword in keywords)

def generate(user_input, field):
    if field.lower() not in [f.lower() for f in ALLOWED_FIELDS]:
        print(f" Error: '{field}' is not a supported field.")
        print(f"Supported fields are: {', '.join(ALLOWED_FIELDS)}")
        sys.exit(1)
    
    if not is_question_valid_for_field(user_input, field):
        print(f" Error: Your question doesn't seem to be related to the selected field '{field}'.")
        sys.exit(1)
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    field = input("Enter the field like Artificial Intelligence, Deep learning, machine learning: ").strip()
    user_input = input("Enter your prompt/question: ").strip()
    generate(user_input, field)

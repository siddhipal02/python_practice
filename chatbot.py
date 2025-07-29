from dotenv import load_dotenv
load_dotenv()
import base64
import os
import sys
from google import genai
from google.genai import types


def generate(query):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=query),
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
        system_instruction=[
            types.Part.from_text(text="""answer only machine learning or AI  related questions else show no info available
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    query = input("Enter your question related to AI/ML: ")
    generate(query)

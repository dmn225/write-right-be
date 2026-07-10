import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai

load_dotenv()


# For Gemini Model

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

async def correct_text(text):

    print("Calling Gemini...")

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"""
Correct the grammar.

Only return the corrected sentence.

Sentence:
{text}
"""
    )

    print("Gemini finished")

    return response.text




# For GPT Model


# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# async def correct_text(text):

#     print("Calling GPT...")

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a language tutor. Correct grammar and only return the corrected sentence."
#             },
#             {
#                 "role": "user",
#                 "content": text
#             }
#         ]
#     )

#     print("GPT finished")

#     return response.text
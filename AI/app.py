from transformers import pipeline
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# client = genai.Client(api_key=f"{os.environ["GEMINI_API_KEY"]}")
# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works"
# )
# print(response.text)


summarizer = pipeline('summarization')

async def summarize(query: str) -> str:
  """Summarizing the data into small piece of text."""
  try:
    res = summarizer(query, max_length=1000, min_length=10, do_sample=False)
    return res[0]['summary_text']
  except IndexError:
    return "Too big data"
  except Exception as e:
    raise f"Error while process the data {e}"
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from .utils.jsonParse import format_str_to_json
from .AI.app import summarize
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query/")
async def root(request: Request):
    # Get the qeury body
    data = await request.body()
    # Retrieve the @query field from the qeury's body
    text = format_str_to_json(data.decode())['query']
    print(text, len(text))
    summary = await summarize(text)
    return {"text": summary}

@app.get("/")
async def root():
    return {"text": "Hello World"}
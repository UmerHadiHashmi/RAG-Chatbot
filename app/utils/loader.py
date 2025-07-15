import json
from langchain.schema import Document

def load_documents(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []
    for item in data:
        content = f"Q: {item['question']}\nA: {item['answer']}"
        docs.append(Document(page_content=content))
    return docs

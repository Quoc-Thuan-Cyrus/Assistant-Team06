# AI interface design

## Function signature
def answer_question(question: str, context: dict | None = None) -> dict:

## Inputs
- question: question from the user
- context: optional retrieval data

## Outputs
{
  "answer": "text",
  "sources": [],
  "confidence": 0.0,
  "error": null
}

## Errors
- LLM unavailable
- Request timeout
- Bad input data

## Fallback
If the LLM fails, return a safe, non-technical fallback answer.

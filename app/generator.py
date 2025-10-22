from openai import OpenAI
from app.config import settings

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """You are KnowFlow AI, a helpful assistant.
Answer the question strictly using the provided context.
If the answer is not in the context, say "The document does not contain this information."
Always finish with a short 'Sources' section showing which chunks were used.
Keep responses concise and factual.
"""

def build_context(chunks):
    """Combine retrieved chunks into a single text block for the model."""
    return "\n\n".join([f"[{i+1}] {c.page_content}" for i, c in enumerate(chunks)])


def generate_answer(question, retrieved_chunks):
    """Generate an answer from the LLM using retrieved context."""
    context = build_context(retrieved_chunks)
    user_prompt = f"Question: {question}\n\nContext:\n{context}\n\nAnswer:"

    response = client.chat.completions.create(
        model=settings.CHAT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_tokens=400
    )

    answer = response.choices[0].message.content.strip()
    return answer

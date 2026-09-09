import ollama

from retrieval import search_documents


MODEL_NAME = "gemma3"


def answer_question(
    query,
    chunks,
    chunk_embeddings,
    embedding_model,
    top_k=5
):
    # Step 1: Retrieve relevant document chunks
    results = search_documents(
        query,
        chunks,
        chunk_embeddings,
        embedding_model,
        top_k=top_k
    )

    if not results:
        return {
            "answer": "I could not find relevant information in the uploaded documents.",
            "sources": []
        }

    # Step 2: Build the context for Gemma
    context_parts = []

    for result in results:
        context_parts.append(
            f"Source: {result['source']}, "
            f"Page: {result['page']}\n"
            f"{result['text']}"
        )

    context = "\n\n".join(context_parts)

    # Step 3: Create the RAG prompt
    prompt = f"""
You are a helpful AI assistant that answers questions
using the provided document context.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{query}

Instructions:
- Answer using the document context.
- Do not invent information.
- If the answer is not present in the context,
  say that the information was not found in the document.
- Give a clear and concise answer.
"""

    # Step 4: Ask Gemma
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    # Step 5: Return answer and sources
    sources = list(dict.fromkeys(
        (result["source"], result["page"])
        for result in results
    ))

    return {
        "answer": answer,
        "sources": sources
    }





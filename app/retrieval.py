from sklearn.metrics.pairwise import cosine_similarity


def search_documents(
    query,
    chunks,
    chunk_embeddings,
    embedding_model,
    top_k=5
):
    # Convert user question into an embedding
    query_embedding = embedding_model.encode([query])

    # Compare  question with every document chunk
    similarities = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    # Words from user's question
    query_words = set(query.lower().split())

    results = []

    for index, chunk in enumerate(chunks):

        text_lower = chunk["text"].lower()

        # Simple keyword matching
        keyword_matches = sum(
            1
            for word in query_words
            if len(word) > 3 and word in text_lower
        )

        # Hybrid score
        final_score = (
            similarities[index]
            + keyword_matches * 0.05
        )

        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "page": chunk["page"],
            "score": final_score
        })

    # Highest-scoring chunks first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]




if __name__ == "__main__":

    from document import read_pdf, create_document_chunks
    from embeddings import embedding_model, create_embeddings

    pages = read_pdf("../data/my_document.pdf")

    documents = [
        {
            "filename": "my_document.pdf",
            "page": page["page"],
            "text": page["text"]
        }
        for page in pages
    ]

    chunks = create_document_chunks(documents)

    chunk_embeddings = create_embeddings(chunks)

    query = "What is the main objective of this project?"

    results = search_documents(
        query,
        chunks,
        chunk_embeddings,
        embedding_model,
        top_k=5
    )

    print("\nTop results:\n")

    for result in results:
        print(
            f"Page {result['page']} | "
            f"Score: {result['score']:.3f}"
        )
        print(result["text"][:300])
        print("-" * 60)
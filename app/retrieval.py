from sklearn.metrics.pairwise import cosine_similarity
from indexer import load_index


def search_documents(
    query,
    chunks=None,
    chunk_embeddings=None,
    embedding_model=None,
    top_k=5,
    min_score=0.20
):

    if chunks is None or chunk_embeddings is None:
        index = load_index()

        if index is None:
            raise FileNotFoundError(
                "No document index found. Build the index first."
            )

        chunks = index["chunks"]
        chunk_embeddings = index["embeddings"]

    # Convert user question into an embedding
    if embedding_model is None:
        from embeddings import embedding_model

    query_embedding = embedding_model.encode([query])

    # Compare  question with every document chunk
    similarities = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    # Words from user's question
    query_words = {
        word.lower().strip(".,!?;:")
        for word in query.split()
        if len(word) > 3
    }

    results = []

    for index, chunk in enumerate(chunks):

        text_lower = chunk["text"].lower()

        # Simple keyword matching
        keyword_matches = sum(
            1
            for word in query_words
            if word in text_lower
        )

        keyword_score = (
            keyword_matches / len(query_words)
            if query_words
            else 0
        )

        final_score = (
                similarities[index] * 0.85
                + keyword_score * 0.15
        )

        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "file_type": chunk["file_type"],
            "page": chunk["page"],
            "score": final_score
        })

    # Highest-scoring chunks first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    results = [
        result
        for result in results
        if result["score"] >= min_score
    ]

    return results[:top_k]





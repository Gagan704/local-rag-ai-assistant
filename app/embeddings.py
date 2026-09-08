from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks):

    chunk_texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedding_model.encode(
        chunk_texts,
        show_progress_bar=True
    )

    return embeddings





if __name__ == "__main__":

    from document import read_pdf, create_document_chunks

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

    embeddings = create_embeddings(chunks)

    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("Embedding shape:", embeddings.shape)
import os
import pickle

from document import load_documents, create_document_chunks
from embeddings import create_embeddings


INDEX_PATH = "../data/document_index.pkl"


def build_index(data_folder="../data"):
    documents = load_documents(data_folder)
    chunks = create_document_chunks(documents)
    embeddings = create_embeddings(chunks)

    index = {
        "chunks": chunks,
        "embeddings": embeddings
    }

    with open(INDEX_PATH, "wb") as file:
        pickle.dump(index, file)

    return index


def load_index():
    if not os.path.exists(INDEX_PATH):
        return None

    with open(INDEX_PATH, "rb") as file:
        return pickle.load(file)






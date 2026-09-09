from indexer import load_index
from rag import answer_question


class AIService:
    def __init__(self):
        self.index = load_index()

    def ask(self, question):
        if not question or not question.strip():
            return {
                "answer": "Please enter a question.",
                "sources": []
            }

        if self.index is None:
            return {
                "answer": "No documents have been indexed yet.",
                "sources": []
            }






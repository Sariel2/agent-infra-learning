from pydantic import BaseModel


class Document(BaseModel):
    title: str
    content: str


class RetrievalResult(BaseModel):
    title: str
    score: int
    citation: str


DOCS = [
    Document(title="agent-basics", content="Agent infra includes tools tracing evals and workflow."),
    Document(title="rag-notes", content="RAG uses retrieval citations and document chunks."),
]


def retrieve(query: str) -> list[RetrievalResult]:
    query_tokens = set(query.lower().split())
    results = []
    for doc in DOCS:
        score = len(query_tokens & set(doc.content.lower().split()))
        if score:
            results.append(RetrievalResult(title=doc.title, score=score, citation=f"{doc.title}:1"))
    return sorted(results, key=lambda item: item.score, reverse=True)


def main() -> None:
    print([item.model_dump() for item in retrieve("retrieval citations")])


if __name__ == "__main__":
    main()

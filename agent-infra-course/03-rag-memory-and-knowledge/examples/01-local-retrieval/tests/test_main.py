from app.main import retrieve


def test_retrieve_returns_ranked_results() -> None:
    results = retrieve("retrieval citations")
    assert results[0].title == "rag-notes"

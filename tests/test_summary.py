from services.summary import generate_summary

def test_generate_summary():
    text = "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints."
    summary = generate_summary(text)
    assert "fastapi" in summary.lower()

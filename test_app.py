
from pathlib import Path

def test_homepage():
    content = Path("index.html").read_text()
    assert "Learning GitHub Actions" in content

if __name__ == "__main__":
    test_homepage()
    print("Test passed!")

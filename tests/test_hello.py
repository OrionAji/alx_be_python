def test_hello():
    assert "hello".upper() == "HELLO"

def test_hello_length():
    assert len("hello") == 5

def test_hello_contains():
    assert "hello" in "hello world"
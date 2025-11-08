# tests/test_sample.py

def add(a, b):
    """Function to add two numbers."""
    return a + b

def test_add():
    """Test case for the add function."""
    assert add(2, 3) == 5, "Expected 2 + 3 to be 5"
    assert add(0, 0) == 0, "Expected 0 + 0 to be 0"
    assert add(-1, 1) == 0, "Expected -1 + 1 to be 0"

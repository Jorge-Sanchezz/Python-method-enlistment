from tested_hello_23 import hello

def test_default():
    assert hello() == "Hello, world"
    
def test_argument():
    assert hello("Jorge") == "Hello, Jorge"

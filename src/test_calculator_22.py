from tested_calculator_21 import square

#Run with 'pytest' tool after installing it writing 'pip install pytest' on your 
#terminal (to run it, just write 'pytest test_calculator_22.py' in this case)
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
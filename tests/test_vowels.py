from programs.vowels import vowels

def test_hello():
    assert vowels("hello")==2

def test_mixed_case():
    assert vowels("AAAaaaBBBbbb")==6

def test_empty_string():
    assert vowels("")==0
from programs.factorial import fact

def test_fact_1():
    assert fact(1)==1

def test_fact_3():
    assert fact(3)==6

def test_fact():
    assert fact(0)==1
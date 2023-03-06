from mypackage import mymodule

def test_top_n():
    """
    To test if the function, top_n, works correctly
    """
    assert mymodule.top_n([4,6,9,2,7],3) == [9,7,6], 'Incorrect'
    assert mymodule.top_n([11,5,40,6,9,2,7],5) == [40,11,9,7,6], 'Incorrect'
    assert mymodule.top_n([15,0,19,2,7],2) == [19,15], 'Incorrect'
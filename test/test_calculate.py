from calculate import add_func

def test_ad_func():
    assert add_func(1,2)==3
    assert add_func(0,0)==0
    assert add_func(-1,-2)==-3
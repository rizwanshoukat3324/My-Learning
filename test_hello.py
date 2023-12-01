from hello import hello

def test_default():
    hello()=="hello,World"

def test_argument():
    hello("Rizwan")=="Hello, Rizwan"


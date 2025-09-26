
import pytest

#to skip this
@pytest.mark.skip  
def test_firstprogram():
    msg = "vinayak"#operations
    assert msg == "mahadev","test failed because strings do not match"


@pytest.mark.smoke
def test_secondprogram():
    a = 4
    b = 6
    assert a+2 == 6
    print('Run sucessfully..')


#when it comes across this setup it will check if there is any fixture defind this setup, its defined means its first executie 
#the def setup first and then only it runs, In selenium framework we use this fixtures for opening a browser are seting up database
'''def test_fixturedemo(setup):
    print("I will execute steps in fixture demo")
'''

#declaring method in any class the manidatory parameter is self
@pytest.mark.usefixtures("setup")
class Testexample:
    def test_fixturedemo(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo1(self):
        print("I will execute steps in fixture demo1")

    def test_fixturedemo2(self):
        print("I will execute steps in fixture demo2")

    def test_fixturedemo3(self):
        print("I will execute steps in fixture demo3")



#

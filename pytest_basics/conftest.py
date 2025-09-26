#browser invoke part is comman for all the test case 
import pytest


@pytest.fixture(scope='class')
def setup():
    print('I will be executing first')
    yield
    print("I will executeed last")

@pytest.fixture()# we have to say this is the fixter to the pytest
def dataload():
    print("user profile data is being created")
    return ["Ranga","Rajan","https://peps.python.org/pep-0008/"]# pause the data from here to the test(we return here is list- mutable)

#multiple data set(each time one data is  passing)
@pytest.fixture(params=["chrome","firefox","IE"])
def crossbrowser(request):
    return request.param

#multiple data set(multiple data must pass for every single run)
@pytest.fixture(params=[("chrome","Ranga","ponday"),("firefox","raj"),("IE","RR")])
def multicrossdata(request):
    return request.param
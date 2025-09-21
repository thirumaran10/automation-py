# data loading
import pytest

@pytest.mark.usefixtures("dataload")
class Testexample2:

    def test_editprofile(self,dataload):
        print(dataload)


#parameterizing test with multiple data sets using fixtures
def test_crossbrowser(crossbrowser):
     print(crossbrowser)#it runs for three time because in parameter three diff datas are there

#multiple data must need to be pass for every run
def test_crossdata(multicrossdata):
    print(multicrossdata[1])#using index
 
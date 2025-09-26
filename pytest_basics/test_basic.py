# pytest method names should start with test
# any pytest file should start with test_ or end with _test
# any code should be wrapped in method only
# Method name should have sense
# -k stands for  method names execution (run using function name)
# -s stands for logs in output (print output in terminal)
# -v stands for more info metadata (. => passed)
# py.test <filename> you can run specific file
# mark (tag) tests '@pytest.mark.smoke' and then run with -m
# skip test with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixter and make it available to all test cases
# fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple formate
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_oneprogram(setup):
    print("vinayak")


@pytest.mark.xfail
def test_firstprogram1():
    print("mahadev")
# consider this as a parent class

class browserutils:

    def __init__(self):
        self.driver = driver

    # want to apply a logic on particular page there is no point to write a header footer in every page, reduce a code
    def gettitle(self):
        return self.driver.title
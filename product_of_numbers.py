import math

class ProductOfNumbers(object):

    def __init__(self):
        self.data=[1,2]

    def add(self, num):
        self.data.append(num)
        """
        :type num: int
        :rtype: None
        """

    def getProduct(self, k):

        list = self.data[-k:]
        prod = 1
        for elem in list:
            prod *= elem

        return prod

        """
        :type k: int
        :rtype: int
        """

obj = ProductOfNumbers()
print(obj.data)
obj.add(3)
print(obj.data)
print(obj.getProduct(2))

import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        # self.fail("TODO: Write add unit test")
        self.assertEquals(katas.add(1, 1), 2)

    def test_multiply(self):
        # self.fail("TODO: Write multiply unit test")
        self.assertEquals(katas.multiply(2, 3), 6)

    def test_power(self):
        # self.fail("TODO: Write power unit test")
        self.assertEquals(katas.power(2, 2), 4)

    def test_factorial(self):
        # self.fail("TODO: Write factorial unit test")
        self.assertEquals(katas.factorial(3), 6)

    def test_fibonacci(self):
        # self.fail("TODO: Write fibonacci unit test")
        self.assertEquals(katas.fibonacci(2), 1)


if __name__ == '__main__':
    unittest.main()

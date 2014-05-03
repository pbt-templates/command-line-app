import {{cookiecutter.app_name}} as app
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dummy(self):
        self.assertEqual(4, 5)

if __name__ == '__main__':
    unittest.main()

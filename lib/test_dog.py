import unittest
from dog import Dog  # Import the Dog class from dog.py

class TestDog(unittest.TestCase):

    def test_is_class(self):
        '''Check if the class "Dog" is defined'''
        with self.assertRaises(TypeError):
            fido = Dog()

    def test_sit(self):
        fido = Dog("Fido", "Labrador")
        sit_result = fido.sit()
        self.assertEqual(sit_result, "The dog is sitting.")

    def test_bark(self):
        fido = Dog("Fido", "Labrador")
        bark_result = fido.bark()
        self.assertEqual(bark_result.strip(), "Fido says Woof!")

if __name__ == '__main__':
    unittest.main()

import unittest
from chatbot import get_response


class TestChatbot(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(get_response("hello"), "Hi!")
        self.assertEqual(get_response("HELLO!"), "Hi!")
        self.assertEqual(get_response("hi"), "Hi!")
        self.assertEqual(get_response("  hey  "), "Hi!")

    def test_how_are_you(self):
        self.assertEqual(get_response("how are you"), "I'm fine, thanks!")
        self.assertEqual(get_response("How are you?"), "I'm fine, thanks!")
        self.assertEqual(get_response("HOW ARE YOU DOING?"), "I'm fine, thanks!")

    def test_farewell(self):
        self.assertEqual(get_response("bye"), "Goodbye!")
        self.assertEqual(get_response("goodbye!"), "Goodbye!")
        self.assertEqual(get_response("exit"), "Goodbye!")

    def test_help_and_unknown(self):
        self.assertIn("You can say", get_response("help"))
        self.assertIn("I don't understand", get_response("random unknown query"))


if __name__ == "__main__":
    unittest.main()

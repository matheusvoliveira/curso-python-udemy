import unittest
import cap


class TextCap(unittest.TestCase):
# você cria uma classe pai de teste
    def test_one_word(self):
        #esse é um tipo de teste com só uma palavra
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')


    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
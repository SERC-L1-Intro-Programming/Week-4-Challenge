import unittest

from commacode import list_to_grammar


class Test(unittest.TestCase):

    def test_empty_list(self):
        result=list_to_grammar([])
        expected=""
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected, "Should be empty string")
        pass

    def test_single_item(self):
        items = ['a', 'cat', 5, 4.7]

        for item in items:
            result=list_to_grammar([item])
            expected=str(item)
            self.assertIsInstance(result, str)
            self.assertEqual(result, expected, "Should be single item as string")
        
    def test_list(self):
        test_items = [
            # test  # expected
            [['apples', 'bananas', 'tofu', 'cats'], 'apples, bananas, tofu and cats'],
            [['cats', 'dogs'], 'cats and dogs'],
            [[1, 2], '1 and 2'],
            [[1, 2, 3], '1, 2 and 3'],
            [[1, 2, 3, 4, 5], '1, 2, 3, 4 and 5'],
        ]

        for test_item in test_items:
            result=list_to_grammar(test_item[0])
            expected=test_item[1]
            self.assertIsInstance(result, str)
            self.assertEqual(result, expected, "Should be items seperated by comma")

    def test_not_list(self):
        test_items = ['eggs', 'a', 1, 2, 3.45]

        for item in test_items:
            self.assertRaises(TypeError, list_to_grammar(item))


if __name__ == '__main__':
    unittest.main()

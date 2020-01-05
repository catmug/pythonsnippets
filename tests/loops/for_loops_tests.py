import unittest
import io
import sys
from loops import for_loops
import unittest.mock

class TestLoops(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_for_each_printing(self, mock_stdout):
        """
        Test python for loop.
        """
        for_loops.for_each()
        self.assertEqual(mock_stdout.getvalue(), 'estonian\nenglish\nrussian\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_for_with_index(self, mock_stdout):
        """
        Test enumerated for loop.
        """
        for_loops.for_with_index()
        self.assertEqual(mock_stdout.getvalue(), '1 elantra\n2 passat\n')


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_for_with_range(self, mock_stdout):
        """
        Test for loop with range.
        """
        for_loops.for_with_range()
        self.assertEqual(mock_stdout.getvalue(), 'elantra\npassat\n')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_for_with_range_backwards(self, mock_stdout):
        """
        Test for loop with range backwards.
        """
        for_loops.for_with_range_backwards()
        self.assertEqual(mock_stdout.getvalue(), 'passat\nelantra\n')

if __name__ == '__main__':
    unittest.main()
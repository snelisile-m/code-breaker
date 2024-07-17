import unittest
from unittest.mock import patch
from io import StringIO
import mastermind
from test_base import captured_output
import io
import sys




class testMastermind(unittest.TestCase):
    

    def test_create_digit_len_digit(self):
        answer = mastermind.create_code()
        self.assertEqual(len(answer), 4)
        self.assertTrue(str, type(answer))


    def test_create_digit_content(self):  
        answer =mastermind.create_code()
        digits = [int(j) for j in range(1,9)]
        for x in range(100): 
            for i in answer:
                self.assertIn(i,digits)


    def test_check_correctness(self):
        with captured_output():
            answer = mastermind.check_correctness(1 ,2)
            self.assertFalse(answer)
            answer2 = mastermind.check_correctness(1,4)
            self.assertTrue(answer2)

    @patch("sys.stdin", StringIO("123\nabc\n1234"))
    def test_get_answer_input(self):
        with captured_output():
            answer = mastermind.get_answer_input()
            self.assertNotEqual(answer,"123")
            self.assertNotEqual(answer,"abc")
            self.assertEqual(answer,"1234")


    @patch("sys.stdin", StringIO("8562\n6412\n1234"))
    def test_take_turn(self):
        with captured_output():
            answer1 = (mastermind.take_turn([5, 4, 6, 2])) 
            self.assertEqual(answer1, (2, 1)) 
            answer2 = (mastermind.take_turn([3, 2, 1, 4]))
            self.assertEqual(answer2, (1, 2))
            answer3 = (mastermind.take_turn([1, 2, 3, 4]))
            self.assertEqual(answer3, (4, 0))


    
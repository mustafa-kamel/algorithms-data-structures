import io
from unittest import TestCase
from unittest.mock import patch

from recursion import count_down

builtins_print = "builtins.print"
sys_stdout = "sys.stdout"


class TestCountDown(TestCase):
    def test_high_zero(self):
        # Tests that the function prints 0 when high is 0
        with patch(sys_stdout, new=io.StringIO()) as fake_out:
            count_down(0)
            self.assertEqual(fake_out.getvalue().strip(), "0")

    def test_high_positive(self):
        # Tests that the function prints the numbers from high to 0 when high is a positive integer
        with patch(sys_stdout, new=io.StringIO()) as fake_out:
            count_down(5)
            self.assertEqual(fake_out.getvalue().strip(), "5\n4\n3\n2\n1\n0")

    def test_high_negative(self):
        # Tests that the function does not print anything when high is a negative integer
        with patch(sys_stdout, new=io.StringIO()) as fake_out:
            count_down(-5)
            self.assertEqual(fake_out.getvalue().strip(), "")

    def test_high_float(self):
        # Tests that the function raises a TypeError when high is a float
        count_down(3.14)

    def test_high_none(self):
        # Tests that the function raises a TypeError when high is None
        with self.assertRaises(TypeError):
            count_down(None)

    def test_high_string(self):
        # Tests that the function raises a TypeError when high is a string
        with self.assertRaises(TypeError):
            count_down("5")

    def test_high_string_chars(self):
        # Tests that the function raises a TypeError when high is a non-integer argument
        with self.assertRaises(TypeError):
            count_down("abc")

    def test_high_minus_one(self):
        # Tests that the function does not print anything when high is -1
        with patch(sys_stdout, new=io.StringIO()) as fake_out:
            count_down(-1)
            self.assertEqual(fake_out.getvalue().strip(), "")

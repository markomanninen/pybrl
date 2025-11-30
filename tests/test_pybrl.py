import unittest
from pybrl.main import braille, ascii, hex, dot, matrix, hex2braille, dot2braille, matrix2braille

class TestPyBrl(unittest.TestCase):
    def test_ascii_to_braille(self):
        self.assertEqual(braille("a"), "⠁")
        self.assertEqual(braille("b"), "⠃")
        self.assertEqual(braille("hello world"), "⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙")

    def test_braille_to_ascii(self):
        self.assertEqual(ascii("⠁"), "a")
        self.assertEqual(ascii("⠃"), "b")
        self.assertEqual(ascii("⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙"), "hello world")

    def test_braille_to_hex(self):
        # 'a' -> '⠁' -> hex?
        # Based on library mapping, 'a' (braille ⠁) maps to hex '41' (which is 'A' in ASCII table, but used here)
        res = hex("⠁")
        self.assertEqual(res, ['41'])

    def test_hex_to_braille(self):
        self.assertEqual(hex2braille(['41']), "⠁")

    def test_braille_to_dot(self):
        # a -> ⠁ -> dot 1
        res = dot("⠁")
        self.assertEqual(res, ['1'])

    def test_dot_to_braille(self):
        self.assertEqual(dot2braille(['1']), "⠁")

    def test_matrix_roundtrip(self):
        b_str = "⠁"
        m = matrix(b_str)
        # Expected matrix for 'a' (⠁) which is dot 1.
        # dot 1 is top left.
        # [[1, 0], [0, 0], [0, 0]]
        self.assertEqual(m, [[[1, 0], [0, 0], [0, 0]]])

        b_back = matrix2braille(m)
        self.assertEqual(b_back, b_str)

if __name__ == '__main__':
    unittest.main()

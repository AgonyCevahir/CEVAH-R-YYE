import unittest

from app.core.root import Root


class TestRoot(unittest.TestCase):

    def test_root_letters(self):
        root = Root("ن", "ص", "ر")

        self.assertEqual(root.fa, "ن")
        self.assertEqual(root.ayn, "ص")
        self.assertEqual(root.lam, "ر")

    def test_root_text(self):
        root = Root("ن", "ص", "ر")

        self.assertEqual(root.text, "نصر")

    def test_root_letters_tuple(self):
        root = Root("ن", "ص", "ر")

        self.assertEqual(
            root.letters,
            ("ن", "ص", "ر")
        )


if __name__ == "__main__":
    unittest.main()
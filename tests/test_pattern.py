import unittest

from app.core.root import Root
from app.core.pattern import apply_pattern


class TestPattern(unittest.TestCase):

    def test_past_pattern(self):
        root = Root("ن", "ص", "ر")

        result = apply_pattern(
            "فَعَلَ",
            root
        )

        self.assertEqual(
            result,
            "نَصَرَ"
        )

    def test_present_pattern(self):
        root = Root("ن", "ص", "ر")

        result = apply_pattern(
            "يَفْعُلُ",
            root
        )

        self.assertEqual(
            result,
            "يَنْصُرُ"
        )


if __name__ == "__main__":
    unittest.main()
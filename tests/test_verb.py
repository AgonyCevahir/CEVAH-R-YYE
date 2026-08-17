import unittest

from app.core.root import Root
from app.core.bab import BAB_1
from app.models.verb import Verb


class TestVerb(unittest.TestCase):

    def test_verb_data(self):
        root = Root("ن", "ص", "ر")

        verb = Verb(
            root=root,
            bab=BAB_1,
            past="نَصَرَ",
            present="يَنْصُرُ",
        )

        self.assertEqual(verb.root.text, "نصر")

        self.assertEqual(
            verb.bab.number,
            1
        )

        self.assertEqual(
            verb.bab.past_pattern,
            "فَعَلَ"
        )

        self.assertEqual(
            verb.bab.present_pattern,
            "يَفْعُلُ"
        )

        self.assertEqual(
            verb.past,
            "نَصَرَ"
        )

        self.assertEqual(
            verb.present,
            "يَنْصُرُ"
        )


if __name__ == "__main__":
    unittest.main()
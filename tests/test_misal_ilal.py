import unittest

from app.core.bab import BAB_2, BAB_4, BAB_5
from app.core.root import Root
from app.core.siga import SIGA_01, SIGA_02
from app.core.siga_engine import build_siga


class TestMisalYaIlal(unittest.TestCase):

    # ======================================================
    # 1 - ي س ر
    #
    # 2. BÂB
    #
    # يَسَرَ → يَيْسِرُ
    # ======================================================

    def test_yasar_mazi(self):
        root = Root(
            "ي",
            "س",
            "ر",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_2,
                SIGA_01,
            ),
            "يَسَرَ",
        )

    def test_yasar_muzari(self):
        root = Root(
            "ي",
            "س",
            "ر",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_2,
                SIGA_02,
            ),
            "يَيْسِرُ",
        )

    # ======================================================
    # 2 - ي ب س
    #
    # 4. BÂB
    #
    # يَبِسَ → يَيْبَسُ
    # ======================================================

    def test_yabisa_mazi(self):
        root = Root(
            "ي",
            "ب",
            "س",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_4,
                SIGA_01,
            ),
            "يَبِسَ",
        )

    def test_yabisa_muzari(self):
        root = Root(
            "ي",
            "ب",
            "س",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_4,
                SIGA_02,
            ),
            "يَيْبَسُ",
        )

    # ======================================================
    # 3 - ي م ن
    #
    # 5. BÂB
    #
    # يَمُنَ → يَيْمُنُ
    # ======================================================

    def test_yamuna_mazi(self):
        root = Root(
            "ي",
            "م",
            "ن",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_5,
                SIGA_01,
            ),
            "يَمُنَ",
        )

    def test_yamuna_muzari(self):
        root = Root(
            "ي",
            "م",
            "ن",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_5,
                SIGA_02,
            ),
            "يَيْمُنُ",
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from app.core.bab import (
    BAB_1,
    BAB_2,
    BAB_3,
    BAB_4,
    BAB_5,
    BAB_6,
)
from app.core.root import Root
from app.core.verb_engine import build_verb


class TestVerbEngine(unittest.TestCase):

    def setUp(self):
        self.nsr = Root(
            "ن",
            "ص",
            "ر",
        )

        self.drb = Root(
            "ض",
            "ر",
            "ب",
        )

        self.mdh = Root(
            "م",
            "د",
            "ح",
        )

        self.alm = Root(
            "ع",
            "ل",
            "م",
        )

        self.bsr = Root(
            "ب",
            "ص",
            "ر",
        )

        self.hsb = Root(
            "ح",
            "س",
            "ب",
        )

        # ====================================================
        # İ'LÂL İÇİN ECVEF KÖKLER
        # ====================================================

        self.qwl = Root(
            "ق",
            "و",
            "ل",
        )

        self.bya = Root(
            "ب",
            "ي",
            "ع",
        )

    # ========================================================
    # NORMAL BÂB TESTLERİ
    # ========================================================

    def test_bab_1(self):
        result = build_verb(
            self.nsr,
            BAB_1,
        )

        self.assertEqual(
            result.past,
            "نَصَرَ",
        )

        self.assertEqual(
            result.present,
            "يَنْصُرُ",
        )

    def test_bab_2(self):
        result = build_verb(
            self.drb,
            BAB_2,
        )

        self.assertEqual(
            result.past,
            "ضَرَبَ",
        )

        self.assertEqual(
            result.present,
            "يَضْرِبُ",
        )

    def test_bab_3(self):
        result = build_verb(
            self.mdh,
            BAB_3,
        )

        self.assertEqual(
            result.past,
            "مَدَحَ",
        )

        self.assertEqual(
            result.present,
            "يَمْدَحُ",
        )

    def test_bab_4(self):
        result = build_verb(
            self.alm,
            BAB_4,
        )

        self.assertEqual(
            result.past,
            "عَلِمَ",
        )

        self.assertEqual(
            result.present,
            "يَعْلَمُ",
        )

    def test_bab_5(self):
        result = build_verb(
            self.bsr,
            BAB_5,
        )

        self.assertEqual(
            result.past,
            "بَصُرَ",
        )

        self.assertEqual(
            result.present,
            "يَبْصُرُ",
        )

    def test_bab_6(self):
        result = build_verb(
            self.hsb,
            BAB_6,
        )

        self.assertEqual(
            result.past,
            "حَسِبَ",
        )

        self.assertEqual(
            result.present,
            "يَحْسِبُ",
        )

    # ========================================================
    # İ'LÂL ENTEGRASYONU — ECVEF VÂVÎ
    # ========================================================

    def test_qawl_past_qalb(self):
        result = build_verb(
            self.qwl,
            BAB_1,
        )

        self.assertEqual(
            result.past,
            "قَالَ",
        )

    def test_qawl_present_transfer(self):
        result = build_verb(
            self.qwl,
            BAB_1,
        )

        self.assertEqual(
            result.present,
            "يَقُولُ",
        )

    # ========================================================
    # İ'LÂL ENTEGRASYONU — ECVEF YÂÎ
    # ========================================================

    def test_baya_past_qalb(self):
        result = build_verb(
            self.bya,
            BAB_1,
        )

        self.assertEqual(
            result.past,
            "بَاعَ",
        )


if __name__ == "__main__":
    unittest.main()
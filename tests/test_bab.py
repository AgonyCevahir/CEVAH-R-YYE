import unittest

from app.core.bab import (
    BAB_1,
    BAB_2,
    BAB_3,
    BAB_4,
    BAB_5,
    BAB_6,
    BOGAZ_HARFLERI,
    SULASI_MUCERRED_BABLAR,
)


class TestBablar(unittest.TestCase):

    def test_alti_bab_var(self):
        self.assertEqual(len(SULASI_MUCERRED_BABLAR), 6)

    def test_bab_numaralari(self):
        numbers = [
            bab.number
            for bab in SULASI_MUCERRED_BABLAR
        ]

        self.assertEqual(
            numbers,
            [1, 2, 3, 4, 5, 6]
        )

    def test_bab_1(self):
        self.assertEqual(BAB_1.past_pattern, "فَعَلَ")
        self.assertEqual(BAB_1.present_pattern, "يَفْعُلُ")
        self.assertEqual(BAB_1.past_example, "نَصَرَ")
        self.assertEqual(BAB_1.present_example, "يَنْصُرُ")

    def test_bab_2(self):
        self.assertEqual(BAB_2.past_pattern, "فَعَلَ")
        self.assertEqual(BAB_2.present_pattern, "يَفْعِلُ")
        self.assertEqual(BAB_2.past_example, "ضَرَبَ")
        self.assertEqual(BAB_2.present_example, "يَضْرِبُ")

    def test_bab_3(self):
        self.assertEqual(BAB_3.past_pattern, "فَعَلَ")
        self.assertEqual(BAB_3.present_pattern, "يَفْعَلُ")
        self.assertEqual(BAB_3.past_example, "مَدَحَ")
        self.assertEqual(BAB_3.present_example, "يَمْدَحُ")

        self.assertIn("أ", BOGAZ_HARFLERI)
        self.assertIn("ح", BOGAZ_HARFLERI)
        self.assertIn("خ", BOGAZ_HARFLERI)
        self.assertIn("ع", BOGAZ_HARFLERI)
        self.assertIn("غ", BOGAZ_HARFLERI)
        self.assertIn("هـ", BOGAZ_HARFLERI)

        self.assertIn(
            "أَبَى - يَأْبَى",
            BAB_3.exceptions
        )

    def test_bab_4(self):
        self.assertEqual(BAB_4.past_pattern, "فَعِلَ")
        self.assertEqual(BAB_4.present_pattern, "يَفْعَلُ")
        self.assertEqual(BAB_4.past_example, "عَلِمَ")
        self.assertEqual(BAB_4.present_example, "يَعْلَمُ")

    def test_bab_5(self):
        self.assertEqual(BAB_5.past_pattern, "فَعُلَ")
        self.assertEqual(BAB_5.present_pattern, "يَفْعُلُ")
        self.assertIn("sadece lâzım", BAB_5.transitivity)

    def test_bab_6(self):
        self.assertEqual(BAB_6.past_pattern, "فَعِلَ")
        self.assertEqual(BAB_6.present_pattern, "يَفْعِلُ")
        self.assertEqual(BAB_6.past_example, "حَسِبَ")
        self.assertEqual(BAB_6.present_example, "يَحْسِبُ")


if __name__ == "__main__":
    unittest.main()
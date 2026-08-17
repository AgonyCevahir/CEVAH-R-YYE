import unittest

from app.core.siga import (
    EMSILE_I_MUHTELIFE,
    SIGA_01,
    SIGA_03,
    SIGA_15,
    SIGA_20,
    SIGA_24,
)


class TestSiga(unittest.TestCase):

    def test_twenty_four_sigam_var(self):
        self.assertEqual(
            len(EMSILE_I_MUHTELIFE),
            24,
        )

    def test_siga_numbers_are_sequential(self):
        numbers = [
            siga.number
            for siga in EMSILE_I_MUHTELIFE
        ]

        self.assertEqual(
            numbers,
            list(range(1, 25)),
        )

    def test_first_siga(self):
        self.assertEqual(SIGA_01.name, "Mâzi Fiil")
        self.assertEqual(SIGA_01.pattern, "فَعَلَ")
        self.assertEqual(SIGA_01.example, "نَصَرَ")

    def test_mastar_source_note(self):
        self.assertEqual(SIGA_03.example, "نَصْرًا")
        self.assertEqual(SIGA_03.meaning, "Yazmak")
        self.assertIn("S. 42", SIGA_03.note)

    def test_fifteenth_siga(self):
        self.assertEqual(
            SIGA_15.name,
            "İsm-i Zaman, İsm-i Mekân, Mastar-ı Mîmî",
        )
        self.assertEqual(
            SIGA_15.pattern,
            "مَفْعَلٌ",
        )

    def test_twentieth_siga_has_no_confirmed_pattern(self):
        self.assertIsNone(SIGA_20.pattern)

    def test_last_siga(self):
        self.assertEqual(
            SIGA_24.name,
            "Ta‘accup Fiili II",
        )
        self.assertEqual(
            SIGA_24.pattern,
            "أَفْعِلْ بِهِ",
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from app.core.ilal import (
    ILLET_HARFLERI,
    IlalResult,
    HarakaTransfer,
    apply_ilal_rule,
    delete_weak_letter,
    has_weak_letter,
    is_weak_letter,
    qalb_to_alif,
    sakinize_weak_letter,
    transfer_weak_vowel,
)


class TestIlal(unittest.TestCase):

    # ======================================================
    # İLLET HARFLERİ
    # ======================================================

    def test_ilet_harfleri(self):
        self.assertEqual(
            ILLET_HARFLERI,
            ("و", "ي", "ى"),
        )

    def test_is_weak_letter_true(self):
        self.assertTrue(
            is_weak_letter("و"),
        )

        self.assertTrue(
            is_weak_letter("ي"),
        )

        self.assertTrue(
            is_weak_letter("ى"),
        )

    def test_is_weak_letter_false(self):
        self.assertFalse(
            is_weak_letter("ن"),
        )

        self.assertFalse(
            is_weak_letter("ص"),
        )

    def test_has_weak_letter(self):
        self.assertTrue(
            has_weak_letter(
                ("ق", "و", "ل"),
            )
        )

        self.assertTrue(
            has_weak_letter(
                ("ب", "ي", "ع"),
            )
        )

        self.assertFalse(
            has_weak_letter(
                ("ن", "ص", "ر"),
            )
        )

    # ======================================================
    # KALB
    # ======================================================

    def test_qalb_vav_to_alif(self):
        result = qalb_to_alif(
            previous_letter="ق",
            weak_letter="و",
            previous_vowel="َ",
            weak_vowel="ُ",
        )

        self.assertEqual(
            result,
            "ا",
        )

    def test_qalb_ya_to_alif(self):
        result = qalb_to_alif(
            previous_letter="ب",
            weak_letter="ي",
            previous_vowel="َ",
            weak_vowel="ِ",
        )

        self.assertEqual(
            result,
            "ا",
        )

    def test_qalb_does_not_change_without_fatha(self):
        result = qalb_to_alif(
            previous_letter="ق",
            weak_letter="و",
            previous_vowel="ُ",
            weak_vowel="َ",
        )

        self.assertEqual(
            result,
            "و",
        )

    def test_qalb_does_not_change_non_weak_letter(self):
        result = qalb_to_alif(
            previous_letter="ن",
            weak_letter="ص",
            previous_vowel="َ",
            weak_vowel="ُ",
        )

        self.assertEqual(
            result,
            "ص",
        )

    # ======================================================
    # HAZF
    # ======================================================

    def test_delete_weak_letter_when_meczum_and_final(self):
        result = delete_weak_letter(
            weak_letter="و",
            is_meczum=True,
            is_final=True,
        )

        self.assertEqual(
            result,
            "",
        )

    def test_delete_ya_when_meczum_and_final(self):
        result = delete_weak_letter(
            weak_letter="ي",
            is_meczum=True,
            is_final=True,
        )

        self.assertEqual(
            result,
            "",
        )

    def test_do_not_delete_weak_letter_when_not_meczum(self):
        result = delete_weak_letter(
            weak_letter="و",
            is_meczum=False,
            is_final=True,
        )

        self.assertEqual(
            result,
            "و",
        )

    def test_do_not_delete_weak_letter_when_not_final(self):
        result = delete_weak_letter(
            weak_letter="و",
            is_meczum=True,
            is_final=False,
        )

        self.assertEqual(
            result,
            "و",
        )

    def test_do_not_delete_strong_letter(self):
        result = delete_weak_letter(
            weak_letter="ر",
            is_meczum=True,
            is_final=True,
        )

        self.assertEqual(
            result,
            "ر",
        )

    # ======================================================
    # İSKÂN
    # ======================================================

    def test_sakinize_final_vav(self):
        result = sakinize_weak_letter(
            weak_letter="و",
            is_final=True,
        )

        self.assertEqual(
            result,
            "و",
        )

    def test_sakinize_final_ya(self):
        result = sakinize_weak_letter(
            weak_letter="ي",
            is_final=True,
        )

        self.assertEqual(
            result,
            "ي",
        )

    def test_sakinize_non_final_letter(self):
        result = sakinize_weak_letter(
            weak_letter="و",
            is_final=False,
        )

        self.assertEqual(
            result,
            "و",
        )

    # ======================================================
    # NAKL-İ HAREKE
    # ======================================================

    def test_transfer_vav_damma(self):
        result = transfer_weak_vowel(
            previous_vowel="ْ",
            weak_vowel="ُ",
            weak_letter="و",
        )

        self.assertEqual(
            result,
            HarakaTransfer(
                previous_vowel="ُ",
                weak_vowel="",
            ),
        )

    def test_transfer_ya_kesra(self):
        result = transfer_weak_vowel(
            previous_vowel="ْ",
            weak_vowel="ِ",
            weak_letter="ي",
        )

        self.assertEqual(
            result,
            HarakaTransfer(
                previous_vowel="ِ",
                weak_vowel="",
            ),
        )

    def test_do_not_transfer_strong_letter(self):
        result = transfer_weak_vowel(
            previous_vowel="ْ",
            weak_vowel="ُ",
            weak_letter="ص",
        )

        self.assertEqual(
            result,
            HarakaTransfer(
                previous_vowel="ْ",
                weak_vowel="ُ",
            ),
        )

    def test_do_not_transfer_without_vowel(self):
        result = transfer_weak_vowel(
            previous_vowel="ْ",
            weak_vowel="",
            weak_letter="و",
        )

        self.assertEqual(
            result,
            HarakaTransfer(
                previous_vowel="ْ",
                weak_vowel="",
            ),
        )

    # ======================================================
    # İ'LÂL SONUCU
    # ======================================================

    def test_apply_ilal_rule(self):
        result = apply_ilal_rule(
            original="قَوَلَ",
            result="قَالَ",
            rule="Kalb: vâv → elif",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="قَوَلَ",
                result="قَالَ",
                rule="Kalb: vâv → elif",
            ),
        )

        self.assertEqual(
            result.original,
            "قَوَلَ",
        )

        self.assertEqual(
            result.result,
            "قَالَ",
        )

        self.assertEqual(
            result.rule,
            "Kalb: vâv → elif",
        )


if __name__ == "__main__":
    unittest.main()agony
import unittest

from app.core.ilal_engine import (
    Harf,
    IlalEngine,
)


class TestIlalEngine(unittest.TestCase):

    # ======================================================
    # KALB
    # ======================================================

    def test_qalb_vav_to_alif(self):
        previous = Harf(
            "ق",
            "َ",
        )

        weak = Harf(
            "و",
            "ُ",
        )

        result = IlalEngine.qalb_to_alif(
            previous,
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "ا",
                "",
            ),
        )

    def test_qalb_ya_to_alif(self):
        previous = Harf(
            "ب",
            "َ",
        )

        weak = Harf(
            "ي",
            "ِ",
        )

        result = IlalEngine.qalb_to_alif(
            previous,
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "ا",
                "",
            ),
        )

    def test_qalb_does_not_apply_without_fatha(self):
        previous = Harf(
            "ق",
            "ُ",
        )

        weak = Harf(
            "و",
            "ُ",
        )

        result = IlalEngine.qalb_to_alif(
            previous,
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "و",
                "",
            ),
        )

    def test_qalb_does_not_apply_to_strong_letter(self):
        previous = Harf(
            "ن",
            "َ",
        )

        weak = Harf(
            "ص",
            "ُ",
        )

        result = IlalEngine.qalb_to_alif(
            previous,
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "ص",
                "",
            ),
        )

    # ======================================================
    # HAZF
    # ======================================================

    def test_delete_final_vav_when_meczum(self):
        weak = Harf(
            "و",
            "",
        )

        result = IlalEngine.delete_final_weak(
            weak,
            True,
        )

        self.assertEqual(
            result,
            Harf(
                "",
                "",
            ),
        )

    def test_delete_final_ya_when_meczum(self):
        weak = Harf(
            "ي",
            "",
        )

        result = IlalEngine.delete_final_weak(
            weak,
            True,
        )

        self.assertEqual(
            result,
            Harf(
                "",
                "",
            ),
        )

    def test_do_not_delete_final_weak_when_not_meczum(self):
        weak = Harf(
            "و",
            "ُ",
        )

        result = IlalEngine.delete_final_weak(
            weak,
            False,
        )

        self.assertEqual(
            result,
            Harf(
                "و",
                "ُ",
            ),
        )

    def test_do_not_delete_strong_letter(self):
        weak = Harf(
            "ر",
            "",
        )

        result = IlalEngine.delete_final_weak(
            weak,
            True,
        )

        self.assertEqual(
            result,
            Harf(
                "ر",
                "",
            ),
        )

    # ======================================================
    # İSKÂN
    # ======================================================

    def test_sakinize_final_vav(self):
        weak = Harf(
            "و",
            "ُ",
        )

        result = IlalEngine.sakinize_final_weak(
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "و",
                "",
            ),
        )

    def test_sakinize_final_ya(self):
        weak = Harf(
            "ي",
            "ِ",
        )

        result = IlalEngine.sakinize_final_weak(
            weak,
        )

        self.assertEqual(
            result,
            Harf(
                "ي",
                "",
            ),
        )

    # ======================================================
    # NAKL-İ HAREKE
    # ======================================================

    def test_transfer_vav_damma(self):
        previous = Harf(
            "ق",
            "ْ",
        )

        weak = Harf(
            "و",
            "ُ",
        )

        new_previous, new_weak = (
            IlalEngine.transfer_weak_vowel(
                previous,
                weak,
            )
        )

        self.assertEqual(
            new_previous,
            Harf(
                "ق",
                "ُ",
            ),
        )

        self.assertEqual(
            new_weak,
            Harf(
                "و",
                "",
            ),
        )

    def test_transfer_ya_kesra(self):
        previous = Harf(
            "ب",
            "ْ",
        )

        weak = Harf(
            "ي",
            "ِ",
        )

        new_previous, new_weak = (
            IlalEngine.transfer_weak_vowel(
                previous,
                weak,
            )
        )

        self.assertEqual(
            new_previous,
            Harf(
                "ب",
                "ِ",
            ),
        )

        self.assertEqual(
            new_weak,
            Harf(
                "ي",
                "",
            ),
        )

    def test_do_not_transfer_strong_letter(self):
        previous = Harf(
            "ق",
            "ْ",
        )

        weak = Harf(
            "ص",
            "ُ",
        )

        new_previous, new_weak = (
            IlalEngine.transfer_weak_vowel(
                previous,
                weak,
            )
        )

        self.assertEqual(
            new_previous,
            Harf(
                "ق",
                "ْ",
            ),
        )

        self.assertEqual(
            new_weak,
            Harf(
                "ص",
                "ُ",
            ),
        )

    # ======================================================
    # İLLET HARFİ KONTROLÜ
    # ======================================================

    def test_is_weak_vav(self):
        self.assertTrue(
            IlalEngine.is_weak("و"),
        )

    def test_is_weak_ya(self):
        self.assertTrue(
            IlalEngine.is_weak("ي"),
        )

    def test_is_weak_alif_maqsura(self):
        self.assertTrue(
            IlalEngine.is_weak("ى"),
        )

    def test_is_not_weak(self):
        self.assertFalse(
            IlalEngine.is_weak("ن"),
        )

    # ======================================================
    # İ'LÂL SONUCU
    # ======================================================

    def test_make_result(self):
        result = IlalEngine.make_result(
            original="قَوَلَ",
            result="قَالَ",
            rule="Kalb: vâv → elif",
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
    unittest.main()
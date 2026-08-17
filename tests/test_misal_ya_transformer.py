import unittest

from app.core.ilal_transformer import IlalTransformer


class TestMisalYaTransformer(unittest.TestCase):

    # ======================================================
    # 1 - KİTAPTAKİ DOĞRU ÖRNEK
    #
    # يُيْسَرُ
    # ↓
    # يُوسَرُ
    #
    # Yâ sâkin.
    # Önceki gerçek harf dammeli.
    # ======================================================

    def test_ya_to_vav(self):

        result = IlalTransformer.qalb_ya_to_vav(
            "يُيْسَرُ",
            2,
        )

        self.assertEqual(
            result.result,
            "يُوسَرُ",
        )

    # ======================================================
    # 2 - YÂ SÂKİN DEĞİLSE DÖNÜŞMEMELİ
    # ======================================================

    def test_ya_to_vav_requires_sukun(self):

        with self.assertRaises(ValueError):

            IlalTransformer.qalb_ya_to_vav(
                "يُيَسَرُ",
                2,
            )

    # ======================================================
    # 3 - ÖNCEKİ HARF DAMMELİ DEĞİLSE DÖNÜŞMEMELİ
    # ======================================================

    def test_ya_to_vav_requires_previous_damma(self):

        with self.assertRaises(ValueError):

            IlalTransformer.qalb_ya_to_vav(
                "يِيسَرُ",
                2,
            )

    # ======================================================
    # 4 - BELİRTİLEN KONUMDA YÂ YOKSA
    # ======================================================

    def test_ya_to_vav_requires_ya(self):

        with self.assertRaises(ValueError):

            IlalTransformer.qalb_ya_to_vav(
                "يُوْسَرُ",
                2,
            )


if __name__ == "__main__":
    unittest.main()
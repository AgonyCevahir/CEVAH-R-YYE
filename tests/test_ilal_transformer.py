import unittest

from app.core.ilal import IlalResult
from app.core.ilal_transformer import IlalTransformer


class TestIlalTransformer(unittest.TestCase):

    # ======================================================
    # KALB — VÂV → ELİF
    # ======================================================

    def test_qalb_vav_to_alif(self):
        result = IlalTransformer.qalb_vav_to_alif(
            "قَوَلَ",
            2,
        )

        self.assertEqual(
            result,
            IlalResult(
                original="قَوَلَ",
                result="قَالَ",
                rule="Kalb: vâv → elif",
            ),
        )

    # ======================================================
    # KALB — YÂ → ELİF
    # ======================================================

    def test_qalb_ya_to_alif(self):
        result = IlalTransformer.qalb_ya_to_alif(
            "بَيَعَ",
            2,
        )

        self.assertEqual(
            result,
            IlalResult(
                original="بَيَعَ",
                result="بَاعَ",
                rule="Kalb: yâ → elif",
            ),
        )

    # ======================================================
    # KALB — HATALI KONUM
    # ======================================================

    def test_qalb_vav_wrong_position(self):
        with self.assertRaises(ValueError):
            IlalTransformer.qalb_vav_to_alif(
                "قَالَ",
                2,
            )

    def test_qalb_ya_wrong_position(self):
        with self.assertRaises(ValueError):
            IlalTransformer.qalb_ya_to_alif(
                "بَاعَ",
                2,
            )

    def test_qalb_index_out_of_range(self):
        with self.assertRaises(IndexError):
            IlalTransformer.qalb_vav_to_alif(
                "قَوَلَ",
                10,
            )

    # ======================================================
    # HAZF — SON İLLET HARFİ
    # ======================================================

    def test_delete_final_vav(self):
        result = IlalTransformer.delete_final_weak(
            "يَدْعُو",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَدْعُو",
                result="يَدْعُ",
                rule="Hazf: son illet harfi düşürüldü",
            ),
        )

    def test_delete_final_ya(self):
        result = IlalTransformer.delete_final_weak(
            "يَرْمِي",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَرْمِي",
                result="يَرْمِ",
                rule="Hazf: son illet harfi düşürüldü",
            ),
        )

    def test_delete_final_alif_maqsura(self):
        result = IlalTransformer.delete_final_weak(
            "يَسْعَى",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَسْعَى",
                result="يَسْعَ",
                rule="Hazf: son illet harfi düşürüldü",
            ),
        )

    def test_delete_final_strong_letter(self):
        with self.assertRaises(ValueError):
            IlalTransformer.delete_final_weak(
                "يَنْصُر",
            )

    def test_delete_empty_word(self):
        with self.assertRaises(ValueError):
            IlalTransformer.delete_final_weak(
                "",
            )

    # ======================================================
    # İSKÂN — SON HAREKE
    # ======================================================

    def test_remove_final_vowel_mark(self):
        result = IlalTransformer.remove_final_vowel_mark(
            "يَدْعُوُ",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَدْعُوُ",
                result="يَدْعُو",
                rule="İskân: son hareke kaldırıldı",
            ),
        )

    def test_remove_final_fatha(self):
        result = IlalTransformer.remove_final_vowel_mark(
            "يَرْمِيَ",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَرْمِيَ",
                result="يَرْمِي",
                rule="İskân: son hareke kaldırıldı",
            ),
        )

    def test_iskan_without_final_vowel(self):
        result = IlalTransformer.remove_final_vowel_mark(
            "يَدْعُو",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَدْعُو",
                result="يَدْعُو",
                rule="İskân: uygulanacak son hareke bulunamadı",
            ),
        )

    # ======================================================
    # NAKL-İ HAREKE — VÂV
    # ======================================================

    def test_transfer_vav_damma(self):
        result = IlalTransformer.transfer_vowel(
            "يَقْوُ",
            4,
            "ُ",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَقْوُ",
                result="يَقُو",
                rule="Nakl-i hareke: illet harfinin harekesi önceki harfe aktarıldı",
            ),
        )

    # ======================================================
    # NAKL-İ HAREKE — YÂ
    # ======================================================

    def test_transfer_ya_kesra(self):
        result = IlalTransformer.transfer_vowel(
            "يَبْيِ",
            4,
            "ِ",
        )

        self.assertEqual(
            result,
            IlalResult(
                original="يَبْيِ",
                result="يَبِي",
                rule="Nakl-i hareke: illet harfinin harekesi önceki harfe aktarıldı",
            ),
        )

    # ======================================================
    # NAKL-İ HAREKE — HATALI DURUMLAR
    # ======================================================

    def test_transfer_strong_letter(self):
        with self.assertRaises(ValueError):
            IlalTransformer.transfer_vowel(
                "يَقْصُ",
                4,
                "ُ",
            )

    def test_transfer_first_letter(self):
        with self.assertRaises(ValueError):
            IlalTransformer.transfer_vowel(
                "وُعِدَ",
                0,
                "ُ",
            )

    def test_transfer_invalid_vowel(self):
        with self.assertRaises(ValueError):
            IlalTransformer.transfer_vowel(
                "يَقْوُ",
                4,
                "ْ",
            )

    def test_transfer_wrong_vowel(self):
        with self.assertRaises(ValueError):
            IlalTransformer.transfer_vowel(
                "يَقْوُ",
                4,
                "ِ",
            )

    def test_transfer_index_out_of_range(self):
        with self.assertRaises(IndexError):
            IlalTransformer.transfer_vowel(
                "يَقْوُ",
                20,
                "ُ",
            )

    # ======================================================
    # KÜÇÜK SINIF KONTROLÜ
    # ======================================================

    def test_transformer_instance(self):
        transformer = IlalTransformer()

        self.assertIsInstance(
            transformer,
            IlalTransformer,
        )


if __name__ == "__main__":
    unittest.main()
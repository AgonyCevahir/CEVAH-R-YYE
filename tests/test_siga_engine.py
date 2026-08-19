import unittest

from app.core.bab import BAB_1
from app.core.root import Root
from app.core.siga import (
    SIGA_01,
    SIGA_02,
    SIGA_03,
    SIGA_04,
    SIGA_05,
    SIGA_06,
    SIGA_07,
    SIGA_08,
    SIGA_09,
    SIGA_10,
    SIGA_11,
    SIGA_12,
    SIGA_13,
    SIGA_14,
    SIGA_15,
    SIGA_16,
    SIGA_17,
    SIGA_18,
    SIGA_19,
    SIGA_20,
    SIGA_21,
    SIGA_22,
    SIGA_23,
    SIGA_24,
)
from app.core.siga_engine import build_siga


class TestSigaEngine(unittest.TestCase):

    def setUp(self):

        # ==================================================
        # SAĞLAM KÖK
        # ن ص ر
        # ==================================================

        self.nsr = Root(
            "ن",
            "ص",
            "ر",
        )

        # ==================================================
        # ECVEF VÂV
        # ق و ل
        # ==================================================

        self.qwl = Root(
            "ق",
            "و",
            "ل",
        )

        # ==================================================
        # ECVEF YÂ
        # ب ي ع
        # ==================================================

        self.bya = Root(
            "ب",
            "ي",
            "ع",
        )

        # ==================================================
        # MUDÂAF
        # م د د
        # ==================================================

        self.mdd = Root(
            "م",
            "د",
            "د",
        )

    # ======================================================
    # 1 - MÂZİ
    # ======================================================

    def test_mazi(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_01,
            ),
            "نَصَرَ",
        )

    # ======================================================
    # 2 - MUZÂRİ
    # ======================================================

    def test_muzari(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_02,
            ),
            "يَنْصُرُ",
        )

    # ======================================================
    # 3 - MASTAR
    # ======================================================

    def test_mastar_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_03,
            )

    # ======================================================
    # 4 - İSM-İ FÂİL
    # ======================================================

    def test_ismi_fail(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_04,
            ),
            "نَاصِرٌ",
        )

    # ======================================================
    # 5 - İSM-İ MEF'ÛL
    # ======================================================

    def test_ismi_meful(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_05,
            ),
            "مَنْصُورٌ",
        )

    # ======================================================
    # 6 - CAHD-I MUTLAK
    # ======================================================

    def test_cahd_mutlak(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_06,
            ),
            "لَمْ يَنْصُرْ",
        )

    # ======================================================
    # 7 - CAHD-I MUSTAĞRAK
    # ======================================================

    def test_cahd_mustagrak(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_07,
            ),
            "لَمَّا يَنْصُرْ",
        )

    # ======================================================
    # 8 - NEFY-İ HÂL
    # ======================================================

    def test_nefy_hal(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_08,
            ),
            "مَا يَنْصُرُ",
        )

    # ======================================================
    # 9 - NEFY-İ İSTİKBÂL
    # ======================================================

    def test_nefy_istikbal(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_09,
            ),
            "لَا يَنْصُرُ",
        )

    # ======================================================
    # 10 - TE'KÎD NEFY-İ İSTİKBÂL
    # ======================================================

    def test_tekid_nefy_istikbal(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_10,
            ),
            "لَنْ يَنْصُرَ",
        )

    # ======================================================
    # 11 - EMR-İ ĞÂİB
    # ======================================================

    def test_emr_gaib(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_11,
            ),
            "لِيَنْصُرْ",
        )

    # ======================================================
    # 12 - NEHY-İ ĞÂİB
    # ======================================================

    def test_nehy_gaib(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_12,
            ),
            "لَا يَنْصُرْ",
        )

    # ======================================================
    # 13 - EMR-İ HÂZIR
    # ======================================================

    def test_emr_hazir(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_13,
            ),
            "أُنْصُرْ",
        )

    # ======================================================
    # 14 - NEHY-İ HÂZIR
    # ======================================================

    def test_nehy_hazir(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_14,
            ),
            "لَا تَنْصُرْ",
        )

    # ======================================================
    # 15 - İSM-İ ZAMAN / MEKÂN / MASTAR-I MÎMÎ
    # ======================================================

    def test_ismi_zaman_mekan(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_15,
            ),
            "مَنْصَرٌ",
        )

    # ======================================================
    # 16 - İSM-İ ÂLET
    # ======================================================

    def test_ismi_alet(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_16,
            ),
            "مِنْصَرٌ",
        )

    # ======================================================
    # 17 - MASTAR-I BİNÂ-İ MERRE
    # ======================================================

    def test_mastar_merre(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_17,
            ),
            "نَصْرَةً",
        )

    # ======================================================
    # 18 - MASTAR-I BİNÂ-İ NEV'
    # ======================================================

    def test_mastar_nev(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_18,
            ),
            "نِصْرَةً",
        )

    # ======================================================
    # 19 - İSM-İ TASĞÎR
    # ======================================================

    def test_ismi_tasgir(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_19,
            ),
            "نُصَيْرٌ",
        )

    # ======================================================
    # 20 - İSM-İ MENSUP
    # ======================================================

    def test_ismi_mensup_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_20,
            )

    # ======================================================
    # 21 - MÜBALAĞALI İSM-İ FÂİL
    # ======================================================

    def test_mubalaghali_ismi_fail(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_21,
            ),
            "نَصَّارٌ",
        )

    # ======================================================
    # 22 - İSM-İ TAFDİL
    # ======================================================

    def test_ismi_tafdil(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_22,
            ),
            "أَنْصَرُ",
        )

    # ======================================================
    # 23 - TA'ACCUP I
    # ======================================================

    def test_taccup_one(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_23,
            ),
            "مَا أَنْصَرَهُ",
        )

    # ======================================================
    # 24 - TA'ACCUP II
    # ======================================================

    def test_taccup_two(self):
        self.assertEqual(
            build_siga(
                self.nsr,
                BAB_1,
                SIGA_24,
            ),
            "أَنْصِرْ بِهِ",
        )

    # ======================================================
    # İ'LÂL ENTEGRASYON TESTLERİ
    #
    # Buradan itibaren mevcut sîga motorunun
    # illetli köklerle çalışması test edilir.
    # ======================================================

    # ======================================================
    # 25 - ECVEF VÂV MÂZÎ
    #
    # ق و ل
    #
    # قَوَلَ → قَالَ
    # ======================================================

    def test_qawl_mazi_qalb(self):
        self.assertEqual(
            build_siga(
                self.qwl,
                BAB_1,
                SIGA_01,
            ),
            "قَالَ",
        )

    # ======================================================
    # 26 - ECVEF VÂV MUZÂRİ
    #
    # ق و ل
    #
    # يَقْوُلُ → يَقُولُ
    # ======================================================

    def test_qawl_muzari(self):
        self.assertEqual(
            build_siga(
                self.qwl,
                BAB_1,
                SIGA_02,
            ),
            "يَقُولُ",
        )

    # ======================================================
    # 27 - ECVEF VÂV CAHD
    #
    # يَقُولُ → يَقُلْ
    # ======================================================

    def test_qawl_cahd(self):
        self.assertEqual(
            build_siga(
                self.qwl,
                BAB_1,
                SIGA_06,
            ),
            "لَمْ يَقُلْ",
        )

    # ======================================================
    # 28 - ECVEF VÂV EMİR
    #
    # يَقُولُ → قُلْ
    # ======================================================

    def test_qawl_emr_hazir(self):
        self.assertEqual(
            build_siga(
                self.qwl,
                BAB_1,
                SIGA_13,
            ),
            "قُلْ",
        )

    # ======================================================
    # 29 - ECVEF YÂ MÂZÎ
    #
    # بَيَعَ → بَاعَ
    # ======================================================

    def test_baya_mazi_qalb(self):
        self.assertEqual(
            build_siga(
                self.bya,
                BAB_1,
                SIGA_01,
            ),
            "بَاعَ",
        )

    # ======================================================
    # 30 - ECVEF YÂ MUZÂRİ
    #
    # يَبْيِعُ → يَبِيعُ
    # ======================================================

    def test_baya_muzari(self):
        self.assertEqual(
            build_siga(
                self.bya,
                BAB_1,
                SIGA_02,
            ),
            "يَبِيعُ",
        )

    # ======================================================
    # 31 - MUDÂAF MÂZÎ
    #
    # م د د
    #
    # مَدَدَ → مَدَّ
    # ======================================================

    def test_mudaf_mazi_idgam(self):
        self.assertEqual(
            build_siga(
                self.mdd,
                BAB_1,
                SIGA_01,
            ),
            "مَدَّ",
        )

    # ======================================================
    # 32 - MUDÂAF MUZÂRİ
    #
    # م د د
    #
    # يَمْدُدُ → يَمُدُّ
    # ======================================================

    def test_mudaf_muzari_idgam(self):
        self.assertEqual(
            build_siga(
                self.mdd,
                BAB_1,
                SIGA_02,
            ),
            "يَمُدُّ",
        )


if __name__ == "__main__":
    unittest.main()
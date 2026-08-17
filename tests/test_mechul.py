import unittest

from app.core.bab import BAB_1, BAB_2, BAB_3, BAB_4, BAB_5, BAB_6
from app.core.root import Root
from app.core.siga import SIGA_01, SIGA_02
from app.core.siga_engine import build_siga


class TestMechul(unittest.TestCase):

    # ======================================================
    # 1 - SAHİH FİİL
    #
    # ن ص ر
    #
    # نَصَرَ → نُصِرَ
    # يَنْصُرُ → يُنْصَرُ
    # ======================================================

    def test_nasara_mazi_passive(self):
        root = Root(
            "ن",
            "ص",
            "ر",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_01,
                voice="passive",
            ),
            "نُصِرَ",
        )

    def test_nasara_muzari_passive(self):
        root = Root(
            "ن",
            "ص",
            "ر",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_02,
                voice="passive",
            ),
            "يُنْصَرُ",
        )

    # ======================================================
    # 2 - م د ح
    #
    # 3. BÂB
    #
    # مَدَحَ → مُدِحَ
    # يَمْدَحُ → يُمْدَحُ
    # ======================================================

    def test_madaha_mazi_passive(self):
        root = Root(
            "م",
            "د",
            "ح",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_3,
                SIGA_01,
                voice="passive",
            ),
            "مُدِحَ",
        )

    def test_madaha_muzari_passive(self):
        root = Root(
            "م",
            "د",
            "ح",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_3,
                SIGA_02,
                voice="passive",
            ),
            "يُمْدَحُ",
        )

    # ======================================================
    # 3 - و ع د
    #
    # 2. BÂB — MİSÂL-İ VÂVÎ
    #
    # وَعَدَ → وُعِدَ
    # يَعِدُ → يُوعَدُ
    #
    # Mâzî meçhul:
    # Vâv korunur.
    #
    # Muzâri meçhul:
    # Malumda düşen vâv geri gelir.
    # ======================================================

    def test_waada_mazi_passive(self):
        root = Root(
            "و",
            "ع",
            "د",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_2,
                SIGA_01,
                voice="passive",
            ),
            "وُعِدَ",
        )

    def test_waada_muzari_passive(self):
        root = Root(
            "و",
            "ع",
            "د",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_2,
                SIGA_02,
                voice="passive",
            ),
            "يُوعَدُ",
        )

    # ======================================================
    # 4 - ي س ر
    #
    # 2. BÂB — MİSÂL-İ YÂÎ
    #
    # يَسَرَ → يُسِرَ
    # يُيْسَرُ → يُوسَرُ
    #
    # Sakin yâ, kendisinden önce damme bulunduğu için
    # vâva kalb edilir.
    # ======================================================

    def test_yasara_mazi_passive(self):
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
                voice="passive",
            ),
            "يُسِرَ",
        )

    def test_yasara_muzari_passive(self):
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
                voice="passive",
            ),
            "يُوسَرُ",
        )

    # ======================================================
    # 5 - ق و ل
    #
    # 1. BÂB — ECVEF VÂVÎ
    #
    # قَالَ → قِيلَ
    # يَقُولُ → يُقَالُ
    #
    # Mâzî meçhul:
    # قُوِلَ
    # ↓
    # قِيلَ
    #
    # Muzâri meçhul:
    # يُقْوَلُ
    # ↓
    # يُقَالُ
    #
    # Nakl-i hareke + kalb-i illet.
    # ======================================================

    def test_qala_mazi_passive(self):
        root = Root(
            "ق",
            "و",
            "ل",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_01,
                voice="passive",
            ),
            "قِيلَ",
        )

    def test_qala_muzari_passive(self):
        root = Root(
            "ق",
            "و",
            "ل",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_02,
                voice="passive",
            ),
            "يُقَالُ",
        )

    # ======================================================
    # 6 - ب ي ع
    #
    # 1. BÂB — ECVEF YÂÎ
    #
    # بَاعَ → بِيعَ
    # يَبِيعُ → يُبَاعُ
    #
    # Mâzî meçhul:
    # بُيِعَ
    # ↓
    # بِيعَ
    #
    # Muzâri meçhul:
    # يُبْيَعُ
    # ↓
    # يُبَاعُ
    #
    # Nakl-i hareke + kalb-i illet.
    # ======================================================

    def test_baia_mazi_passive(self):
        root = Root(
            "ب",
            "ي",
            "ع",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_01,
                voice="passive",
            ),
            "بِيعَ",
        )

    def test_baia_muzari_passive(self):
        root = Root(
            "ب",
            "ي",
            "ع",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_1,
                SIGA_02,
                voice="passive",
            ),
            "يُبَاعُ",
        )


if __name__ == "__main__":
    unittest.main()
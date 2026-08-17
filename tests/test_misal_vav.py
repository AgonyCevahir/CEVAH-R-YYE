import unittest

from app.core.bab import BAB_2, BAB_3, BAB_4
from app.core.root import Root
from app.core.siga import SIGA_01, SIGA_02
from app.core.siga_engine import build_siga


class TestMisalVavIlal(unittest.TestCase):

    # ======================================================
    # 1 - و ع د
    #
    # 2. BÂB
    #
    # وَعَدَ → يَعِدُ
    #
    # Mâzîde vâv korunur.
    # Muzârî malumda vâv hazfedilir.
    # ======================================================

    def test_waada_mazi(self):
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
            ),
            "وَعَدَ",
        )

    def test_waada_muzari(self):
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
            ),
            "يَعِدُ",
        )

    # ======================================================
    # 2 - و ه ب
    #
    # 3. BÂB
    #
    # وَهَبَ → يَهَبُ
    #
    # Mâzîde vâv korunur.
    # Muzârî malumda vâv hazfedilir.
    #
    # Aynü'l-fiil olan ه harfi boğaz harfidir.
    # ======================================================

    def test_wahaba_mazi(self):
        root = Root(
            "و",
            "ه",
            "ب",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_3,
                SIGA_01,
            ),
            "وَهَبَ",
        )

    def test_wahaba_muzari(self):
        root = Root(
            "و",
            "ه",
            "ب",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_3,
                SIGA_02,
            ),
            "يَهَبُ",
        )

    # ======================================================
    # 3 - و ج ل
    #
    # 4. BÂB
    #
    # وَجِلَ → يَوْجَلُ
    #
    # Mâzîsi kesralıdır.
    # Muzârîsi fethalıdır.
    # Bu bâbda vâv hazfedilmez.
    # ======================================================

    def test_wajila_mazi(self):
        root = Root(
            "و",
            "ج",
            "ل",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_4,
                SIGA_01,
            ),
            "وَجِلَ",
        )

    def test_wajila_muzari(self):
        root = Root(
            "و",
            "ج",
            "ل",
        )

        self.assertEqual(
            build_siga(
                root,
                BAB_4,
                SIGA_02,
            ),
            "يَوْجَلُ",
        )


if __name__ == "__main__":
    unittest.main()
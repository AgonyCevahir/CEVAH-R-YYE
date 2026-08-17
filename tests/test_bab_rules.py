import unittest

from app.core.bab import BAB_3
from app.core.bab_rules import (
    has_throat_letter_for_bab_3,
    is_bab_3_exception,
    is_valid_for_bab_3,
    is_root_valid_for_bab,
)
from app.core.root import Root


class TestBabRules(unittest.TestCase):

    # ========================================================
    # NORMAL BÂB 3 KURALI
    # ========================================================

    def test_bab_3_valid_when_second_letter_is_throat_letter(self):
        root = Root(
            "م",
            "ح",
            "د",
        )

        self.assertTrue(
            has_throat_letter_for_bab_3(root)
        )

        self.assertTrue(
            is_valid_for_bab_3(root)
        )

    def test_bab_3_valid_when_third_letter_is_throat_letter(self):
        root = Root(
            "م",
            "د",
            "ح",
        )

        self.assertTrue(
            has_throat_letter_for_bab_3(root)
        )

        self.assertTrue(
            is_valid_for_bab_3(root)
        )

    # ========================================================
    # BOĞAZ HARFİ YOKSA GEÇERSİZ
    # ========================================================

    def test_bab_3_invalid_without_throat_letter(self):
        root = Root(
            "ك",
            "ت",
            "ب",
        )

        self.assertFalse(
            has_throat_letter_for_bab_3(root)
        )

        self.assertFalse(
            is_valid_for_bab_3(root)
        )

    # ========================================================
    # أَبَى İSTİSNASI
    # ========================================================

    def test_abaa_exception(self):
        root = Root(
            "أ",
            "ب",
            "ي",
        )

        self.assertFalse(
            has_throat_letter_for_bab_3(root)
        )

        self.assertTrue(
            is_bab_3_exception(root)
        )

        self.assertTrue(
            is_valid_for_bab_3(root)
        )

    # ========================================================
    # GENEL BÂB KONTROLÜ
    # ========================================================

    def test_bab_3_general_validation(self):
        root = Root(
            "م",
            "د",
            "ح",
        )

        self.assertTrue(
            is_root_valid_for_bab(
                root,
                BAB_3,
            )
        )

    def test_other_babs_are_valid_by_default(self):
        root = Root(
            "ك",
            "ت",
            "ب",
        )

        # Şimdilik yalnızca Bâb 3'ün özel şartı vardır.
        # Diğer bâblar için burada özel kök şartı
        # uygulanmamaktadır.

        from app.core.bab import BAB_1

        self.assertTrue(
            is_root_valid_for_bab(
                root,
                BAB_1,
            )
        )


if __name__ == "__main__":
    unittest.main()
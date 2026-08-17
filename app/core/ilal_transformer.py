from __future__ import annotations

from app.core.ilal import (
    IlalResult,
    apply_ilal_rule,
)


# ============================================================
# ARAPÇA HAREKELER
# ============================================================

ARABIC_VOWELS = (
    "َ",   # fetha
    "ُ",   # damme
    "ِ",   # kesra
    "ْ",   # cezm
    "ّ",   # şedde
    "ً",   # fethateyn
    "ٌ",   # dammeteyn
    "ٍ",   # kesrateyn
)


WEAK_LETTERS = (
    "و",
    "ي",
    "ى",
)


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def is_vowel(char: str) -> bool:
    """
    Karakterin Arapça hareke işareti olup olmadığını kontrol eder.
    """

    return char in ARABIC_VOWELS


def previous_letter_index(
    word: str,
    index: int,
) -> int:
    """
    Verilen konumdan önceki gerçek harfin indeksini bulur.

    Örnek:

        يَقْوُ
        0 1 2 3 4 5

        vâv = 4
        önceki gerçek harf = ق = 2
    """

    position = index - 1

    while position >= 0:
        if not is_vowel(word[position]):
            return position

        position -= 1

    return -1


def next_vowel_index(
    word: str,
    index: int,
) -> int:
    """
    Verilen gerçek harften sonra gelen ilk harekenin
    indeksini bulur.
    """

    position = index + 1

    while position < len(word):

        if is_vowel(word[position]):
            return position

        # Başka bir gerçek harfe ulaşıldıysa,
        # bu harfin üzerinde hareke yoktur.
        return -1

    return -1


def remove_vowels_after_letter(
    word: str,
    letter_index: int,
) -> str:
    """
    Verilen gerçek harfin hemen arkasındaki bütün
    hareke işaretlerini kaldırır.
    """

    result = word
    position = letter_index + 1

    while position < len(result):

        if not is_vowel(result[position]):
            break

        result = (
            result[:position]
            + result[position + 1:]
        )

    return result


# ============================================================
# İ'LÂL TRANSFORMER
# ============================================================

class IlalTransformer:
    """
    Gerçek Arapça kelimeler üzerinde temel i'lâl
    dönüşümlerini gerçekleştirir.

    Kapsanan işlemler:

        - Kalb
        - Hazf
        - İskân
        - Nakl-i hareke
    """

    # ========================================================
    # KALB — VÂV → ELİF
    # ========================================================

    @staticmethod
    def qalb_vav_to_alif(
        word: str,
        vav_index: int,
    ) -> IlalResult:
        """
        Vâvı elif'e çevirir.

        Örnek:

            قَوَلَ
            ↓
            قَالَ
        """

        if not 0 <= vav_index < len(word):
            raise IndexError(
                "Vâv konumu kelimenin sınırları dışında."
            )

        if word[vav_index] != "و":
            raise ValueError(
                "Belirtilen konumda vâv harfi bulunmuyor."
            )

        # Vâvı elif ile değiştir.
        result = (
            word[:vav_index]
            + "ا"
            + word[vav_index + 1:]
        )

        # Vâvın üzerinde bulunan eski harekeyi kaldır.
        result = remove_vowels_after_letter(
            result,
            vav_index,
        )

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="Kalb: vâv → elif",
        )

    # ========================================================
    # KALB — YÂ → ELİF
    # ========================================================

    @staticmethod
    def qalb_ya_to_alif(
        word: str,
        ya_index: int,
    ) -> IlalResult:
        """
        Yâyı elif'e çevirir.

        Örnek:

            بَيَعَ
            ↓
            بَاعَ
        """

        if not 0 <= ya_index < len(word):
            raise IndexError(
                "Yâ konumu kelimenin sınırları dışında."
            )

        if word[ya_index] != "ي":
            raise ValueError(
                "Belirtilen konumda yâ harfi bulunmuyor."
            )

        # Yâyı elif ile değiştir.
        result = (
            word[:ya_index]
            + "ا"
            + word[ya_index + 1:]
        )

        # Yânın üzerindeki eski harekeyi kaldır.
        result = remove_vowels_after_letter(
            result,
            ya_index,
        )

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="Kalb: yâ → elif",
        )

    # ========================================================
    # KALB — YÂ → VÂV
    # ========================================================

    @staticmethod
    def qalb_ya_to_vav(
        word: str,
        ya_index: int,
    ) -> IlalResult:
        """
        Sâkin yânın, kendisinden önceki gerçek harf
        dammeli olduğunda vâva dönüşmesini sağlar.

        Kitaptaki misâl-i yâî örneği:

            يُيْسَرُ
            ↓
            يُوسَرُ

        Şartlar:

            - Belirtilen konumda yâ bulunmalı.
            - Yâ sâkin olmalı.
            - Yâdan önceki gerçek harfin harekesi
              damme olmalı.
        """

        # ----------------------------------------------------
        # İndeks kontrolü
        # ----------------------------------------------------

        if not 0 <= ya_index < len(word):
            raise IndexError(
                "Yâ konumu kelimenin sınırları dışında."
            )

        # ----------------------------------------------------
        # Yâ kontrolü
        # ----------------------------------------------------

        if word[ya_index] != "ي":
            raise ValueError(
                "Belirtilen konumda yâ harfi bulunmuyor."
            )

        # ----------------------------------------------------
        # Yânın harekesini bul
        # ----------------------------------------------------

        ya_vowel_index = next_vowel_index(
            word,
            ya_index,
        )

        if ya_vowel_index == -1:
            raise ValueError(
                "Yânın harekesi bulunamadı."
            )

        # Yâ mutlaka sakin olmalı.
        if word[ya_vowel_index] != "ْ":
            raise ValueError(
                "Kalb-i yâ → vâv için yânın sakin olması gerekir."
            )

        # ----------------------------------------------------
        # Önceki gerçek harfi bul
        # ----------------------------------------------------

        previous_index = previous_letter_index(
            word,
            ya_index,
        )

        if previous_index == -1:
            raise ValueError(
                "Yâ harfinden önce gerçek bir harf bulunamadı."
            )

        # ----------------------------------------------------
        # Önceki harfin harekesini bul
        # ----------------------------------------------------

        previous_vowel_index = next_vowel_index(
            word,
            previous_index,
        )

        if previous_vowel_index == -1:
            raise ValueError(
                "Yâdan önceki harfin harekesi bulunamadı."
            )

        # Önceki harf dammeli olmalı.
        if word[previous_vowel_index] != "ُ":
            raise ValueError(
                "Kalb-i yâ → vâv için önceki harfin "
                "damme olması gerekir."
            )

        # ----------------------------------------------------
        # YÂ → VÂV
        # ----------------------------------------------------

        result = (
            word[:ya_index]
            + "و"
            + word[ya_index + 1:]
        )

        # Yânın sükûnunu kaldır.
        result = remove_vowels_after_letter(
            result,
            ya_index,
        )

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="Kalb: sâkin yâ → vâv",
        )

    # ========================================================
    # HAZF — SON İLLET HARFİ
    # ========================================================

    @staticmethod
    def delete_final_weak(
        word: str,
    ) -> IlalResult:
        """
        Kelimenin sonundaki illet harfini düşürür.

        Örnek:

            يَدْعُو → يَدْعُ
            يَرْمِي → يَرْمِ
            يَسْعَى → يَسْعَ
        """

        if not word:
            raise ValueError(
                "Boş kelimede hazf uygulanamaz."
            )

        # Son gerçek harfi bul.
        index = len(word) - 1

        while index >= 0 and is_vowel(word[index]):
            index -= 1

        if index < 0:
            raise ValueError(
                "Kelime içinde gerçek harf bulunmuyor."
            )

        if word[index] not in WEAK_LETTERS:
            raise ValueError(
                "Kelimenin son harfi illet harfi değil."
            )

        # İllet harfini ve arkasındaki varsa harekeleri kaldır.
        result = word[:index]

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="Hazf: son illet harfi düşürüldü",
        )

    # ========================================================
    # İSKÂN
    # ========================================================

    @staticmethod
    def remove_final_vowel_mark(
        word: str,
    ) -> IlalResult:
        """
        Kelimenin sonundaki harekeyi kaldırır.
        """

        if not word:
            raise ValueError(
                "Boş kelimede iskân uygulanamaz."
            )

        if not is_vowel(word[-1]):
            return apply_ilal_rule(
                original=word,
                result=word,
                rule="İskân: uygulanacak son hareke bulunamadı",
            )

        result = word[:-1]

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="İskân: son hareke kaldırıldı",
        )

    # ========================================================
    # NAKL-İ HAREKE
    # ========================================================

    @staticmethod
    def transfer_vowel(
        word: str,
        weak_index: int,
        vowel: str,
    ) -> IlalResult:
        """
        İllet harfinin harekesini kendisinden önceki
        gerçek harfe aktarır.

        Örnek:

            يَقْوُ
            ↓
            يَقُو

        Yani:

            قْ + وُ
            ↓
            قُ + و
        """

        # ----------------------------------------------------
        # İndeks kontrolü
        # ----------------------------------------------------

        if not 0 <= weak_index < len(word):
            raise IndexError(
                "İllet harfi konumu kelimenin sınırları dışında."
            )

        # ----------------------------------------------------
        # İllet harfi kontrolü
        # ----------------------------------------------------

        weak_letter = word[weak_index]

        if weak_letter not in WEAK_LETTERS:
            raise ValueError(
                "Belirtilen konumda illet harfi bulunmuyor."
            )

        if weak_index == 0:
            raise ValueError(
                "İlk harfteki illet harfinin harekesi "
                "önceki harfe aktarılamaz."
            )

        # ----------------------------------------------------
        # Hareke kontrolü
        # ----------------------------------------------------

        if vowel not in (
            "َ",
            "ُ",
            "ِ",
        ):
            raise ValueError(
                "Nakl-i hareke için geçerli bir hareke "
                "belirtilmelidir."
            )

        # ----------------------------------------------------
        # İllet harfinin harekesini bul
        # ----------------------------------------------------

        weak_vowel_index = next_vowel_index(
            word,
            weak_index,
        )

        if weak_vowel_index == -1:
            raise ValueError(
                "İllet harfinin harekesi bulunamadı."
            )

        if word[weak_vowel_index] != vowel:
            raise ValueError(
                "Belirtilen hareke illet harfinin üzerinde değil."
            )

        # ----------------------------------------------------
        # Önceki GERÇEK harfi bul
        # ----------------------------------------------------

        previous_index = previous_letter_index(
            word,
            weak_index,
        )

        if previous_index == -1:
            raise ValueError(
                "İllet harfinden önce gerçek bir harf bulunamadı."
            )

        # ====================================================
        # SONUCU ORİJİNAL KELİMEDEN TEK SEFERDE OLUŞTUR
        # ====================================================

        result_parts = []

        # Önceki gerçek harfe kadar olan kısmı al.
        result_parts.append(
            word[:previous_index + 1]
        )

        # Önceki harfin mevcut harekelerini atla.
        position = previous_index + 1

        while position < weak_index:
            if is_vowel(word[position]):
                position += 1
                continue

            break

        # Yeni harekeyi önceki gerçek harfe ekle.
        result_parts.append(vowel)

        # İllet harfine kadar kalan gerçek/hareke yapısını
        # koru.
        result_parts.append(
            word[position:weak_vowel_index]
        )

        # İllet harfinin harekesini atla.
        result_parts.append(
            word[weak_vowel_index + 1:]
        )

        result = "".join(result_parts)

        return apply_ilal_rule(
            original=word,
            result=result,
            rule="Nakl-i hareke: illet harfinin harekesi önceki harfe aktarıldı",
        )


# ============================================================
# TEK MERKEZDEN ERİŞİM
# ============================================================

ILAL_TRANSFORMER = IlalTransformer()
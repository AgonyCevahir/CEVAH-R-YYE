from app.core.bab import Bab
from app.core.bab_rules import is_root_valid_for_bab
from app.core.ilal import is_weak_letter
from app.core.ilal_transformer import IlalTransformer
from app.core.pattern import apply_pattern
from app.core.root import Root
from app.models.verb import Verb


# ============================================================
# ARAPÇA HAREKELER
# ============================================================

ARABIC_VOWELS = (
    "َ",
    "ُ",
    "ِ",
    "ْ",
    "ّ",
    "ً",
    "ٌ",
    "ٍ",
)


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def _is_vowel(char: str) -> bool:
    """
    Karakterin Arapça hareke olup olmadığını kontrol eder.
    """

    return char in ARABIC_VOWELS


def _find_root_letter_index(
    word: str,
    root_letter: str,
    start: int = 0,
) -> int:
    """
    Kelimede belirli bir kök harfinin gerçek konumunu bulur.
    """

    position = start

    while position < len(word):

        if word[position] == root_letter:
            return position

        position += 1

    return -1


def _find_previous_letter_index(
    word: str,
    index: int,
) -> int:
    """
    Verilen konumdan önceki gerçek Arapça harfin indeksini bulur.
    """

    position = index - 1

    while position >= 0:

        if not _is_vowel(word[position]):
            return position

        position -= 1

    return -1


def _find_vowel_after_letter(
    word: str,
    letter_index: int,
) -> tuple[int, str]:
    """
    Verilen gerçek harfin hemen sonrasındaki harekeyi bulur.

    Sonuç:

        (indeks, hareke)

    Bulamazsa:

        (-1, "")
    """

    position = letter_index + 1

    while position < len(word):

        if _is_vowel(word[position]):
            return position, word[position]

        if not _is_vowel(word[position]):
            return -1, ""

        position += 1

    return -1, ""


def _replace_vowel_after_letter(
    word: str,
    letter_index: int,
    new_vowel: str,
) -> str:
    """
    Bir gerçek harfin hemen arkasındaki harekeyi değiştirir.
    """

    vowel_index, _ = _find_vowel_after_letter(
        word,
        letter_index,
    )

    if vowel_index == -1:
        return (
            word[:letter_index + 1]
            + new_vowel
            + word[letter_index + 1:]
        )

    return (
        word[:vowel_index]
        + new_vowel
        + word[vowel_index + 1:]
    )


def _remove_vowel_after_letter(
    word: str,
    letter_index: int,
) -> str:
    """
    Bir gerçek harfin hemen arkasındaki harekeyi kaldırır.
    """

    vowel_index, _ = _find_vowel_after_letter(
        word,
        letter_index,
    )

    if vowel_index == -1:
        return word

    return (
        word[:vowel_index]
        + word[vowel_index + 1:]
    )


# ============================================================
# MÂZÎ İ'LÂLİ
# ============================================================

def _apply_past_ilal(
    word: str,
    root: Root,
) -> str:
    """
    Mâzî fiilde temel kalb dönüşümünü uygular.

    Ecvef vâv:

        قَوَلَ → قَالَ

    Ecvef yâ:

        بَيَعَ → بَاعَ
    """

    if not is_weak_letter(root.ayn):
        return word

    weak_index = _find_root_letter_index(
        word,
        root.ayn,
    )

    if weak_index == -1:
        return word

    previous_index = _find_previous_letter_index(
        word,
        weak_index,
    )

    if previous_index == -1:
        return word

    _, previous_vowel = _find_vowel_after_letter(
        word,
        previous_index,
    )

    _, weak_vowel = _find_vowel_after_letter(
        word,
        weak_index,
    )

    if (
        previous_vowel != "َ"
        or weak_vowel == ""
    ):
        return word

    # --------------------------------------------------------
    # VÂV → ELİF
    # --------------------------------------------------------

    if root.ayn == "و":

        result = IlalTransformer.qalb_vav_to_alif(
            word,
            weak_index,
        )

        return result.result

    # --------------------------------------------------------
    # YÂ → ELİF
    # --------------------------------------------------------

    if root.ayn == "ي":

        result = IlalTransformer.qalb_ya_to_alif(
            word,
            weak_index,
        )

        return result.result

    return word


# ============================================================
# MİSÂL-İ VÂVÎ — MUZÂRİ İ'LÂLİ
# ============================================================

def _apply_misal_vav_present(
    word: str,
    root: Root,
    bab: Bab,
) -> str:
    """
    Misâl-i vâvî fiillerin muzâri malumunda
    kitapta belirtilen vâv hazfini uygular.

    Kitaptaki temel örnekler:

        II. Bâb:
            وَعَدَ → يَوْعِدُ → يَعِدُ

        III. Bâb:
            وَهَبَ → يَوْهَبُ → يَهَبُ

        IV. Bâb:
            وَجِلَ → يَوْجَلُ
            vâv korunur.

    Kurala göre:

        II. Bâbda aynü'l-fiil kesralıysa vâv hazfedilir.
        III. Bâbda aynü'l-fiil fethalıysa vâv hazfedilir.
        IV. Bâbda vâv korunur.
    """

    # --------------------------------------------------------
    # MİSÂL-İ VÂVÎ ŞARTI
    # --------------------------------------------------------

    if root.fa != "و":
        return word

    # --------------------------------------------------------
    # ŞU AŞAMADA SADECE MUZÂRİ MALUMUN
    # BİLİNEN HAZF KURALLARI
    # --------------------------------------------------------

    # Bâb 2 ve Bâb 3'te vâv hazfedilir.
    #
    # Bâb 4'te korunur.
    if bab.number not in (2, 3):
        return word

    # --------------------------------------------------------
    # İLK KÖK HARFİ VÂVIN KONUMUNU BUL
    # --------------------------------------------------------

    root_fa_index = _find_root_letter_index(
        word,
        root.fa,
    )

    if root_fa_index == -1:
        return word

    # --------------------------------------------------------
    # VÂVIN HAREKESİ
    # --------------------------------------------------------

    vav_vowel_index, vav_vowel = (
        _find_vowel_after_letter(
            word,
            root_fa_index,
        )
    )

    # Vâvın sakin olması gerekir.
    if (
        vav_vowel_index == -1
        or vav_vowel != "ْ"
    ):
        return word

    # --------------------------------------------------------
    # AYNÜ'L-FİİLİ BUL
    # --------------------------------------------------------

    ayn_index = _find_root_letter_index(
        word,
        root.ayn,
        root_fa_index + 1,
    )

    if ayn_index == -1:
        return word

    # --------------------------------------------------------
    # AYNÜ'L-FİİLİN HAREKESİNİ BUL
    # --------------------------------------------------------

    ayn_vowel_index, ayn_vowel = (
        _find_vowel_after_letter(
            word,
            ayn_index,
        )
    )

    if ayn_vowel_index == -1:
        return word

    # --------------------------------------------------------
    # BÂB 2
    #
    # وَعَدَ
    # يَوْعِدُ
    #     ↑
    #     kesra
    #
    # Vâv hazfedilir.
    # --------------------------------------------------------

    if bab.number == 2:

        if ayn_vowel != "ِ":
            return word

        result = (
            word[:root_fa_index]
            + word[vav_vowel_index + 1:]
        )

        return result

    # --------------------------------------------------------
    # BÂB 3
    #
    # وَهَبَ
    # يَوْهَبُ
    #     ↑
    #     fetha
    #
    # Vâv hazfedilir.
    # --------------------------------------------------------

    if bab.number == 3:

        if ayn_vowel != "َ":
            return word

        result = (
            word[:root_fa_index]
            + word[vav_vowel_index + 1:]
        )

        return result

    return word


# ============================================================
# MUZÂRİ İ'LÂLİ
# ============================================================

def _apply_present_ilal(
    word: str,
    root: Root,
    bab: Bab,
) -> str:
    """
    Muzâri fiilde temel i'lâl işlemlerini uygular.

    Kapsanan yapılar:

        1. Misâl-i vâvî
        2. Ecvef yâ
        3. Ecvef vâv
    """

    # ========================================================
    # 1. MİSÂL-İ VÂVÎ
    # ========================================================

    if root.fa == "و":

        return _apply_misal_vav_present(
            word,
            root,
            bab,
        )

    # ========================================================
    # 2. ECVEF KONTROLÜ
    # ========================================================

    if not is_weak_letter(root.ayn):
        return word

    # --------------------------------------------------------
    # Kök harflerinin gerçek konumlarını bul.
    # --------------------------------------------------------

    root_letters = (
        root.fa,
        root.ayn,
        root.lam,
    )

    positions = []

    search_from = 0

    for root_letter in root_letters:

        found = _find_root_letter_index(
            word,
            root_letter,
            search_from,
        )

        if found == -1:
            return word

        positions.append(found)
        search_from = found + 1

    weak_index = positions[1]

    if word[weak_index] != root.ayn:
        return word

    # --------------------------------------------------------
    # İllet harfinin harekesini bul.
    # --------------------------------------------------------

    weak_vowel_index, weak_vowel = (
        _find_vowel_after_letter(
            word,
            weak_index,
        )
    )

    if weak_vowel_index == -1:
        return word

    # --------------------------------------------------------
    # Önceki gerçek harfi bul.
    # --------------------------------------------------------

    previous_index = _find_previous_letter_index(
        word,
        weak_index,
    )

    if previous_index == -1:
        return word

    # ========================================================
    # ECVEF YÂ
    # ========================================================

    if root.ayn == "ي":

        if weak_vowel == "ُ":

            # Önceki harfin mevcut harekesini kaldır.
            result = _remove_vowel_after_letter(
                word,
                previous_index,
            )

            # İllet harfinin konumu değiştiği için
            # yâyı yeniden bul.
            weak_index = _find_root_letter_index(
                result,
                root.ayn,
                previous_index + 1,
            )

            if weak_index == -1:
                return word

            # Yânın harekesini kaldır.
            result = _remove_vowel_after_letter(
                result,
                weak_index,
            )

            # Önceki gerçek harfi yeniden bul.
            previous_index = _find_previous_letter_index(
                result,
                weak_index,
            )

            if previous_index == -1:
                return word

            # Önceki harfe kesra ekle.
            result = _replace_vowel_after_letter(
                result,
                previous_index,
                "ِ",
            )

            return result

        # Yânın üzerinde zaten kesra varsa
        # doğrudan nakl-i hareke uygula.
        if weak_vowel == "ِ":

            result = IlalTransformer.transfer_vowel(
                word,
                weak_index,
                weak_vowel,
            )

            return result.result

        return word

    # ========================================================
    # ECVEF VÂV
    # ========================================================

    if root.ayn == "و":

        if weak_vowel not in (
            "َ",
            "ُ",
            "ِ",
        ):
            return word

        result = IlalTransformer.transfer_vowel(
            word,
            weak_index,
            weak_vowel,
        )

        return result.result

    return word


# ============================================================
# ANA VERB ENGINE
# ============================================================

def build_verb(
    root: Root,
    bab: Bab,
) -> Verb:
    """
    Verilen kök ve bâb bilgisine göre mâzî ve muzâri fiili
    oluşturur.

    Üretim sırası:

        1. Bâb uygunluğu
        2. Temel mâzî
        3. Temel muzâri
        4. Mâzî i'lâli
        5. Muzâri i'lâli
        6. Verb nesnesi
    """

    # ========================================================
    # BÂB KURALLARI
    # ========================================================

    if not is_root_valid_for_bab(
        root,
        bab,
    ):
        raise ValueError(
            f"Kök ({root.text}) {bab.number}. bâb "
            f"({bab.name}) için uygun değildir."
        )

    # ========================================================
    # TEMEL MÂZÎ
    # ========================================================

    past = apply_pattern(
        bab.past_pattern,
        root,
    )

    # ========================================================
    # TEMEL MUZÂRİ
    # ========================================================

    present = apply_pattern(
        bab.present_pattern,
        root,
    )

    # ========================================================
    # MÂZÎ İ'LÂL
    # ========================================================

    past = _apply_past_ilal(
        past,
        root,
    )

    # ========================================================
    # MUZÂRİ İ'LÂL
    # ========================================================

    present = _apply_present_ilal(
        present,
        root,
        bab,
    )

    # ========================================================
    # VERB NESNESİ
    # ========================================================

    return Verb(
        root=root,
        bab=bab,
        past=past,
        present=present,
    )
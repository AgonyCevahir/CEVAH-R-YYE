from app.core.bab import Bab
from app.core.pattern import apply_pattern
from app.core.root import Root
from app.core.siga import Siga
from app.core.verb_engine import build_verb
from app.core.ilal_transformer import IlalTransformer


# ============================================================
# ARAPÇA HAREKELER
# ============================================================

HAREKELER = (
    "َ",
    "ُ",
    "ِ",
    "ْ",
    "ً",
    "ٌ",
    "ٍ",
)


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def _is_hareke(char: str) -> bool:
    """
    Verilen karakterin Arapça hareke işareti olup olmadığını
    kontrol eder.
    """

    return char in HAREKELER


def _remove_final_hareke(
    word: str,
) -> str:
    """
    Kelimenin sonundaki harekeyi kaldırır.
    """

    if not word:
        return word

    if _is_hareke(word[-1]):
        return word[:-1]

    return word


def _put_final_hareke(
    word: str,
    hareke: str,
) -> str:
    """
    Kelimenin son harekesini verilen harekeyle değiştirir.
    """

    word = _remove_final_hareke(word)

    return word + hareke


def _find_root_positions(
    word: str,
    root: Root,
) -> tuple[int, int, int] | None:
    """
    Kökün üç harfinin kelimedeki gerçek konumlarını bulur.

    Hareke karakterleri kök harfi olarak değerlendirilmez.
    """

    positions = []
    search_from = 0

    for root_letter in (
        root.fa,
        root.ayn,
        root.lam,
    ):
        found = -1

        for index in range(
            search_from,
            len(word),
        ):
            if word[index] == root_letter:
                found = index
                break

        if found == -1:
            return None

        positions.append(found)
        search_from = found + 1

    return (
        positions[0],
        positions[1],
        positions[2],
    )


def _find_letter_after(
    word: str,
    letter: str,
    start: int = 0,
) -> int:
    """
    Belirtilen başlangıç konumundan sonra verilen gerçek
    harfi bulur.
    """

    for index in range(
        start,
        len(word),
    ):
        if word[index] == letter:
            return index

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

    vowel_index = letter_index + 1

    if (
        vowel_index < len(word)
        and _is_hareke(word[vowel_index])
    ):
        return (
            vowel_index,
            word[vowel_index],
        )

    return (
        -1,
        "",
    )


def _remove_vowel_after_letter(
    word: str,
    letter_index: int,
) -> str:
    """
    Verilen gerçek harfin hemen arkasındaki harekeyi kaldırır.
    """

    vowel_index = letter_index + 1

    if (
        vowel_index < len(word)
        and _is_hareke(word[vowel_index])
    ):
        return (
            word[:vowel_index]
            + word[vowel_index + 1:]
        )

    return word


def _replace_vowel_after_letter(
    word: str,
    letter_index: int,
    new_vowel: str,
) -> str:
    """
    Verilen gerçek harfin hemen arkasındaki harekeyi değiştirir.
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


# ============================================================
# ECVEF — MÂZÎ MEÇHUL İ'LÂLİ
# ============================================================

def _apply_hollow_past_passive_ilal(
    word: str,
    root: Root,
) -> str:
    """
    Ecvef fiilin mâzî meçhulündeki i'lâli uygular.

    Vâvî:

        قُوِلَ
        ↓
        قِيلَ

    Yâî:

        بُيِعَ
        ↓
        بِيعَ

    İşlem sırası:

        1. İllet harfinin üzerindeki kesra kaldırılır.
        2. Kesra fâu'l-fiile aktarılır.
        3. Sakin kalan illet harfi yâya çevrilir.
    """

    if root.ayn not in (
        "و",
        "ي",
    ):
        return word

    positions = _find_root_positions(
        word,
        root,
    )

    if positions is None:
        return word

    fa_index, weak_index, _ = positions

    # --------------------------------------------------------
    # İllet harfinin harekesini bul.
    # --------------------------------------------------------

    weak_vowel_index, weak_vowel = (
        _find_vowel_after_letter(
            word,
            weak_index,
        )
    )

    if (
        weak_vowel_index == -1
        or weak_vowel != "ِ"
    ):
        return word

    # --------------------------------------------------------
    # 1. İllet harfinin üzerindeki kesrayı kaldır.
    # --------------------------------------------------------

    result = _remove_vowel_after_letter(
        word,
        weak_index,
    )

    # --------------------------------------------------------
    # 2. Fâu'l-fiilin mevcut harekesini kaldır.
    # --------------------------------------------------------

    fa_index = _find_letter_after(
        result,
        root.fa,
    )

    if fa_index == -1:
        return word

    result = _remove_vowel_after_letter(
        result,
        fa_index,
    )

    # --------------------------------------------------------
    # 3. Kesrayı fâu'l-fiile aktar.
    # --------------------------------------------------------

    result = _replace_vowel_after_letter(
        result,
        fa_index,
        "ِ",
    )

    # --------------------------------------------------------
    # 4. İllet harfini yâya çevir.
    #
    # قُوِلَ → قِيلَ
    # بُيِعَ → بِيعَ
    # --------------------------------------------------------

    weak_index = _find_letter_after(
        result,
        root.ayn,
        fa_index + 1,
    )

    if weak_index == -1:
        return result

    result = (
        result[:weak_index]
        + "ي"
        + result[weak_index + 1:]
    )

    return result


# ============================================================
# ECVEF — MUZÂRİ MEÇHUL İ'LÂLİ
# ============================================================

def _apply_hollow_present_passive_ilal(
    word: str,
    root: Root,
) -> str:
    """
    Ecvef fiilin muzâri meçhulündeki i'lâli uygular.

    Vâvî:

        يُقْوَلُ
        ↓
        يُقَالُ

    Yâî:

        يُبْيَعُ
        ↓
        يُبَاعُ

    İşlem sırası:

        1. İllet harfinin üzerindeki fetha kaldırılır.
        2. Fetha fâu'l-fiile aktarılır.
        3. Sakin kalan illet harfi elife çevrilir.
    """

    if root.ayn not in (
        "و",
        "ي",
    ):
        return word

    positions = _find_root_positions(
        word,
        root,
    )

    if positions is None:
        return word

    fa_index, weak_index, _ = positions

    # --------------------------------------------------------
    # İllet harfinin harekesini bul.
    # --------------------------------------------------------

    weak_vowel_index, weak_vowel = (
        _find_vowel_after_letter(
            word,
            weak_index,
        )
    )

    if (
        weak_vowel_index == -1
        or weak_vowel != "َ"
    ):
        return word

    # --------------------------------------------------------
    # 1. İllet harfinin üzerindeki fethayı kaldır.
    # --------------------------------------------------------

    result = _remove_vowel_after_letter(
        word,
        weak_index,
    )

    # --------------------------------------------------------
    # 2. Fâu'l-fiilin mevcut harekesini kaldır.
    # --------------------------------------------------------

    fa_index = _find_letter_after(
        result,
        root.fa,
    )

    if fa_index == -1:
        return word

    result = _remove_vowel_after_letter(
        result,
        fa_index,
    )

    # --------------------------------------------------------
    # 3. Fethayı fâu'l-fiile aktar.
    # --------------------------------------------------------

    result = _replace_vowel_after_letter(
        result,
        fa_index,
        "َ",
    )

    # --------------------------------------------------------
    # 4. İllet harfini elife çevir.
    #
    # يُقْوَلُ → يُقَالُ
    # يُبْيَعُ → يُبَاعُ
    # --------------------------------------------------------

    weak_index = _find_letter_after(
        result,
        root.ayn,
        fa_index + 1,
    )

    if weak_index == -1:
        return result

    result = (
        result[:weak_index]
        + "ا"
        + result[weak_index + 1:]
    )

    return result


# ============================================================
# ECVEF — MEZCÛM
# ============================================================

def _delete_hollow_letter_from_jussive(
    word: str,
    root: Root,
) -> str:
    """
    Ecvef fiilin meczûm hâlini üretir.

    Örnek:

        يَقُولُ → يَقُلْ
        يَبِيعُ → يَبِعْ
    """

    if root.ayn not in (
        "و",
        "ي",
    ):
        return _put_final_hareke(
            word,
            "ْ",
        )

    positions = _find_root_positions(
        word,
        root,
    )

    if positions is None:
        return _put_final_hareke(
            word,
            "ْ",
        )

    _, weak_index, _ = positions

    # --------------------------------------------------------
    # İllet harfini sil.
    # --------------------------------------------------------

    result = (
        word[:weak_index]
        + word[weak_index + 1:]
    )

    # --------------------------------------------------------
    # İllet harfinin arkasındaki harekeyi sil.
    # --------------------------------------------------------

    if (
        weak_index < len(result)
        and _is_hareke(result[weak_index])
    ):
        result = (
            result[:weak_index]
            + result[weak_index + 1:]
        )

    # --------------------------------------------------------
    # Lâmü'l-fiili bul.
    # --------------------------------------------------------

    fa_index = _find_letter_after(
        result,
        root.fa,
    )

    if fa_index == -1:
        return result

    lam_index = _find_letter_after(
        result,
        root.lam,
        fa_index + 1,
    )

    if lam_index == -1:
        return result

    # --------------------------------------------------------
    # Lâmü'l-fiilin harekesini cezm yap.
    # --------------------------------------------------------

    after_lam = lam_index + 1

    if (
        after_lam < len(result)
        and _is_hareke(result[after_lam])
    ):
        result = (
            result[:after_lam]
            + "ْ"
            + result[after_lam + 1:]
        )

    else:
        result = (
            result[:lam_index + 1]
            + "ْ"
            + result[lam_index + 1:]
        )

    return result


def _make_jussive(
    present: str,
    root: Root,
) -> str:
    """
    Muzâri fiili meczûm hâle getirir.
    """

    if root.ayn in (
        "و",
        "ي",
    ):
        return _delete_hollow_letter_from_jussive(
            present,
            root,
        )

    return _put_final_hareke(
        present,
        "ْ",
    )


# ============================================================
# NASB
# ============================================================

def _make_nasb(
    present: str,
) -> str:
    """
    Muzâri fiili nasb hâline getirir.

    Örnek:

        يَنْصُرُ → يَنْصُرَ
    """

    return _put_final_hareke(
        present,
        "َ",
    )


# ============================================================
# MUHATAB
# ============================================================

def _make_muhatab_present(
    present: str,
) -> str:
    """
    Üçüncü şahıs muzâriyi ikinci şahıs muzâriye çevirir.

        يَنْصُرُ → تَنْصُرُ
        يَقُولُ  → تَقُولُ
    """

    if present.startswith("ي"):
        return "ت" + present[1:]

    return present


# ============================================================
# MUZÂRAAT HARFİNİ KALDIRMA
# ============================================================

def _remove_muzari_prefix(
    word: str,
) -> str:
    """
    Muzâraat harfi olan ي ile onun harekesini birlikte kaldırır.
    """

    if not word.startswith("ي"):
        return word

    if (
        len(word) >= 2
        and _is_hareke(word[1])
    ):
        return word[2:]

    return word[1:]


# ============================================================
# EMR-İ HÂZIR
# ============================================================

def _make_emr_hazir(
    present: str,
    root: Root,
) -> str:
    """
    Muzâriden emr-i hâzır üretir.
    """

    if not present.startswith("ي"):
        return present

    # --------------------------------------------------------
    # 1. Muzâraat harfini + harekesini kaldır.
    # --------------------------------------------------------

    base_present = _remove_muzari_prefix(
        present,
    )

    # --------------------------------------------------------
    # 2. Meczûm hâle getir.
    # --------------------------------------------------------

    jussive = _make_jussive(
        present,
        root,
    )

    base = _remove_muzari_prefix(
        jussive,
    )

    if not base:
        return base_present

    # --------------------------------------------------------
    # 3. Ecvef.
    # --------------------------------------------------------

    if root.ayn in (
        "و",
        "ي",
    ):
        return base

    # --------------------------------------------------------
    # 4. Normal fiil.
    # --------------------------------------------------------

    if len(base) < 2:
        return base

    first_vowel = base[1]

    if first_vowel == "ْ":
        return "أُ" + base

    return base


# ============================================================
# MEÇHUL — MÂZÎ
# ============================================================

def _build_past_passive(
    root: Root,
    bab: Bab,
) -> str:
    """
    Sülâsî mücerred fiilin mâzî meçhulünü üretir.

    Genel kalıp:

        فُعِلَ

    Örnek:

        نَصَرَ → نُصِرَ

    Ecvef vâvî:

        قَالَ
        ↓
        قُوِلَ
        ↓
        قِيلَ

    Ecvef yâî:

        بَاعَ
        ↓
        بُيِعَ
        ↓
        بِيعَ
    """

    # --------------------------------------------------------
    # Bâb uygunluğunu doğrula.
    # --------------------------------------------------------

    build_verb(
        root,
        bab,
    )

    # --------------------------------------------------------
    # Genel mâzî meçhul.
    # --------------------------------------------------------

    result = apply_pattern(
        "فُعِلَ",
        root,
    )

    # --------------------------------------------------------
    # Ecvef i'lâli.
    # --------------------------------------------------------

    if root.ayn in (
        "و",
        "ي",
    ):
        result = _apply_hollow_past_passive_ilal(
            result,
            root,
        )

    return result


# ============================================================
# MEÇHUL — MUZÂRİ
# ============================================================

def _build_present_passive(
    root: Root,
    bab: Bab,
) -> str:
    """
    Sülâsî mücerred fiilin muzâri meçhulünü üretir.

    Genel kalıp:

        يُفْعَلُ

    Sahih:

        يَنْصُرُ
        ↓
        يُنْصَرُ

    Misâl-i Vâvî:

        يَعِدُ
        ↓
        يُوْعَدُ
        ↓
        يُوعَدُ

    Misâl-i Yâî:

        يَيْسِرُ
        ↓
        يُيْسَرُ
        ↓
        يُوسَرُ

    Ecvef vâvî:

        يَقُولُ
        ↓
        يُقْوَلُ
        ↓
        يُقَالُ

    Ecvef yâî:

        يَبِيعُ
        ↓
        يُبْيَعُ
        ↓
        يُبَاعُ
    """

    # --------------------------------------------------------
    # Bâb uygunluğunu doğrula.
    # --------------------------------------------------------

    build_verb(
        root,
        bab,
    )

    # --------------------------------------------------------
    # Genel muzâri meçhul.
    # --------------------------------------------------------

    result = apply_pattern(
        "يُفْعَلُ",
        root,
    )

    # ========================================================
    # ECVEF
    # ========================================================

    if root.ayn in (
        "و",
        "ي",
    ):
        return _apply_hollow_present_passive_ilal(
            result,
            root,
        )

    # ========================================================
    # MİSÂL-İ VÂVÎ
    # ========================================================

    if root.fa == "و":

        vav_index = _find_letter_after(
            result,
            "و",
            1,
        )

        if vav_index != -1:
            # Kitaptaki yazım:
            #
            # يُوعَدُ
            #
            # Vâv korunur ancak üzerindeki
            # sükûn ayrıca gösterilmez.

            result = _remove_vowel_after_letter(
                result,
                vav_index,
            )

        return result

    # ========================================================
    # MİSÂL-İ YÂÎ
    # ========================================================

    if root.fa == "ي":

        ya_index = _find_letter_after(
            result,
            "ي",
            1,
        )

        if ya_index == -1:
            return result

        transformed = IlalTransformer.qalb_ya_to_vav(
            result,
            ya_index,
        )

        return transformed.result

    return result


# ============================================================
# DIŞARIDAN ERİŞİLEBİLEN MEÇHUL MOTORLARI
# ============================================================

def build_past_passive(
    root: Root,
    bab: Bab,
) -> str:
    """
    Mâzî meçhulü doğrudan üretir.
    """

    return _build_past_passive(
        root,
        bab,
    )


def build_present_passive(
    root: Root,
    bab: Bab,
) -> str:
    """
    Muzâri meçhulü doğrudan üretir.
    """

    return _build_present_passive(
        root,
        bab,
    )


# ============================================================
# ANA SÎGA MOTORU
# ============================================================

def build_siga(
    root: Root,
    bab: Bab,
    siga: Siga,
    voice: str = "active",
) -> str:
    """
    Verilen kök, bâb ve sîgaya göre sîga formunu üretir.

    voice:

        "active"
            Malum / etken

        "passive"
            Meçhul / edilgen

    Meçhul, yeni bir sîga numarası değildir.
    Sîganın binâsı olarak ele alınır.
    """

    # ========================================================
    # BİNA / VOICE KONTROLÜ
    # ========================================================

    if voice not in (
        "active",
        "passive",
    ):
        raise ValueError(
            f"Bilinmeyen bina: {voice}. "
            f"'active' veya 'passive' kullanılmalıdır."
        )

    # ========================================================
    # MEÇHUL
    # ========================================================

    if voice == "passive":

        if siga.number == 1:
            return build_past_passive(
                root,
                bab,
            )

        if siga.number == 2:
            return build_present_passive(
                root,
                bab,
            )

        raise NotImplementedError(
            "Şu aşamada yalnızca mâzî ve muzâri "
            "meçhul desteklenmektedir."
        )

    # ========================================================
    # MALUM VERB MOTORU
    # ========================================================

    verb = build_verb(
        root,
        bab,
    )

    # ========================================================
    # 1 - MÂZİ
    # ========================================================

    if siga.number == 1:
        return verb.past

    # ========================================================
    # 2 - MUZÂRİ
    # ========================================================

    if siga.number == 2:
        return verb.present

    # ========================================================
    # 3 - MASTAR
    # ========================================================

    if siga.number == 3:
        raise NotImplementedError(
            "Sülâsî mastar için kitapta tek bir üretim "
            "kuralı belirtilmemiştir."
        )

    # ========================================================
    # 4 - İSM-İ FÂİL
    # ========================================================

    if siga.number == 4:
        return apply_pattern(
            "فَاعِلٌ",
            root,
        )

    # ========================================================
    # 5 - İSM-İ MEF'ÛL
    # ========================================================

    if siga.number == 5:
        return apply_pattern(
            "مَفْعُولٌ",
            root,
        )

    # ========================================================
    # 6 - CAHD-I MUTLAK
    # ========================================================

    if siga.number == 6:
        jussive = _make_jussive(
            verb.present,
            root,
        )

        return f"لَمْ {jussive}"

    # ========================================================
    # 7 - CAHD-I MUSTAĞRAK
    # ========================================================

    if siga.number == 7:
        jussive = _make_jussive(
            verb.present,
            root,
        )

        return f"لَمَّا {jussive}"

    # ========================================================
    # 8 - NEFY-İ HÂL
    # ========================================================

    if siga.number == 8:
        return f"مَا {verb.present}"

    # ========================================================
    # 9 - NEFY-İ İSTİKBÂL
    # ========================================================

    if siga.number == 9:
        return f"لَا {verb.present}"

    # ========================================================
    # 10 - TE'KÎD NEFY-İ İSTİKBÂL
    # ========================================================

    if siga.number == 10:
        nasb = _make_nasb(
            verb.present,
        )

        return f"لَنْ {nasb}"

    # ========================================================
    # 11 - EMR-İ ĞÂİB
    # ========================================================

    if siga.number == 11:
        jussive = _make_jussive(
            verb.present,
            root,
        )

        return f"لِ{jussive}"

    # ========================================================
    # 12 - NEHY-İ ĞÂİB
    # ========================================================

    if siga.number == 12:
        jussive = _make_jussive(
            verb.present,
            root,
        )

        return f"لَا {jussive}"

    # ========================================================
    # 13 - EMR-İ HÂZIR
    # ========================================================

    if siga.number == 13:
        return _make_emr_hazir(
            verb.present,
            root,
        )

    # ========================================================
    # 14 - NEHY-İ HÂZIR
    # ========================================================

    if siga.number == 14:

        muhatab = _make_muhatab_present(
            verb.present,
        )

        jussive = _make_jussive(
            muhatab,
            root,
        )

        return f"لَا {jussive}"

    # ========================================================
    # 15 - İSM-İ ZAMAN / MEKÂN / MASTAR-I MÎMÎ
    # ========================================================

    if siga.number == 15:
        return apply_pattern(
            "مَفْعَلٌ",
            root,
        )

    # ========================================================
    # 16 - İSM-İ ÂLET
    # ========================================================

    if siga.number == 16:
        return apply_pattern(
            "مِفْعَلٌ",
            root,
        )

    # ========================================================
    # 17 - MASTAR-I BİNÂ-İ MERRE
    # ========================================================

    if siga.number == 17:
        return apply_pattern(
            "فَعْلَةً",
            root,
        )

    # ========================================================
    # 18 - MASTAR-I BİNÂ-İ NEV'
    # ========================================================

    if siga.number == 18:
        return apply_pattern(
            "فِعْلَةً",
            root,
        )

    # ========================================================
    # 19 - İSM-İ TASĞÎR
    # ========================================================

    if siga.number == 19:
        return apply_pattern(
            "فُعَيْلٌ",
            root,
        )

    # ========================================================
    # 20 - İSM-İ MENSUP
    # ========================================================

    if siga.number == 20:
        raise NotImplementedError(
            "İsm-i Mensup için kitapta özel üretim "
            "vezni belirtilmemiştir."
        )

    # ========================================================
    # 21 - MÜBALAĞALI İSM-İ FÂİL
    # ========================================================

    if siga.number == 21:
        return apply_pattern(
            "فَعَّالٌ",
            root,
        )

    # ========================================================
    # 22 - İSM-İ TAFDİL
    # ========================================================

    if siga.number == 22:
        return apply_pattern(
            "أَفْعَلُ",
            root,
        )

    # ========================================================
    # 23 - TA'ACCUP I
    # ========================================================

    if siga.number == 23:
        return apply_pattern(
            "مَا أَفْعَلَهُ",
            root,
        )

    # ========================================================
    # 24 - TA'ACCUP II
    # ========================================================

    if siga.number == 24:
        return apply_pattern(
            "أَفْعِلْ بِهِ",
            root,
        )

    # ========================================================
    # BİLİNMEYEN SÎGA
    # ========================================================

    raise ValueError(
        f"Bilinmeyen sîga numarası: {siga.number}"
    )
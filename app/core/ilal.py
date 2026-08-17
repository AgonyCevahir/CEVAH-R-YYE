from __future__ import annotations

from dataclasses import dataclass


# ============================================================
# İLLET HARFLERİ
# ============================================================

ILLET_HARFLERI = (
    "و",
    "ي",
    "ى",
)


# ============================================================
# İ'LÂL İŞLEM TÜRLERİ
# ============================================================

@dataclass(frozen=True)
class IlalResult:
    """
    Bir i'lâl işleminin sonucunu temsil eder.

    original:
        İşlem öncesindeki kelime.

    result:
        İşlem sonrasındaki kelime.

    rule:
        Uygulanan i'lâl kuralının adı.
    """

    original: str
    result: str
    rule: str


# ============================================================
# YARDIMCI KONTROLLER
# ============================================================

def is_weak_letter(letter: str) -> bool:
    """
    Verilen harfin illet harfi olup olmadığını kontrol eder.
    """

    return letter in ILLET_HARFLERI


def has_weak_letter(letters: tuple[str, ...]) -> bool:
    """
    Harf dizisinde en az bir illet harfi bulunup bulunmadığını
    kontrol eder.
    """

    return any(
        is_weak_letter(letter)
        for letter in letters
    )


# ============================================================
# KALB
# ============================================================

def qalb_to_alif(
    previous_letter: str,
    weak_letter: str,
    previous_vowel: str,
    weak_vowel: str,
) -> str:
    """
    Vâv veya yânın elif'e dönüşmesi için temel şartı kontrol eder.

    Kitaptaki temel kural:
    İllet harfi harekeli olacak ve kendisinden önceki harf
    fethalı bulunacaktır.

    Bu fonksiyon yalnızca dönüşümün mümkün olup olmadığını
    kontrol eder.

    Doğrudan kelime üretmez.
    """

    if weak_letter not in ("و", "ي"):
        return weak_letter

    if weak_vowel == "" or previous_vowel != "َ":
        return weak_letter

    return "ا"


# ============================================================
# HAZF
# ============================================================

def delete_weak_letter(
    weak_letter: str,
    is_meczum: bool,
    is_final: bool,
) -> str:
    """
    Meczûm durumda kelime sonunda bulunan illet harfinin
    hazfedilmesini temsil eder.

    Şimdilik yalnızca açıkça tanımlanabilen genel mekanizmayı
    uygular.

    Gerçek fiil üretimi verb/siga motorunda yapılacaktır.
    """

    if (
        is_meczum
        and is_final
        and is_weak_letter(weak_letter)
    ):
        return ""

    return weak_letter


# ============================================================
# İSKÂN
# ============================================================

def sakinize_weak_letter(
    weak_letter: str,
    is_final: bool,
) -> str:
    """
    Kelime sonunda bulunan vâv veya yânın sakin bırakılmasını
    temsil eder.

    Harfin kendisini değiştirmez.
    Hareke bilgisi daha sonra hareke motoru tarafından yönetilir.
    """

    if is_final and is_weak_letter(weak_letter):
        return weak_letter

    return weak_letter


# ============================================================
# NAKL-İ HAREKE
# ============================================================

@dataclass(frozen=True)
class HarakaTransfer:
    """
    Bir illet harfinin harekesinin kendisinden önceki
    harfe aktarılmasını temsil eder.
    """

    previous_vowel: str
    weak_vowel: str


def transfer_weak_vowel(
    previous_vowel: str,
    weak_vowel: str,
    weak_letter: str,
) -> HarakaTransfer:
    """
    Ecvef fiillerde nakl-i harekenin temel veri dönüşümünü
    temsil eder.

    Örnek mantık:

        يَقْوُلُ
              ↓
        يَقُولُ

    Vâvın dammesi önceki harfe aktarılır.

    Bu fonksiyon yalnızca hareke aktarımını temsil eder;
    kelimenin tamamını yeniden yazmaz.
    """

    if not is_weak_letter(weak_letter):
        return HarakaTransfer(
            previous_vowel=previous_vowel,
            weak_vowel=weak_vowel,
        )

    if weak_vowel == "":
        return HarakaTransfer(
            previous_vowel=previous_vowel,
            weak_vowel=weak_vowel,
        )

    return HarakaTransfer(
        previous_vowel=weak_vowel,
        weak_vowel="",
    )


# ============================================================
# İ'LÂL KURALI SONUCU
# ============================================================

def apply_ilal_rule(
    original: str,
    result: str,
    rule: str,
) -> IlalResult:
    """
    Uygulanan i'lâl işlemini kayıt altına alır.
    """

    return IlalResult(
        original=original,
        result=result,
        rule=rule,
    )
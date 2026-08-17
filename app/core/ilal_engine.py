from __future__ import annotations

from dataclasses import dataclass

from app.core.ilal import (
    ILLET_HARFLERI,
    HarakaTransfer,
    IlalResult,
    apply_ilal_rule,
    delete_weak_letter,
    qalb_to_alif,
    sakinize_weak_letter,
    transfer_weak_vowel,
)


# ============================================================
# HAREKELİ HARF
# ============================================================

@dataclass(frozen=True)
class Harf:
    """
    Bir Arapça harfi ve üzerindeki harekeyi temsil eder.

    Örnek:

        Harf("ق", "َ")
        Harf("و", "ُ")
    """

    letter: str
    vowel: str = ""


# ============================================================
# İ'LÂL MOTORU
# ============================================================

class IlalEngine:
    """
    İlletli fiillerde uygulanacak temel i'lâl işlemlerini
    yöneten motor.

    Bu sınıf şu işlemleri kapsar:

        - Kalb
        - Hazf
        - İskân
        - Nakl-i hareke

    Motor şu aşamada doğrudan fiil çekimi yapmaz.
    Kendisine verilen harf/hareke yapısı üzerinde işlem yapar.

    Böylece i'lâl kuralları verb_engine'dan bağımsız
    ve ayrı olarak test edilebilir.
    """

    # ========================================================
    # KALB
    # ========================================================

    @staticmethod
    def qalb_to_alif(
        previous: Harf,
        weak: Harf,
    ) -> Harf:
        """
        Harekeli vâv veya yânın elif'e dönüşmesini kontrol eder.

        Temel şart:

            önceki harf fethalı
            +
            illet harfi vâv veya yâ
            +
            illet harfi harekeli

        ise illet harfi elif'e çevrilir.

        Örnek mantık:

            قَوَلَ
              ↑
            و → ا

        Sonuçta yalnızca değişen harf döndürülür.
        """

        result = qalb_to_alif(
            previous_letter=previous.letter,
            weak_letter=weak.letter,
            previous_vowel=previous.vowel,
            weak_vowel=weak.vowel,
        )

        return Harf(
            letter=result,
            vowel="",
        )

    # ========================================================
    # HAZF
    # ========================================================

    @staticmethod
    def delete_final_weak(
        weak: Harf,
        is_meczum: bool,
    ) -> Harf:
        """
        Meczûm durumda kelime sonundaki illet harfinin
        hazfedilmesini uygular.

        Örnek mantık:

            يَقُولْ
               ↓
            يَقُلْ

        Burada son illet harfi düşürülür.
        """

        result = delete_weak_letter(
            weak_letter=weak.letter,
            is_meczum=is_meczum,
            is_final=True,
        )

        return Harf(
            letter=result,
            vowel="" if result == "" else weak.vowel,
        )

    # ========================================================
    # İSKÂN
    # ========================================================

    @staticmethod
    def sakinize_final_weak(
        weak: Harf,
    ) -> Harf:
        """
        Kelime sonundaki vâv veya yânın sakin hale
        getirilmesini temsil eder.

        Harfin kendisini değiştirmez.

        Hareke bilgisi boş bırakılır.
        """

        result = sakinize_weak_letter(
            weak_letter=weak.letter,
            is_final=True,
        )

        return Harf(
            letter=result,
            vowel="",
        )

    # ========================================================
    # NAKL-İ HAREKE
    # ========================================================

    @staticmethod
    def transfer_weak_vowel(
        previous: Harf,
        weak: Harf,
    ) -> tuple[Harf, Harf]:
        """
        İllet harfinin harekesini kendisinden önceki
        harfe aktarır.

        Örnek mantık:

            يَقْوُلُ
               ↓
            يَقُولُ

        Vâvın dammesi önceki harfe aktarılır.
        """

        result: HarakaTransfer = transfer_weak_vowel(
            previous_vowel=previous.vowel,
            weak_vowel=weak.vowel,
            weak_letter=weak.letter,
        )

        new_previous = Harf(
            letter=previous.letter,
            vowel=result.previous_vowel,
        )

        new_weak = Harf(
            letter=weak.letter,
            vowel=result.weak_vowel,
        )

        return (
            new_previous,
            new_weak,
        )

    # ========================================================
    # İLLET HARFİ KONTROLÜ
    # ========================================================

    @staticmethod
    def is_weak(letter: str) -> bool:
        """
        Verilen harfin illet harfi olup olmadığını kontrol eder.
        """

        return letter in ILLET_HARFLERI

    # ========================================================
    # İ'LÂL SONUCUNU KAYDETME
    # ========================================================

    @staticmethod
    def make_result(
        original: str,
        result: str,
        rule: str,
    ) -> IlalResult:
        """
        Uygulanan i'lâl işlemini kayıt altına alır.
        """

        return apply_ilal_rule(
            original=original,
            result=result,
            rule=rule,
        )


# ============================================================
# TEK MERKEZDEN MOTOR ERİŞİMİ
# ============================================================

ILAL_ENGINE = IlalEngine()
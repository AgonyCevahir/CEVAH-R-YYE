from app.core.bab import (
    Bab,
    BAB_3,
    BOGAZ_HARFLERI,
)
from app.core.root import Root


# ============================================================
# BÂB 3 - BOĞAZ HARFİ KONTROLÜ
# ============================================================

def has_throat_letter_for_bab_3(root: Root) -> bool:
    """
    Bâb 3 için ayne'l-fiil veya lâme'l-fiilin
    boğaz harfi olup olmadığını kontrol eder.

    Kitaptaki kural:
    Ayne'l-fiil veya lâme'l-fiil boğaz harflerinden
    biri olmalıdır.
    """

    return (
        root.ayn in BOGAZ_HARFLERI
        or root.lam in BOGAZ_HARFLERI
    )


# ============================================================
# BÂB 3 - أَبَى İSTİSNASI
# ============================================================

def is_bab_3_exception(root: Root) -> bool:
    """
    Bâb 3'ün kitapta belirtilen istisnası:

        أَبَى - يَأْبَى

    Bu fiil normal boğaz harfi şartını taşımamasına
    rağmen Bâb 3'ten gelir.

    Root sınıfında kök:
        أ - ب - ي

    şeklinde tutulur.

    Bazı yüzey yazımlarında son harf ى şeklinde
    görünebilir. Bu nedenle hem ي hem ى kabul edilir.
    """

    return (
        root.fa == "أ"
        and root.ayn == "ب"
        and root.lam in ("ي", "ى")
    )


# ============================================================
# BÂB 3 - GEÇERLİLİK KONTROLÜ
# ============================================================

def is_valid_for_bab_3(root: Root) -> bool:
    """
    Kökün Bâb 3'e uygun olup olmadığını kontrol eder.

    Öncelik:
    1. أَبَى istisnası
    2. Boğaz harfi kuralı
    3. Aksi halde geçersiz
    """

    # Önce kitapta belirtilen istisnayı kontrol et.
    if is_bab_3_exception(root):
        return True

    # Normal Bâb 3 kuralını kontrol et.
    return has_throat_letter_for_bab_3(root)


# ============================================================
# GENEL BÂB UYGUNLUK KONTROLÜ
# ============================================================

def is_root_valid_for_bab(root: Root, bab: Bab) -> bool:
    """
    Verilen kökün seçilen bâba uygun olup olmadığını kontrol eder.

    Şu aşamada kitapta kökün yapısına ilişkin özel şartı
    açıkça tanımlanan bâb Bâb 3'tür.

    Diğer bâblar için henüz ek bir kök kısıtlaması uygulanmaz.
    """

    if bab.number == BAB_3.number:
        return is_valid_for_bab_3(root)

    return True
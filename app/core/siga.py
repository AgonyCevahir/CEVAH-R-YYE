from dataclasses import dataclass


@dataclass(frozen=True)
class Siga:
    number: int
    name: str
    pattern: str | None
    example: str
    meaning: str
    category: str
    note: str
    pages: tuple[int, ...]


# ============================================================
# EMSİLE-İ MUHTELİFE — 24 SÎGA
#
# Kaynak:
# Kelime Bilgisi Sarf
#
# Bu bölüm yalnızca kitapta doğrulanan verileri temsil eder.
# Henüz üretim algoritması değildir.
# ============================================================


SIGA_01 = Siga(
    number=1,
    name="Mâzi Fiil",
    pattern="فَعَلَ",
    example="نَصَرَ",
    meaning="Yardım etti",
    category="Fiil",
    note="Geçmiş zaman bildiren fiil.",
    pages=(18, 25),
)


SIGA_02 = Siga(
    number=2,
    name="Muzâri Fiil",
    pattern="يَفْعُلُ",
    example="يَنْصُرُ",
    meaning="Yardım ediyor, eder, edecek",
    category="Fiil",
    note="Şimdiki ve gelecek zaman.",
    pages=(18, 25),
)


SIGA_03 = Siga(
    number=3,
    name="Mastar",
    pattern="فَعْلًا",
    example="نَصْرًا",
    meaning="Yazmak",
    category="İsim",
    note=(
        "S. 18'de 'Yazmak' geçer; "
        "S. 42'de 'Yardım etmek' olarak açıklanır."
    ),
    pages=(18, 42),
)


SIGA_04 = Siga(
    number=4,
    name="İsm-i Fâil",
    pattern="فَاعِلٌ",
    example="نَاصِرٌ",
    meaning="Yardım eden",
    category="İsim",
    note="İş yapanın ismidir.",
    pages=(18, 27),
)


SIGA_05 = Siga(
    number=5,
    name="İsm-i Mef‘ûl",
    pattern="مَفْعُولٌ",
    example="مَنْصُورٌ",
    meaning="Yardım edilmiş",
    category="İsim",
    note="Yapılan işten etkilenen isim.",
    pages=(18, 27),
)


SIGA_06 = Siga(
    number=6,
    name="Cahd-ı Mutlak",
    pattern="لَمْ يَفْعُلْ",
    example="لَمْ يَنْصُرْ",
    meaning="Yardım etmedi",
    category="Fiil",
    note="Muzâriyi geçmiş zaman olumsuza çevirir.",
    pages=(18, 51),
)


SIGA_07 = Siga(
    number=7,
    name="Cahd-ı Mustağrak",
    pattern="لَمَّا يَفْعُلْ",
    example="لَمَّا يَنْصُرْ",
    meaning="Henüz yardım etmedi",
    category="Fiil",
    note="Eylemin henüz yapılmadığını bildirir.",
    pages=(18, 51),
)


SIGA_08 = Siga(
    number=8,
    name="Nefy-i Hâl",
    pattern="مَا يَفْعُلُ",
    example="مَا يَنْصُرُ",
    meaning="Yardım etmiyor",
    category="Fiil",
    note="Şimdiki zaman olumsuzu.",
    pages=(18, 51),
)


SIGA_09 = Siga(
    number=9,
    name="Nefy-i İstikbâl",
    pattern="لَا يَفْعُلُ",
    example="لَا يَنْصُرُ",
    meaning="Yardım etmez",
    category="Fiil",
    note="Gelecek zaman olumsuzu.",
    pages=(18, 50),
)


SIGA_10 = Siga(
    number=10,
    name="Te’kîd Nefy-i İstikbâl",
    pattern="لَنْ يَفْعُلَ",
    example="لَنْ يَنْصُرَ",
    meaning="Asla yardım etmeyecek",
    category="Fiil",
    note="Kesin gelecek zaman olumsuzu.",
    pages=(18, 51),
)


SIGA_11 = Siga(
    number=11,
    name="Emr-i Ğâib",
    pattern="لِيَفْعُلْ",
    example="لِيَنْصُرْ",
    meaning="Yardım etsin",
    category="Fiil",
    note="Üçüncü şahsa emir.",
    pages=(18, 51),
)


SIGA_12 = Siga(
    number=12,
    name="Nehy-i Ğâib",
    pattern="لَا يَفْعُلْ",
    example="لَا يَنْصُرْ",
    meaning="Yardım etmesin",
    category="Fiil",
    note="Üçüncü şahsa yasaklama.",
    pages=(18, 51),
)


SIGA_13 = Siga(
    number=13,
    name="Emr-i Hâzır",
    pattern="اُفْعُلْ",
    example="أُنْصُرْ",
    meaning="Yardım et",
    category="Fiil",
    note="Hemze dammelidir.",
    pages=(18, 26),
)


SIGA_14 = Siga(
    number=14,
    name="Nehy-i Hâzır",
    pattern="لَا تَفْعُلْ",
    example="لَا تَنْصُرْ",
    meaning="Yardım etme!",
    category="Fiil",
    note="Muhataba yasaklama.",
    pages=(18, 26),
)


SIGA_15 = Siga(
    number=15,
    name="İsm-i Zaman, İsm-i Mekân, Mastar-ı Mîmî",
    pattern="مَفْعَلٌ",
    example="مَنْصَرٌ",
    meaning="Yardım edilecek yer, zaman, mastar",
    category="İsim",
    note="Üç anlamda da kullanılır.",
    pages=(18, 90),
)


SIGA_16 = Siga(
    number=16,
    name="İsm-i Âlet",
    pattern="مِفْعَلٌ",
    example="مِنْصَرٌ",
    meaning="Yardım etme aleti",
    category="İsim",
    note="Eylemin aleti.",
    pages=(18, 28),
)


SIGA_17 = Siga(
    number=17,
    name="Mastar-ı Binâ-i Merre",
    pattern="فَعْلَةً",
    example="نَصْرَةً",
    meaning="Bir kere yardım etmek",
    category="İsim",
    note="Bir kere yapma bildirir.",
    pages=(18, 91),
)


SIGA_18 = Siga(
    number=18,
    name="Mastar-ı Binâ-i Nev’",
    pattern="فِعْلَةً",
    example="نِصْرَةً",
    meaning="Bir çeşit yardım etmek",
    category="İsim",
    note="Bir çeşit yapma bildirir.",
    pages=(18, 92),
)


SIGA_19 = Siga(
    number=19,
    name="İsm-i Tasğîr",
    pattern="فُعَيْلٌ",
    example="نُصَيْرٌ",
    meaning="Küçücük bir yardım etme",
    category="İsim",
    note="Küçültme ismi.",
    pages=(18, 29),
)


SIGA_20 = Siga(
    number=20,
    name="İsm-i Mensup",
    pattern=None,
    example="نَصْرِيٌّ",
    meaning="Yardım etmeye ait olan",
    category="İsim",
    note="Kitapta özel vezin formülü belirtilmemiştir.",
    pages=(18,),
)


SIGA_21 = Siga(
    number=21,
    name="Mübalağalı İsm-i Fâil",
    pattern="فَعَّالٌ",
    example="نَصَّارٌ",
    meaning="Çok yardım edici",
    category="İsim",
    note="Bir işi çok yapanın ismidir.",
    pages=(18, 27),
)


SIGA_22 = Siga(
    number=22,
    name="İsm-i Tafdil",
    pattern="أَفْعَلُ",
    example="أَنْصَرُ",
    meaning="En, daha yardım edici",
    category="İsim",
    note="Üstünlük bildiren isim.",
    pages=(18, 27),
)


SIGA_23 = Siga(
    number=23,
    name="Ta‘accup Fiili I",
    pattern="مَا أَفْعَلَهُ",
    example="مَا أَنْصَرَهُ",
    meaning="Amma da yardım etti",
    category="Fiil",
    note="Şaşırma bildiren 1. form.",
    pages=(18,),
)


SIGA_24 = Siga(
    number=24,
    name="Ta‘accup Fiili II",
    pattern="أَفْعِلْ بِهِ",
    example="أَنْصِرْ بِهِ",
    meaning="Amma da yardım etti",
    category="Fiil",
    note="Şaşırma bildiren 2. form.",
    pages=(18,),
)


# ============================================================
# 24 SÎGANIN TEK MERKEZDE TOPLANMASI
# ============================================================

EMSILE_I_MUHTELIFE = (
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
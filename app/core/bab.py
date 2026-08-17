from dataclasses import dataclass


@dataclass(frozen=True)
class Bab:
    number: int
    name: str

    past_pattern: str
    present_pattern: str

    past_example: str
    present_example: str

    meaning: str
    transitivity: str

    condition: str | None = None
    exceptions: tuple[str, ...] = ()

    masdar: str | None = None
    masdar_meaning: str | None = None


# ============================================================
# SÜLÂSÎ MÜCERREDİN ALTI BÂBI
# Kaynak: Kelime Bilgisi Sarf
# ============================================================

BAB_1 = Bab(
    number=1,
    name="fethu dammu",
    past_pattern="فَعَلَ",
    present_pattern="يَفْعُلُ",
    past_example="نَصَرَ",
    present_example="يَنْصُرُ",
    meaning="Yardım etmek",
    transitivity="Çoğu kere müte'addî, bazen de lâzım olur",
    masdar="نَصْرٌ",
    masdar_meaning="Yardım etmek",
)


BAB_2 = Bab(
    number=2,
    name="fethu kesru",
    past_pattern="فَعَلَ",
    present_pattern="يَفْعِلُ",
    past_example="ضَرَبَ",
    present_example="يَضْرِبُ",
    meaning="Vurmak",
    transitivity="Çoğu kere müte'addî, bazen de lâzım olur",
    masdar="ضَرْبٌ",
    masdar_meaning="Vurmak",
)


BAB_3 = Bab(
    number=3,
    name="fethatân",
    past_pattern="فَعَلَ",
    present_pattern="يَفْعَلُ",
    past_example="مَدَحَ",
    present_example="يَمْدَحُ",
    meaning="Övmek",
    transitivity="Çoğu kere müte'addî, bazen lâzım olur",
    condition=(
        "Ayne'l-fiili veya lâme'l-fiili boğaz harflerinden biri olmalıdır"
    ),
    exceptions=(
        "أَبَى - يَأْبَى",
    ),
    masdar="مَدْحٌ",
    masdar_meaning="Övmek",
)


BAB_4 = Bab(
    number=4,
    name="kesru fethu",
    past_pattern="فَعِلَ",
    present_pattern="يَفْعَلُ",
    past_example="عَلِمَ",
    present_example="يَعْلَمُ",
    meaning="Bilmek",
    transitivity="Çoğu kere müte'addî, bazen de lâzım olur",
    masdar="عِلْمٌ",
    masdar_meaning="Bilmek",
)


BAB_5 = Bab(
    number=5,
    name="dammu dammu",
    past_pattern="فَعُلَ",
    present_pattern="يَفْعُلُ",
    past_example="بَصُرَ",
    present_example="يَبْصُرُ",
    meaning="Görmek",
    transitivity="Bu bâb sadece lâzım (geçişsiz) olur",
    masdar="بَصَرٌ",
    masdar_meaning="Görmek",
)


BAB_6 = Bab(
    number=6,
    name="kesretân",
    past_pattern="فَعِلَ",
    present_pattern="يَفْعِلُ",
    past_example="حَسِبَ",
    present_example="يَحْسِبُ",
    meaning="Saymak, hesaplamak",
    transitivity="Bu bâbdan gelen çok az fiil vardır. Çoğu kere müte'addî, bazen lâzım olur",
    masdar="حِسَابٌ",
    masdar_meaning="Saymak, hesaplamak",
)


# ============================================================
# BÂBLARIN TEK MERKEZDEN ERİŞİLEBİLİRLİĞİ
# ============================================================

SULASI_MUCERRED_BABLAR = (
    BAB_1,
    BAB_2,
    BAB_3,
    BAB_4,
    BAB_5,
    BAB_6,
)


# ============================================================
# BOĞAZ HARFLERİ
# 3. BÂBIN KİTAPTA BELİRTİLEN ŞARTI
# ============================================================

BOGAZ_HARFLERI = (
    "أ",
    "ح",
    "خ",
    "ع",
    "غ",
    "ه",
    "هـ",
)
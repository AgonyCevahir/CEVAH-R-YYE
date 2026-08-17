from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SigaDefinition:
    number: int
    name: str
    arabic_name: Optional[str]
    kind: str
    pattern: Optional[str]
    example: str
    meaning: str
    source_structure: Optional[str]
    rule: str
    exceptions: Optional[str]
    pages: tuple[int, ...]


SIGA_DEFINITIONS = {

    # =========================================================
    # 1. MÂZÎ
    # =========================================================

    1: SigaDefinition(
        number=1,
        name="Mâzî Fiil",
        arabic_name=None,
        kind="Fiil",
        pattern="فَعَلَ",
        example="نَصَرَ",
        meaning="Yardım etti",
        source_structure="Mastardan türetilir",
        rule=(
            "Geçmiş zamanda bir eylemin olduğunu bildirir. "
            "Fiilin son harfi daima üstündür ve fetha üzere mebnidir."
        ),
        exceptions=(
            "3. bâbdan gelmesi için 2. veya 3. harfinin boğaz harfi "
            "olması şarttır. İstisna: أَبَى - يَأْبَى."
        ),
        pages=(18, 25, 33, 41),
    ),

    # =========================================================
    # 2. MUZÂRİ
    # =========================================================

    2: SigaDefinition(
        number=2,
        name="Muzâri Fiil",
        arabic_name=None,
        kind="Fiil",
        pattern="يَفْعُلُ",
        example="يَنْصُرُ",
        meaning="Yardım ediyor, eder, edecek",
        source_structure="Mâzî fiilden türetilir",
        rule=(
            "Mâzînin başına ا ت ي ن muzâraat harflerinden biri getirilir. "
            "Fiilin sonu merfûdur."
        ),
        exceptions=None,
        pages=(18, 25, 33),
    ),

    # =========================================================
    # 3. MASTAR
    # =========================================================

    3: SigaDefinition(
        number=3,
        name="Mastar",
        arabic_name=None,
        kind="İsim",
        pattern="فَعْلًا",
        example="نَصْرًا",
        meaning="Yazmak; yardım etmek",
        source_structure="Asıl/kök kabul edilen kelime",
        rule=(
            "Bir işi işlemek manasındadır. Sülâsî fiillerin mastarları "
            "çeşitli vezinlerde gelir ve kesin bir üretim kuralı yoktur."
        ),
        exceptions=(
            "Sülâsî mücerred mastarları semâîdir; kitapta 48 farklı "
            "mastar vezninden söz edilir."
        ),
        pages=(18, 42, 101),
    ),

    # =========================================================
    # 4. İSM-İ FÂİL
    # =========================================================

    4: SigaDefinition(
        number=4,
        name="İsm-i Fâil",
        arabic_name=None,
        kind="İsim",
        pattern="فَاعِلٌ",
        example="نَاصِرٌ",
        meaning="Yardım eden",
        source_structure="Mastardan müştaktır",
        rule=(
            "Bir işi yapana delalet eden isimdir. Sülâsî fiillerde "
            "فَاعِلٌ vezni kullanılır."
        ),
        exceptions=None,
        pages=(18, 27, 35),
    ),

    # =========================================================
    # 5. İSM-İ MEF'ÛL
    # =========================================================

    5: SigaDefinition(
        number=5,
        name="İsm-i Mef‘ûl",
        arabic_name=None,
        kind="İsim",
        pattern="مَفْعُولٌ",
        example="مَنْصُورٌ",
        meaning="Yardım edilmiş",
        source_structure="Mastardan müştaktır",
        rule=(
            "Yapılan eylemden etkilenen isimdir. Sülâsî fiillerde "
            "مَفْعُولٌ vezni kullanılır."
        ),
        exceptions=(
            "Lâzım fiillerden gelen sîgalarla ilgili kitapta özel "
            "hükümler bulunmaktadır."
        ),
        pages=(18, 27, 35, 40),
    ),

    # =========================================================
    # 6. CAHD-I MUTLAK
    # =========================================================

    6: SigaDefinition(
        number=6,
        name="Cahd-ı Mutlak",
        arabic_name=None,
        kind="Fiil",
        pattern="لَمْ يَفْعُلْ",
        example="لَمْ يَنْصُرْ",
        meaning="Yardım etmedi",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına لَمْ getirilir. Fiilin sonu "
            "cezimlenir ve geçmiş zaman olumsuz anlamı verir."
        ),
        exceptions=None,
        pages=(18, 51, 59, 77),
    ),

    # =========================================================
    # 7. CAHD-I MUSTAĞRAK
    # =========================================================

    7: SigaDefinition(
        number=7,
        name="Cahd-ı Mustağrak",
        arabic_name=None,
        kind="Fiil",
        pattern="لَمَّا يَفْعُلْ",
        example="لَمَّا يَنْصُرْ",
        meaning="Henüz yardım etmedi",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına لَمَّا getirilir ve fiil cezmedilir."
        ),
        exceptions=None,
        pages=(18, 51, 59, 78),
    ),

    # =========================================================
    # 8. NEFY-İ HÂL
    # =========================================================

    8: SigaDefinition(
        number=8,
        name="Nefy-i Hâl",
        arabic_name=None,
        kind="Fiil",
        pattern="مَا يَفْعُلُ",
        example="مَا يَنْصُرُ",
        meaning="Yardım etmiyor",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına مَا getirilir. Şimdiki zaman "
            "olumsuzluğu bildirir ve fiilin harekesini değiştirmez."
        ),
        exceptions=None,
        pages=(18, 51, 58, 71),
    ),

    # =========================================================
    # 9. NEFY-İ İSTİKBÂL
    # =========================================================

    9: SigaDefinition(
        number=9,
        name="Nefy-i İstikbâl",
        arabic_name=None,
        kind="Fiil",
        pattern="لَا يَفْعُلُ",
        example="لَا يَنْصُرُ",
        meaning="Yardım etmez",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına لَا getirilir. Gelecek zaman "
            "olumsuzluğu bildirir ve fiilin harekesini değiştirmez."
        ),
        exceptions=None,
        pages=(18, 50, 58, 70),
    ),

    # =========================================================
    # 10. TE'KÎD NEFY-İ İSTİKBÂL
    # =========================================================

    10: SigaDefinition(
        number=10,
        name="Te’kîd Nefy-i İstikbâl",
        arabic_name=None,
        kind="Fiil",
        pattern="لَنْ يَفْعُلَ",
        example="لَنْ يَنْصُرَ",
        meaning="Asla yardım etmeyecek",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına لَنْ getirilir. Muzâri fiilin sonu "
            "nasb sebebiyle üstün olur."
        ),
        exceptions=None,
        pages=(18, 51, 74),
    ),

    # =========================================================
    # 11. EMR-İ ĞÂİB
    # =========================================================

    11: SigaDefinition(
        number=11,
        name="Emr-i Ğâib",
        arabic_name=None,
        kind="Fiil",
        pattern="لِيَفْعُلْ",
        example="لِيَنْصُرْ",
        meaning="Yardım etsin",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına lâm-ı emir لِ getirilir ve "
            "fiilin sonu cezimlenir."
        ),
        exceptions=None,
        pages=(18, 51, 77),
    ),

    # =========================================================
    # 12. NEHY-İ ĞÂİB
    # =========================================================

    12: SigaDefinition(
        number=12,
        name="Nehy-i Ğâib",
        arabic_name=None,
        kind="Fiil",
        pattern="لَا يَفْعُلْ",
        example="لَا يَنْصُرْ",
        meaning="Yardım etmesin",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzârinin başına nehiy lâ'sı لَا getirilir ve "
            "fiilin sonu cezimlenir."
        ),
        exceptions=None,
        pages=(18, 51, 77),
    ),

    # =========================================================
    # 13. EMR-İ HÂZIR
    # =========================================================

    13: SigaDefinition(
        number=13,
        name="Emr-i Hâzır",
        arabic_name=None,
        kind="Fiil",
        pattern="اُفْعُلْ",
        example="أُنْصُرْ",
        meaning="Yardım et",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzâraat harfi atılır. Kalan harf okunamıyorsa başına "
            "elif-i vasıl getirilir. Elifin harekesi muzâri orta "
            "harfinin harekesine göre belirlenir ve sonu cezimlenir."
        ),
        exceptions=(
            "Muzâraat harfi atıldıktan sonra kalan yapı okunabiliyorsa "
            "elif eklenmez."
        ),
        pages=(18, 26, 34),
    ),

    # =========================================================
    # 14. NEHY-İ HÂZIR
    # =========================================================

    14: SigaDefinition(
        number=14,
        name="Nehy-i Hâzır",
        arabic_name=None,
        kind="Fiil",
        pattern="لَا تَفْعُلْ",
        example="لَا تَنْصُرْ",
        meaning="Yardım etme!",
        source_structure="Muzâri fiilden türetilir",
        rule=(
            "Muzâri muhatap sîgasının başına لَا getirilir "
            "ve fiilin sonu cezmedilir."
        ),
        exceptions=None,
        pages=(18, 26, 34),
    ),

    # =========================================================
    # 15. İSM-İ ZAMAN / MEKÂN / MİMÎ MASTAR
    # =========================================================

    15: SigaDefinition(
        number=15,
        name="İsm-i Zaman, Mekân, Mastar-ı Mîmî",
        arabic_name=None,
        kind="İsim",
        pattern="مَفْعَلٌ",
        example="مَنْصَرٌ",
        meaning="Yardım edilecek yer, zaman, mastar",
        source_structure="Mastardan türetilir",
        rule=(
            "Başında zâid bir mim bulunur. Eylemin yerini, zamanını "
            "veya mîmî mastar anlamını bildirebilir."
        ),
        exceptions=None,
        pages=(18, 28, 90, 92, 98),
    ),

    # =========================================================
    # 16. İSM-İ ÂLET
    # =========================================================

    16: SigaDefinition(
        number=16,
        name="İsm-i Âlet",
        arabic_name=None,
        kind="İsim",
        pattern="مِفْعَلٌ",
        example="مِنْصَرٌ",
        meaning="Yardım etme aleti",
        source_structure="Mastardan türetilir",
        rule=(
            "Bir işin aletinin ismidir. Kitaptaki örnek "
            "مِفْعَلٌ veznindedir."
        ),
        exceptions=(
            "Kitapta mezîd fiil mastarlarından ism-i âlet "
            "türetilemeyeceği belirtilmiştir."
        ),
        pages=(18, 28, 36, 85, 93),
    ),

    # =========================================================
    # 17. MASTAR-I BİNÂ-İ MERRE
    # =========================================================

    17: SigaDefinition(
        number=17,
        name="Mastar-ı Binâ-i Merre",
        arabic_name=None,
        kind="İsim",
        pattern="فَعْلَةً",
        example="نَصْرَةً",
        meaning="Bir kere yardım etmek",
        source_structure="Kök fiilden türetilir",
        rule=(
            "Bir eylemin bir kere yapıldığını bildirir. "
            "فَعْلَةً vezni kullanılır."
        ),
        exceptions=None,
        pages=(18, 91, 99),
    ),

    # =========================================================
    # 18. MASTAR-I BİNÂ-İ NEV'
    # =========================================================

    18: SigaDefinition(
        number=18,
        name="Mastar-ı Binâ-i Nev’",
        arabic_name=None,
        kind="İsim",
        pattern="فِعْلَةً",
        example="نِصْرَةً",
        meaning="Bir çeşit yardım etmek",
        source_structure="Kök fiilden türetilir",
        rule=(
            "Bir eylemin belli bir çeşit veya tarzda yapıldığını "
            "bildirir. فِعْلَةً vezni kullanılır."
        ),
        exceptions=None,
        pages=(18, 92, 100),
    ),

    # =========================================================
    # 19. İSM-İ TASĞÎR
    # =========================================================

    19: SigaDefinition(
        number=19,
        name="İsm-i Tasğîr",
        arabic_name=None,
        kind="İsim",
        pattern="فُعَيْلٌ",
        example="نُصَيْرٌ",
        meaning="Küçücük bir yardım etme",
        source_structure="İsimden türetilir",
        rule=(
            "Küçültme, sevgi veya azlık ifade eder. İlk harf dammeli, "
            "ikinci harf fethalı yapılır ve ikinci harften sonra "
            "sakin bir yâ getirilir."
        ),
        exceptions=None,
        pages=(18, 29, 37),
    ),

    # =========================================================
    # 20. İSM-İ MENSUP
    # =========================================================

    20: SigaDefinition(
        number=20,
        name="İsm-i Mensup",
        arabic_name=None,
        kind="İsim",
        pattern=None,
        example="نَصْرِيٌّ",
        meaning="Yardım etmeye ait olan",
        source_structure=None,
        rule="Aidiyet bildiren sîgadır.",
        exceptions=(
            "Kitapta bu sîga için genel üretim vezni açıkça "
            "belirtilmemiştir."
        ),
        pages=(18, 86),
    ),

    # =========================================================
    # 21. MÜBALAĞALI İSM-İ FÂİL
    # =========================================================

    21: SigaDefinition(
        number=21,
        name="Mübalağalı İsm-i Fâil",
        arabic_name=None,
        kind="İsim",
        pattern="فَعَّالٌ",
        example="نَصَّارٌ",
        meaning="Çok yardım edici",
        source_structure="Mastardan türetilir",
        rule=(
            "Bir işi çok yapanın ismidir. Kitaptaki örnek "
            "فَعَّالٌ veznindedir."
        ),
        exceptions=(
            "Mübalağalı ism-i fâil farklı vezinlerde gelebilir; "
            "kitapta yirmi farklı vezin listelenmiştir."
        ),
        pages=(18, 27, 35, 81, 89),
    ),

    # =========================================================
    # 22. İSM-İ TAFDÎL
    # =========================================================

    22: SigaDefinition(
        number=22,
        name="İsm-i Tafdîl",
        arabic_name=None,
        kind="İsim",
        pattern="أَفْعَلُ",
        example="أَنْصَرُ",
        meaning="En, daha yardım edici",
        source_structure="Mastardan türetilir",
        rule=(
            "Bir işi diğerinden daha fazla veya en üstün derecede "
            "yapanı bildirir. أَفْعَلُ vezni kullanılır."
        ),
        exceptions=(
            "Renk ve kusurlardan ism-i tafdîl türetilmesiyle ilgili "
            "özel şartlar vardır."
        ),
        pages=(18, 27, 35, 83, 91),
    ),

    # =========================================================
    # 23. TA'ACCUP I
    # =========================================================

    23: SigaDefinition(
        number=23,
        name="Ta‘accup Fiili I",
        arabic_name=None,
        kind="Fiil",
        pattern="مَا أَفْعَلَهُ",
        example="مَا أَنْصَرَهُ",
        meaning="Amma da yardım etti",
        source_structure=None,
        rule=(
            "Şaşırma/taaccup ifade eden birinci formdur. "
            "مَا أَفْعَلَهُ kalıbıyla gelir."
        ),
        exceptions=None,
        pages=(18, 317),
    ),

    # =========================================================
    # 24. TA'ACCUP II
    # =========================================================

    24: SigaDefinition(
        number=24,
        name="Ta‘accup Fiili II",
        arabic_name=None,
        kind="Fiil",
        pattern="أَفْعِلْ بِهِ",
        example="أَنْصِرْ بِهِ",
        meaning="Amma da yardım etti",
        source_structure=None,
        rule=(
            "Şaşırma/taaccup ifade eden ikinci formdur. "
            "أَفْعِلْ بِهِ kalıbıyla gelir."
        ),
        exceptions=None,
        pages=(18, 317),
    ),
}
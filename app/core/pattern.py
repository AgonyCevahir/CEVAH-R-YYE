from app.core.root import Root


def apply_pattern(pattern: str, root: Root) -> str:
    """
    Arapça vezni verilen kökle birleştirir.

    ف = kökün birinci harfi
    ع = kökün ikinci harfi
    ل = kökün üçüncü harfi
    """

    root_letters = {
        "ف": root.fa,
        "ع": root.ayn,
        "ل": root.lam,
    }

    result = []

    for char in pattern:
        result.append(root_letters.get(char, char))

    return "".join(result)
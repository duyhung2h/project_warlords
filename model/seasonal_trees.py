class SeasonalTrees:
    """
    Seasonal trees which contains information for each trees

    can also includes plants
    Oak -> Oak -> Oak Autumn -> Oak Autumn Snow

    """

    def __init__(self, SpringVariant, SummerVariant, FallVariant, WinterVariant):
        self.SpringVariant = SpringVariant
        self.SummerVariant = SummerVariant
        self.FallVariant = FallVariant
        self.WinterVariant = WinterVariant

    def get_seasonal_trees():
        return [
            SeasonalTrees(SpringVariant=4, SummerVariant=4, FallVariant=23, WinterVariant=23),
            SeasonalTrees(SpringVariant=5, SummerVariant=5, FallVariant=22, WinterVariant=22),
            SeasonalTrees(SpringVariant=6, SummerVariant=6, FallVariant=24, WinterVariant=24),
            SeasonalTrees(SpringVariant=7, SummerVariant=7, FallVariant=20, WinterVariant=20),
            SeasonalTrees(SpringVariant=8, SummerVariant=8, FallVariant=21, WinterVariant=21),
            SeasonalTrees(SpringVariant=9, SummerVariant=9, FallVariant=19, WinterVariant=19),
            # 10: dead tree
            # 11: dead tree
            # 12: dead tree
            SeasonalTrees(SpringVariant=13, SummerVariant=13, FallVariant=30, WinterVariant=30),
            SeasonalTrees(SpringVariant=14, SummerVariant=14, FallVariant=28, WinterVariant=28),
            SeasonalTrees(SpringVariant=15, SummerVariant=15, FallVariant=29, WinterVariant=29),
            # 16: dead tree
            # 17: dead tree
            # 18: dead tree
            # 19-24: orange leaf tree
            # 25-27: dead tree
            SeasonalTrees(SpringVariant=28, SummerVariant=28, FallVariant=26, WinterVariant=26),
            SeasonalTrees(SpringVariant=29, SummerVariant=29, FallVariant=25, WinterVariant=25),
            SeasonalTrees(SpringVariant=30, SummerVariant=30, FallVariant=24, WinterVariant=24),
            SeasonalTrees(SpringVariant=31, SummerVariant=31, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=32, SummerVariant=32, FallVariant=1, WinterVariant=1),
            SeasonalTrees(SpringVariant=33, SummerVariant=33, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=34, SummerVariant=34, FallVariant=1, WinterVariant=1),
            SeasonalTrees(SpringVariant=35, SummerVariant=35, FallVariant=2, WinterVariant=2),
            SeasonalTrees(SpringVariant=36, SummerVariant=36, FallVariant=3, WinterVariant=3),
            SeasonalTrees(SpringVariant=37, SummerVariant=37, FallVariant=11, WinterVariant=11),
            SeasonalTrees(SpringVariant=38, SummerVariant=38, FallVariant=10, WinterVariant=10),
            SeasonalTrees(SpringVariant=39, SummerVariant=39, FallVariant=41, WinterVariant=41),
            SeasonalTrees(SpringVariant=40, SummerVariant=40, FallVariant=40, WinterVariant=40),
            SeasonalTrees(SpringVariant=41, SummerVariant=41, FallVariant=7, WinterVariant=7),
            SeasonalTrees(SpringVariant=42, SummerVariant=42, FallVariant=12, WinterVariant=12),
            SeasonalTrees(SpringVariant=1, SummerVariant=1, FallVariant=3, WinterVariant=3),
            SeasonalTrees(SpringVariant=2, SummerVariant=2, FallVariant=1, WinterVariant=1),
            SeasonalTrees(SpringVariant=3, SummerVariant=3, FallVariant=2, WinterVariant=2),
        ]
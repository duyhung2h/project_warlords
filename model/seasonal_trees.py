class SeasonalTrees:
    """
    Seasonal trees which contains information for each trees

    can also includes plants


    """

    def __init__(self, SpringVariant, SummerVariant, FallVariant, WinterVariant):
        self.SpringVariant = SpringVariant
        self.SummerVariant = SummerVariant
        self.FallVariant = FallVariant
        self.WinterVariant = WinterVariant

    def get_seasonal_trees():
        return [
            SeasonalTrees(SpringVariant=4, SummerVariant=4, FallVariant=21, WinterVariant=21),
            SeasonalTrees(SpringVariant=6, SummerVariant=6, FallVariant=19, WinterVariant=19),
            SeasonalTrees(SpringVariant=7, SummerVariant=7, FallVariant=20, WinterVariant=20),
            SeasonalTrees(SpringVariant=8, SummerVariant=8, FallVariant=18, WinterVariant=18),
            SeasonalTrees(SpringVariant=27, SummerVariant=27, FallVariant=26, WinterVariant=26),
            SeasonalTrees(SpringVariant=28, SummerVariant=28, FallVariant=26, WinterVariant=26),
            SeasonalTrees(SpringVariant=29, SummerVariant=29, FallVariant=25, WinterVariant=25),
            SeasonalTrees(SpringVariant=30, SummerVariant=30, FallVariant=24, WinterVariant=24),
            SeasonalTrees(SpringVariant=31, SummerVariant=31, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=32, SummerVariant=32, FallVariant=1, WinterVariant=1),
            SeasonalTrees(SpringVariant=33, SummerVariant=33, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=34, SummerVariant=34, FallVariant=1, WinterVariant=1),
            SeasonalTrees(SpringVariant=35, SummerVariant=35, FallVariant=2, WinterVariant=2),
            SeasonalTrees(SpringVariant=36, SummerVariant=36, FallVariant=10, WinterVariant=10),
            SeasonalTrees(SpringVariant=37, SummerVariant=37, FallVariant=11, WinterVariant=11),
            SeasonalTrees(SpringVariant=38, SummerVariant=38, FallVariant=40, WinterVariant=40),
            SeasonalTrees(SpringVariant=39, SummerVariant=39, FallVariant=39, WinterVariant=39),

            SeasonalTrees(SpringVariant=33, SummerVariant=0, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=33, SummerVariant=1, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=33, SummerVariant=2, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=33, SummerVariant=3, FallVariant=0, WinterVariant=0),
            SeasonalTrees(SpringVariant=33, SummerVariant=5, FallVariant=0, WinterVariant=0),
        ]
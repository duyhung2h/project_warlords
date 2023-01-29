class SeasonalBushes:
    """
    Seasonal bushes which contains information for each bushes
    Bush B -> Bush B -> Bush B -> Bush C
    """

    def __init__(self, SpringVariant, SummerVariant, FallVariant, WinterVariant):
        self.SpringVariant = SpringVariant
        self.SummerVariant = SummerVariant
        self.FallVariant = FallVariant
        self.WinterVariant = WinterVariant

    def get_seasonal_bushes():
        return [
            SeasonalBushes(SpringVariant=27, SummerVariant=27, FallVariant=45, WinterVariant=21),
            SeasonalBushes(SpringVariant=0, SummerVariant=0, FallVariant=49, WinterVariant=22),
            SeasonalBushes(SpringVariant=14, SummerVariant=14, FallVariant=46, WinterVariant=23),
            SeasonalBushes(SpringVariant=12, SummerVariant=12, FallVariant=45, WinterVariant=24),
            SeasonalBushes(SpringVariant=28, SummerVariant=28, FallVariant=46, WinterVariant=25),
            SeasonalBushes(SpringVariant=20, SummerVariant=20, FallVariant=20, WinterVariant=26),
            SeasonalBushes(SpringVariant=42, SummerVariant=42, FallVariant=33, WinterVariant=0),
            SeasonalBushes(SpringVariant=44, SummerVariant=44, FallVariant=34, WinterVariant=1),
            SeasonalBushes(SpringVariant=41, SummerVariant=41, FallVariant=35, WinterVariant=2),
            SeasonalBushes(SpringVariant=30, SummerVariant=30, FallVariant=49, WinterVariant=3),
            SeasonalBushes(SpringVariant=23, SummerVariant=23, FallVariant=53, WinterVariant=4),
            SeasonalBushes(SpringVariant=19, SummerVariant=19, FallVariant=48, WinterVariant=5),
            SeasonalBushes(SpringVariant=40, SummerVariant=40, FallVariant=34, WinterVariant=6),
            SeasonalBushes(SpringVariant=39, SummerVariant=39, FallVariant=35, WinterVariant=7),
            SeasonalBushes(SpringVariant=21, SummerVariant=21, FallVariant=33, WinterVariant=8),
            SeasonalBushes(SpringVariant=11, SummerVariant=11, FallVariant=51, WinterVariant=9),
            SeasonalBushes(SpringVariant=31, SummerVariant=31, FallVariant=52, WinterVariant=10),
            SeasonalBushes(SpringVariant=10, SummerVariant=10, FallVariant=49, WinterVariant=11),
            SeasonalBushes(SpringVariant=2, SummerVariant=2, FallVariant=50, WinterVariant=12),
            SeasonalBushes(SpringVariant=32, SummerVariant=32, FallVariant=32, WinterVariant=13),
            SeasonalBushes(SpringVariant=13, SummerVariant=13, FallVariant=46, WinterVariant=14),
            SeasonalBushes(SpringVariant=39, SummerVariant=39, FallVariant=15, WinterVariant=15),
            SeasonalBushes(SpringVariant=38, SummerVariant=38, FallVariant=38, WinterVariant=16),
            SeasonalBushes(SpringVariant=36, SummerVariant=36, FallVariant=17, WinterVariant=17),
            SeasonalBushes(SpringVariant=18, SummerVariant=18, FallVariant=45, WinterVariant=18),
            SeasonalBushes(SpringVariant=9, SummerVariant=9, FallVariant=9, WinterVariant=19),
            SeasonalBushes(SpringVariant=4, SummerVariant=4, FallVariant=48, WinterVariant=20)

            # SeasonalBushes(SpringVariant=-1, SummerVariant=-1, FallVariant=-1, WinterVariant=-1),
        ]
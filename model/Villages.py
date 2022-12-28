class Villages:
    """
    This is a_localArea Villages class

    A village can have different attributes, such as villageName, locationXY [x1, x2, y1, y2]
    each village is captureable by one of 6 warlords players (each player can only have 3 villages each),
    they are untargetable at first. You either have two option (which are clickable inside the hero unit),

    either you raze the village (to obtain resources (rewarded for each unit kill/building razed) but decrease your unit morale)
    or
    win the village's favor (by doing their errands)
    """

    def __init__(self, villageName, locationXY):
        self.villageName = villageName
        self.locationXY = locationXY


    def get_characters():
        return [
            Villages('Tuyên Quang', [97, 131, 85, 118]),
        ]

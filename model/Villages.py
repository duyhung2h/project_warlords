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

    def __init__(self, villageName, locationXY, typeOfMission, TClocation):
        self.villageName = villageName
        self.locationXY = locationXY
        self.typeOfMission = typeOfMission
        self.TClocation = TClocation

    def get_villages():
        return [
            Villages('Tuyên Quang', [97, 131, 85, 118], 'ARMS_RACE', [117, 105]),
            Villages('Bắc Kạn', [160, 189, 126, 153], 'GATHERING', [172, 141]),
            Villages('Đại La', [82, 104, 147, 174], 'REGENCY', [97, 155]),
            Villages('Hoa Lư 1', [0, 0, 0, 0], 'TRIBAL_FEUD', [0, 0]),
        ]

    '''
    Mission description:
    
    GATHERING:
    X... has always been a defensive position, but in the cost of sizable farming land. 
    We needeth to secure surrounding resources to ourselves. My lord, shall thee beest able to lent us a hand?
    
    ARMS_RACE:
    We have suitable farmlands across X to feed everyone, rather than having enough men to protect those folks. 
    My lord, our realm would be pleased if we receive protection from thy men.
    
    TRIBAL_FEUD:
    There hast always been hostle relation between the warchief in this region. 
    Destroy other tribes in this province, my lord, and thee shall earn our respect.
    
    REGENCY(grand quest involves multiple players):
    
    '''

    '''
    Response to Threat (player defy village)
    
    GATHERING:
    By divines, god save us all!
    
    ARMS_RACE:
    Take these supplies and leave! Spare our women and children!    
    
    TRIBAL_FEUD:
    Barbarians! Thou art just like the rest of them!
    
    REGENCY(grand quest involves multiple players):
    Thee'll get squandered like a bug thou art, traitor.
    
    '''
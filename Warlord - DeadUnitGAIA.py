from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from functions.RebuildingTriggers import RebuildingTriggers
from model.buildings import BuildingInfo

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
scenario_name = "12warlords 0v1v25"
input_path = scenario_folder + scenario_name + ".aoe2scenario"
output_path = scenario_folder + scenario_name + " modify GAIA" + ".aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# print num of triggers
print("Number of triggers: " + str(len(source_trigger_manager.triggers)))

# Rearrange trigger (push to a new list)
identification_name = "Warlord - DeadUnitGAIA.py"
source_trigger_manager.triggers = RebuildingTriggers.rebuild_trigger(self="",
                                                                     source_trigger_manager=source_trigger_manager,
                                                                     identification_name=identification_name)
# start adding triggers
triggerStart = source_trigger_manager.add_trigger("9===" + identification_name + " Start===")

# Get map size
map_size = source_scenario.map_manager.map_size
print("map_size: " + str(map_size))

for playerId in range(1, 9, 1):
    # Add triggers for garrison CAP
    print("===P" + str(playerId) + "=============================================")
    modify_trigger = source_trigger_manager.add_trigger("P" + str(playerId) + "_GAR_CAP")
    modify_trigger.new_condition.timer(timer=1)
    for building in BuildingInfo:
        if building.IS_GAIA_ONLY is False:
            # print(str(building.ID) + "garri = " + str(building.GARRISON_CAP))
            modify_trigger.new_effect.modify_attribute(quantity=building.GARRISON_CAP, operation=Operation.SET,
                                                       source_player=playerId,
                                                       object_list_unit_id=building.ID,
                                                       object_attributes=ObjectAttribute.GARRISON_CAPACITY)

'''
Get all GAIA unit
'''
P1to6_units = source_scenario.unit_manager.get_player_units(player=1) + source_scenario.unit_manager.get_player_units(
    player=2) + source_scenario.unit_manager.get_player_units(player=3) + source_scenario.unit_manager.get_player_units(
    player=4) + source_scenario.unit_manager.get_player_units(player=5) + source_scenario.unit_manager.get_player_units(
    player=6)
GAIA_building = []
print(BuildingInfo.non_gaia())

'''
Add triggers for Garrisoning in
'''
create_garri_trigg = source_trigger_manager.add_trigger("GAIA_GAR_CREATE")
create_garri_trigg.new_condition.timer(timer=11)
for unit in P1to6_units:
    for buildingInfo in BuildingInfo.non_gaia():
        # make building untargetable
        if unit.unit_const == buildingInfo.ID:
            create_garri_trigg.new_effect.disable_unit_targeting(
                selected_object_ids=unit.reference_id
            )
        if buildingInfo.GARRISON_CAP > 0 and unit.unit_const == buildingInfo.ID:
            # print(unit)
            # GAIA_building.append(unit.reference_id)
            for playerId in range(1, 7, 1):
                create_garri_trigg.new_effect.create_garrisoned_object(
                    source_player=0,
                    object_list_unit_id=buildingInfo.ID,
                    object_list_unit_id_2=UnitInfo.VMDL.ID,
                    selected_object_ids=unit.reference_id
                )
            create_garri_trigg.new_effect.none()

'''
Now we teleport the sheep away to count GAIA razing for each players
'''
print("===TeleportAndCountRazing=============================================")
for playerId in range(1, 9, 1):
    # Add triggers for garrison CAP
    sheep_tele_trigg = source_trigger_manager.add_trigger(name="P" + str(playerId) + "_TeleSheep", looping=True,
                                                          enabled=True)
    sheep_tele_trigg.new_condition.own_objects(
        source_player=playerId,
        object_list=UnitInfo.SHEEP.ID,
        quantity=1
    )
    sheep_tele_trigg.new_effect.teleport_object(
        source_player=playerId,
        object_list_unit_id=UnitInfo.SHEEP.ID,
        location_x=249,
        location_y=1
    )
    count_raz_trigg = source_trigger_manager.add_trigger(name="P" + str(playerId) + "_CountSheepRz", looping=True,
                                                         enabled=True)
    count_raz_trigg.new_condition.objects_in_area(
        quantity=1,
        source_player=playerId,
        object_list=UnitInfo.SHEEP.ID,
        object_state=ObjectState.ALIVE,
        area_x1=248,
        area_x2=250,
        area_y1=0,
        area_y2=2
    )
    count_raz_trigg.new_effect.remove_object(
        source_player=playerId,
        object_list_unit_id=UnitInfo.SHEEP.ID,
        area_x1=248,
        area_x2=250,
        area_y1=0,
        area_y2=2,
        object_state=ObjectState.ALIVE,
    )
    count_raz_trigg.new_effect.tribute(
        quantity=-15,
        source_player=playerId,
        target_player=0,
        tribute_list=Attribute.WOOD_STORAGE
    )
    count_raz_trigg.new_effect.tribute(
        quantity=-10,
        source_player=playerId,
        target_player=0,
        tribute_list=Attribute.GOLD_STORAGE
    )
    count_raz_trigg.new_effect.tribute(
        quantity=-10,
        source_player=playerId,
        target_player=0,
        tribute_list=Attribute.STONE_STORAGE
    )
    count_raz_trigg.new_effect.tribute(
        quantity=-15,
        source_player=playerId,
        target_player=0,
        tribute_list=Attribute.FOOD_STORAGE
    )

# Add triggers for Garrisoning in
# for x in range(1, map_size, 1):
#     for y in range(1, map_size, 1):
#         create_garri_trigg = source_trigger_manager.add_trigger("GAIA_GAR_CREATE" + str(x*y))
#         create_garri_trigg.new_condition.timer(timer=11)
#         for building in BuildingInfo:
#             if building.IS_GAIA_ONLY is False and building.GARRISON_CAP > 0:
#                 for createGarriId in range(1, 6, 1):
#                     print("GAIA_GAR_CREATE" + str(x*y))
#                     create_garri_trigg.new_effect.create_garrisoned_object(
#                         source_player=0,
#                         object_list_unit_id=building.ID,
#                         object_list_unit_id_2=206,
#                         area_x1=x, area_x2=x, area_y1=y, area_y2=y
#                     )

triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

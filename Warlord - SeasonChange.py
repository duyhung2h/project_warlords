import random

from AoE2ScenarioParser.datasets.trigger_lists import ColorMood, ObjectClass, ObjectState
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from functions.RebuildingTriggers import RebuildingTriggers
from functions.indexing_file.indexing_file import IndexingFile
# File & Folder setup
from model.seasonal_bushes import SeasonalBushes
from model.seasonal_trees import SeasonalTrees

scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
scenario_name = "12warlords 0v1v29"
input_path = scenario_folder + scenario_name + ".aoe2scenario"
output_path = scenario_folder + scenario_name + " modify Seasons" + ".aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# print num of triggers
print("Number of triggers: " + str(len(source_trigger_manager.triggers)))

# Rearrange trigger (push to a new list)
identification_name = "Warlord - SeasonChange.py"
source_trigger_manager.triggers = RebuildingTriggers.rebuild_trigger(self="",
                                                                     source_trigger_manager=source_trigger_manager,
                                                                     identification_name=identification_name)
# start adding triggers
triggerStart = source_trigger_manager.add_trigger("9===" + identification_name + " Start===")

# Get map size
map_size = source_scenario.map_manager.map_size
print("map_size: " + str(map_size))

indexing_file = IndexingFile()
snow_tiles_log_file = open(indexing_file.uniquify(path="logs/snow_tiles_log/snow_tiles_log.txt"), "w")
write_by_log_file = False
unit_manager = source_scenario.unit_manager

''''''

# get all the terrains tiles (compiled in a list) in the map
originalTerrains = source_scenario.map_manager.terrain
map_manager = source_scenario.map_manager

'''
Define season transition time
'''


'''
Transform trees to correct seasonal variant
'''
print("Transform trees to correct seasonal variant")
trees_in_map_list = []
bushes_in_map_list = []
seasonal_trees_list = SeasonalTrees.get_seasonal_trees()
seasonal_bushes_list = SeasonalBushes.get_seasonal_bushes()

# Add the tree and bushes in the map to the seasonal list by chance
for unit in unit_manager.get_player_units(player=0):
    for seasonal_tree in seasonal_trees_list:
        # add tree oak to list with chances based on elevation
        if unit.rotation == seasonal_tree.SummerVariant and (
                unit.unit_const == 349 or unit.unit_const == 411):  # Oak, Oak Forest
            tile_below_unit = map_manager.get_tile(x=int(unit.x), y=int(unit.y))
            randomChance = ((random.random() - 0.4) ** (1 - (tile_below_unit.elevation - 2) / 5)).real
            if float(randomChance) > float(0.40):  # chances depends on elevation bro
                print(unit)
                trees_in_map_list.append(unit)
for unit in unit_manager.get_player_units(player=0):
    for seasonal_bush in seasonal_bushes_list:
        # add bushes to list with chances based on elevation
        if unit.rotation == seasonal_bush.SummerVariant and (
                unit.unit_const == 1053):  # Bush B
            tile_below_unit = map_manager.get_tile(x=int(unit.x), y=int(unit.y))
            randomChance = ((random.random() - 0.4) ** (1 - (tile_below_unit.elevation - 2) / 5)).real
            if float(randomChance) > float(0.40):  # chances depends on elevation bro
                print(unit)
                bushes_in_map_list.append(unit)

'''
create triggers that changes season manually (create ice patches and replace trees)

de-transition trigger should also be inside map-size loop
'''
trigg_winter = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter",
    enabled=True,
    looping=False
)
trigg_winter.new_condition.timer(
    timer=10,
)
trigg_winter.new_effect.display_instructions(
    source_player=0,
    message="Winter has come!",
    display_time=20,
    instruction_panel_position=1
)
trigg_winter.new_effect.change_color_mood(
    quantity=10,
    color_mood=ColorMood.WINTER
)
# Allowed terrain (ALL LANDS TERRAIN)
allowed_terrains = [0, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 36,
                    40, 41, 42, 45, 46, 48, 49, 50, 56, 60, 63, 64, 65, 66, 67, 70, 71, 72, 75, 76, 77, 78, 83, 88, 89,
                    100, 101, 102, 104, 105, 106, 110, 111, 112]
random_ice_facets = [1, 2, 3, 4, 5, 6]
# random_ice_facet = [5, 2, 3]

'''
random chances to create ice patch for every tiles
Also change tree seasonal variant

random chances would be higher depends on elevation:
if it's 0 or 1 or 2, 0%
> 0% chances start with ele 3

wolfram alpha: 
plot (x-0.3)^(1 - (<ele>-2)/5))
4 -> 9 -> 30 -> 52.5 -> 100

wolfram alpha: 
plot (x-0.4)^(1 - (<ele>-2)/5))
8% -> 17.5% -> 32.5% -> 52.5% -> 100%
'''
old_trigg_winter_snow_transition_y = trigg_winter
for y in range(0, map_size + 1, 1):
    trigg_winter_snow_transition_y = source_trigger_manager.add_trigger(
        name="ModifySeasonWinter_ST" + str(y),
        enabled=False,
        looping=False
    )
    # last wave activating current wave
    if 0 < y < map_size:
        old_trigg_winter_snow_transition_y.new_effect.activate_trigger(
            trigger_id=trigg_winter_snow_transition_y.trigger_id)
    if y == 0:
        trigg_winter.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_y.trigger_id)
    trigg_winter_snow_transition_y.new_condition.timer(timer=2)
    for terrain in originalTerrains:
        if terrain.y == y:
            randomChance = ((random.random() - 0.4) ** (1 - (terrain.elevation - 2) / 5)).real
            # print("X=" + str(terrain.x) + " Y=" + str(terrain.y) + " Elevation=" + str(
            #     terrain.elevation) + " Random chance=" + str(
            #     randomChance))
            if float(randomChance) > float(0.6):  # chances depends on elevation bro
                # print("PASS!")
                for allowed_terrain in allowed_terrains:
                    if terrain.terrain_id == allowed_terrain:
                        random_ice_facet = random.choice(random_ice_facets)
                        trigg_winter_snow_transition_y.new_effect.create_object(
                            object_list_unit_id=728,  # Ice, navigable
                            source_player=0,
                            location_x=terrain.x,
                            location_y=terrain.y,
                            facet=random_ice_facet
                        )
                        snow_tiles_log_file.write(
                            "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(
                                random_ice_facet) + "\n")
                        if terrain.elevation < 6:
                            continue
                        random_ice_facet = random.choice(random_ice_facets)
        elif terrain.y > y:
            break
    # Finally, add the trees in the list to the transition triggers
    for unit in trees_in_map_list:
        if y - 1 <= unit.y < y and y > 0:
            trigg_winter_tree_transition = source_trigger_manager.add_trigger(
                name="WinterTreeTransition_x=" + str(unit.x) + "y=" + str(unit.y),
                enabled=False,
                looping=False
            )
            # print("WinterTreeTransition_x=" + str(unit.x) + "y=" + str(unit.y))
            # activate (using last wave)
            old_trigg_winter_snow_transition_y.new_effect.activate_trigger(
                trigger_id=trigg_winter_tree_transition.trigger_id)
            # disable (using current wave)
            trigg_winter_snow_transition_y.new_effect.deactivate_trigger(
                trigger_id=trigg_winter_tree_transition.trigger_id)
            for seasonal_tree in seasonal_trees_list:
                if unit.rotation == seasonal_tree.SummerVariant:
                    trigg_winter_tree_transition.new_condition.objects_in_area(
                        area_x1=int(unit.x),
                        area_x2=int(unit.x),
                        area_y1=int(unit.y),
                        area_y2=int(unit.y),
                        source_player=0,
                        quantity=1,
                        object_group=ObjectClass.TREE,
                        object_state=ObjectState.ALIVE
                    )
                    trigg_winter_tree_transition.new_effect.remove_object(
                        source_player=0,
                        area_x1=int(unit.x),
                        area_x2=int(unit.x),
                        area_y1=int(unit.y),
                        area_y2=int(unit.y),
                        object_group=ObjectClass.TREE,
                        object_state=ObjectState.ALIVE
                    )
                    trigg_winter_tree_transition.new_effect.create_object(
                        object_list_unit_id=1249,  # Oak Autumn Snow
                        source_player=0,
                        facet=int(seasonal_tree.WinterVariant),
                        location_x=int(unit.x),
                        location_y=int(unit.y),
                    )
    # Finally, add the bushes in the list to the transition triggers
    for unit in bushes_in_map_list:
        if y - 1 <= unit.y < y and y > 0:
            trigg_winter_bush_transition = source_trigger_manager.add_trigger(
                name="WinterBushTransition_x=" + str(unit.x) + "y=" + str(unit.y),
                enabled=False,
                looping=False
            )
            # print("WinterBushTransition_x=" + str(unit.x) + "y=" + str(unit.y))
            # activate (using last wave)
            old_trigg_winter_snow_transition_y.new_effect.activate_trigger(
                trigger_id=trigg_winter_bush_transition.trigger_id)
            # disable (using current wave)
            trigg_winter_snow_transition_y.new_effect.deactivate_trigger(
                trigger_id=trigg_winter_bush_transition.trigger_id)
            for seasonal_bush in seasonal_bushes_list:
                if unit.rotation == seasonal_bush.SummerVariant:
                    trigg_winter_bush_transition.new_condition.objects_in_area(
                        area_x1=int(unit.x),
                        area_x2=int(unit.x),
                        area_y1=int(unit.y),
                        area_y2=int(unit.y),
                        source_player=0,
                        quantity=1,
                        object_group=ObjectClass.TREE,
                        object_state=ObjectState.ALIVE
                    )
                    trigg_winter_bush_transition.new_effect.remove_object(
                        source_player=0,
                        area_x1=int(unit.x),
                        area_x2=int(unit.x),
                        area_y1=int(unit.y),
                        area_y2=int(unit.y),
                        object_group=ObjectClass.TREE,
                        object_state=ObjectState.ALIVE
                    )
                    trigg_winter_bush_transition.new_effect.create_object(
                        object_list_unit_id=1054,  # Bush C
                        source_player=0,
                        facet=int(seasonal_bush.WinterVariant),
                        location_x=int(unit.x),
                        location_y=int(unit.y),
                    )
    old_trigg_winter_snow_transition_y = trigg_winter_snow_transition_y

triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

''''''

snow_tiles_log_file.close()

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

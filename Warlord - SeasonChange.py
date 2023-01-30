import random

from AoE2ScenarioParser.datasets.trigger_lists import ObjectClass, ObjectState, ColorMood, Operation
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from functions.RebuildingTriggers import RebuildingTriggers
from functions.indexing_file.indexing_file import IndexingFile
# File & Folder setup
from functions.random_chance_calculator import RandomChanceCalculator
from model.seasonal_bushes import SeasonalBushes
from model.seasonal_info import SeasonalInfo
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
Define season related classes
'''

random_chance_calculator = RandomChanceCalculator()
season_info = SeasonalInfo()
first_season = 3

'''
Define season transition time (in seconds)
'''

wave_transition_time = 2
season_transition_time = 120

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
            randomPassed = random_chance_calculator.get_tree_chance(elevation=tile_below_unit.elevation)
            if randomPassed:
                print(unit)
                trees_in_map_list.append(unit)
for unit in unit_manager.get_player_units(player=0):
    for seasonal_bush in seasonal_bushes_list:
        # add bushes to list with chances based on elevation
        if unit.rotation == seasonal_bush.SummerVariant and (
                unit.unit_const == 1053):  # Bush B
            tile_below_unit = map_manager.get_tile(x=int(unit.x), y=int(unit.y))
            randomPassed = random_chance_calculator.get_tree_chance(elevation=tile_below_unit.elevation)
            if randomPassed:
                print(unit)
                bushes_in_map_list.append(unit)

'''
change hp of existing props
'''
trigg_chnage_props_hp = source_trigger_manager.add_trigger(
    name="ChangePropsHP",
    enabled=True
)
for season_id in range(1, 5, 1):
    trigg_chnage_props_hp.new_effect.change_object_hp(
        source_player=0,
        operation=Operation.SET,
        quantity=1000,
        object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id)
    )
# declare main season trigger first
trigg_seasons = []
trigg_short_descriptions = []
for season_id in range(1, 5, 1):
    season_enabled = False
    if season_id == first_season:
        season_enabled = True
    season_name = season_info.get_season_name(season_id=season_id)
    trigg_season = source_trigger_manager.add_trigger(
        name="ModifySeason" + season_name,
        enabled=season_enabled,
        looping=False
    )
    trigg_seasons.append(trigg_season)
    '''
    Short description displaying season
    '''
    trigg_short_description = source_trigger_manager.add_trigger(
        name="ShortDescription" + season_name,
        display_on_screen=True,
        enabled=False,
        looping=False,
        short_description="~~~" + season_name + "~~~\n" + season_info.get_season_bonuses_info(season_id=season_id)
    )
    trigg_short_description.new_condition.player_defeated(source_player=0)
    trigg_short_descriptions.append(trigg_short_description)

for season_id in range(1, 5, 1):
    '''
    deactivate other season description
    '''
    for season_id2 in range(1, 5, 1):
        trigg_seasons[season_id - 1].new_effect.deactivate_trigger(trigger_id=trigg_short_descriptions[season_id2 - 1].trigger_id)
    trigg_seasons[season_id - 1].new_effect.activate_trigger(trigger_id=trigg_short_descriptions[season_id - 1].trigger_id)
    season_name = season_info.get_season_name(season_id=season_id)
    color_mood = 0
    if season_id == 1:
        color_mood = ColorMood.DEFAULT
    elif season_id == 2:
        color_mood = ColorMood.DESERT
    else:
        exec("color_mood = ColorMood." + season_name.upper())
    '''
    create triggers that changes season manually (create ice patches and replace trees)
    
    de-transition trigger should also be inside map-size loop
    '''
    trigg_seasons[season_id - 1].new_condition.timer(
        timer=season_transition_time,
    )
    trigg_seasons[season_id - 1].new_effect.display_instructions(
        source_player=0,
        message=season_name + " has come!",
        display_time=20,
        instruction_panel_position=1
    )
    trigg_seasons[season_id - 1].new_effect.change_color_mood(
        quantity=10,
        color_mood=color_mood
    )
    if season_id == 4:
        trigg_seasons[season_id - 1].new_effect.activate_trigger(trigger_id=trigg_seasons[0].trigger_id)
    else:
        trigg_seasons[season_id - 1].new_effect.activate_trigger(trigger_id=trigg_seasons[season_id].trigger_id)
    # Allowed terrain (ALL LANDS TERRAIN)
    allowed_terrains = season_info.get_allowed_terrains(season_id=season_id)
    random_ground_obj_facets = season_info.get_seasonal_ground_obj_facets(season_id=season_id)

    '''
    handle waves of generating season transition
    '''

    old_trigg_season_transition_y = None
    for y in range(0, map_size + 1, 1):
        trigg_season_transition_y = source_trigger_manager.add_trigger(
            name="Transition" + season_name + str(y),
            enabled=False,
            looping=False
        )
        if season_id != 4:
            for season_id2 in range(1, 5, 1):
                trigg_season_transition_y.new_effect.remove_object(
                    source_player=0,
                    object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id2),
                    area_x1=0,
                    area_x2=map_size-1,
                    area_y1=y,
                    area_y2=y
                )
            # trigg_season_transition_y.new_effect.damage_object(
            #     source_player=0,
            #     quantity=11,
            #     object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id2),
            #     area_x1=0,
            #     area_x2=map_size-1,
            #     area_y1=y,
            #     area_y2=y
            # )
            # trigg_season_transition_y.new_effect.heal_object(
            #     source_player=0,
            #     quantity=10,
            #     object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id2),
            #     area_x1=0,
            #     area_x2=map_size-1,
            #     area_y1=y,
            #     area_y2=y
            # )
        # last wave activating current wave
        if 0 < y < map_size:
            old_trigg_season_transition_y.new_effect.activate_trigger(
                trigger_id=trigg_season_transition_y.trigger_id)
        if y == 0:
            trigg_seasons[season_id - 1].new_effect.activate_trigger(trigger_id=trigg_season_transition_y.trigger_id)
        trigg_season_transition_y.new_condition.timer(timer=wave_transition_time)
        for terrain in originalTerrains:
            if terrain.y == y:
                randomPassed = random_chance_calculator.get_ground_prop_chance(
                    elevation=terrain.elevation,
                    season=season_id,
                )
                if randomPassed:  # chances depends on elevation bro
                    # print("PASS!")
                    for allowed_terrain in allowed_terrains:
                        if terrain.terrain_id == allowed_terrain:
                            for allowed_terrain2 in allowed_terrains:
                                if terrain.layer == allowed_terrain2 or terrain.layer == -1:
                                    random_facet = random.choice(random_ground_obj_facets)
                                    trigg_season_transition_y.new_effect.create_object(
                                        object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id),
                                        source_player=0,
                                        location_x=terrain.x,
                                        location_y=terrain.y,
                                        facet=random_facet
                                    )
                                    trigg_season_transition_y.new_effect.create_object(
                                        object_list_unit_id=season_info.get_seasonal_ground_obj_id(season_id=season_id),
                                        source_player=0,
                                        location_x=terrain.x,
                                        location_y=terrain.y,
                                        facet=random_facet
                                    )
                                    snow_tiles_log_file.write(
                                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(
                                            random_facet) + "\n")
                                    break
                            break
            elif terrain.y > y:
                break
        # Finally, add the trees in the list to the transition triggers
        for unit in trees_in_map_list:
            if y - 1 <= unit.y < y and y > 0:
                trigg_seasonal_tree_transition = source_trigger_manager.add_trigger(
                    name=season_name + "TreeTransition_x=" + str(unit.x) + "y=" + str(unit.y),
                    enabled=False,
                    looping=False
                )
                # print("seasonalTreeTransition_x=" + str(unit.x) + "y=" + str(unit.y))
                # activate (using last wave)
                old_trigg_season_transition_y.new_effect.activate_trigger(
                    trigger_id=trigg_seasonal_tree_transition.trigger_id)
                # disable (using current wave)
                trigg_season_transition_y.new_effect.deactivate_trigger(
                    trigger_id=trigg_seasonal_tree_transition.trigger_id)
                for seasonal_tree in seasonal_trees_list:
                    seasonal_tree_facet = -1
                    exec("seasonal_tree_facet = int(seasonal_tree." + season_name + "Variant)")
                    if unit.rotation == seasonal_tree.SummerVariant:
                        trigg_seasonal_tree_transition.new_condition.objects_in_area(
                            area_x1=int(unit.x),
                            area_x2=int(unit.x),
                            area_y1=int(unit.y),
                            area_y2=int(unit.y),
                            source_player=0,
                            quantity=1,
                            object_group=ObjectClass.TREE,
                            object_state=ObjectState.ALIVE
                        )
                        trigg_seasonal_tree_transition.new_effect.remove_object(
                            source_player=0,
                            area_x1=int(unit.x),
                            area_x2=int(unit.x),
                            area_y1=int(unit.y),
                            area_y2=int(unit.y),
                            object_group=ObjectClass.TREE,
                            object_state=ObjectState.ALIVE
                        )
                        trigg_seasonal_tree_transition.new_effect.create_object(
                            object_list_unit_id=season_info.get_seasonal_tree_id(season_id=season_id),
                            source_player=0,
                            facet=seasonal_tree_facet,
                            location_x=int(unit.x),
                            location_y=int(unit.y),
                        )
        # Finally, add the bushes in the list to the transition triggers
        for unit in bushes_in_map_list:
            if y - 1 <= unit.y < y and y > 0:
                trigg_seasonal_bush_transition = source_trigger_manager.add_trigger(
                    name=season_name + "BushTransition_x=" + str(unit.x) + "y=" + str(unit.y),
                    enabled=False,
                    looping=False
                )
                # print("seasonalBushTransition_x=" + str(unit.x) + "y=" + str(unit.y))
                # activate (using last wave)
                old_trigg_season_transition_y.new_effect.activate_trigger(
                    trigger_id=trigg_seasonal_bush_transition.trigger_id)
                # disable (using current wave)
                trigg_season_transition_y.new_effect.deactivate_trigger(
                    trigger_id=trigg_seasonal_bush_transition.trigger_id)
                for seasonal_bush in seasonal_bushes_list:
                    seasonal_bush_facet = -1
                    exec("seasonal_bush_facet = int(seasonal_bush." + season_name + "Variant)")
                    if unit.rotation == seasonal_bush.SummerVariant:
                        trigg_seasonal_bush_transition.new_condition.objects_in_area(
                            area_x1=int(unit.x),
                            area_x2=int(unit.x),
                            area_y1=int(unit.y),
                            area_y2=int(unit.y),
                            source_player=0,
                            quantity=1,
                            object_group=ObjectClass.TREE,
                            object_state=ObjectState.ALIVE
                        )
                        trigg_seasonal_bush_transition.new_effect.remove_object(
                            source_player=0,
                            area_x1=int(unit.x),
                            area_x2=int(unit.x),
                            area_y1=int(unit.y),
                            area_y2=int(unit.y),
                            object_group=ObjectClass.TREE,
                            object_state=ObjectState.ALIVE
                        )
                        trigg_seasonal_bush_transition.new_effect.create_object(
                            object_list_unit_id=season_info.get_seasonal_bush_id(season_id=season_id),
                            source_player=0,
                            facet=seasonal_bush_facet,
                            location_x=int(unit.x),
                            location_y=int(unit.y),
                        )
        old_trigg_season_transition_y = trigg_season_transition_y


triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

''''''

snow_tiles_log_file.close()

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

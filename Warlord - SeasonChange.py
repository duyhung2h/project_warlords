import random

from AoE2ScenarioParser.datasets.trigger_lists import ColorMood
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from functions.RebuildingTriggers import RebuildingTriggers
from functions.indexing_file.indexing_file import IndexingFile

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
scenario_name = "12warlords 0v1v27"
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

''''''

# get all the terrains tiles (compiled in a list) in the map
originalTerrains = source_scenario.map_manager.terrain

'''
create triggers that changes season manually (create ice patches and replace trees)
'''
trigg_winter = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter",
    enabled=True,
    looping=False
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
trigg_winter_snow_transition_1 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST1",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_2 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST2",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_3 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST3",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_4 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST4",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_5 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST5",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_6 = source_trigger_manager.add_trigger(
    name="ModifySeasonWinter_ST6",
    enabled=False,
    looping=False
)
trigg_winter_snow_transition_1.new_condition.timer(timer=5)
trigg_winter_snow_transition_2.new_condition.timer(timer=5)
trigg_winter_snow_transition_3.new_condition.timer(timer=5)
trigg_winter_snow_transition_4.new_condition.timer(timer=5)
trigg_winter_snow_transition_5.new_condition.timer(timer=5)
trigg_winter_snow_transition_6.new_condition.timer(timer=5)
# Allowed terrain (ALL LANDS TERRAIN)
allowed_terrains = [0, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 36,
                    40, 41, 42, 45, 46, 48, 49, 50, 56, 60, 63, 64, 65, 66, 67, 70, 71, 72, 75, 76, 77, 78, 83, 88, 89,
                    100, 101, 102, 104, 105, 106, 110, 111, 112]
random_ice_facets = [1, 2, 3, 4, 5, 6]
# random_ice_facet = [5, 2, 3]

'''
random chances to create ice patch for every tiles

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
for terrain in originalTerrains:
    randomChance = ((random.random() - 0.4) ** (1 - (terrain.elevation - 2) / 5)).real
    print("X=" + str(terrain.x) + " Y=" + str(terrain.y) + " Elevation=" + str(
        terrain.elevation) + " Random chance=" + str(
        randomChance))
    if float(randomChance) > float(0.6):  # chances depends on elevation bro
        print("PASS!")
        for allowed_terrain in allowed_terrains:
            if terrain.terrain_id == allowed_terrain:
                random_ice_facet = random.choice(random_ice_facets)
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_1.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.write(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_2.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.write(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_3.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.write(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_4.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.write(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_5.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.writelines(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
                if random.random() > randomChance:  # 1/6
                    trigg_winter_snow_transition_6.new_effect.create_object(
                        object_list_unit_id=728,  # Ice, navigable
                        source_player=0,
                        location_x=terrain.x,
                        location_y=terrain.y,
                        facet=random_ice_facet
                    )
                    snow_tiles_log_file.write(
                        "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";facet=" + str(random_ice_facet) + "\n")
                    # continue
trigg_winter.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_1.trigger_id)
trigg_winter_snow_transition_1.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_2.trigger_id)
trigg_winter_snow_transition_2.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_3.trigger_id)
trigg_winter_snow_transition_3.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_4.trigger_id)
trigg_winter_snow_transition_4.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_5.trigger_id)
trigg_winter_snow_transition_5.new_effect.activate_trigger(trigger_id=trigg_winter_snow_transition_6.trigger_id)

triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

''''''

snow_tiles_log_file.close()

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

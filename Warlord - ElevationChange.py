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
output_path = scenario_folder + scenario_name + " modify Elevation" + ".aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# print num of triggers
print("Number of triggers: " + str(len(source_trigger_manager.triggers)))

# Rearrange trigger (push to a new list)
identification_name = "Warlord - ElevationChange.py"
source_trigger_manager.triggers = RebuildingTriggers.rebuild_trigger(self="",
                                                                     source_trigger_manager=source_trigger_manager,
                                                                     identification_name=identification_name)
# start adding triggers
triggerStart = source_trigger_manager.add_trigger("9===" + identification_name + " Start===")

# Get map size
map_size = source_scenario.map_manager.map_size
print("map_size: " + str(map_size))

indexing_file = IndexingFile()
elevation_log_file = open(indexing_file.uniquify(path="logs/elevation_log/elevation.txt"), "w")
write_by_log_file = False

''''''

# get all the terrains tiles (compiled in a list) in the map
originalTerrains = source_scenario.map_manager.terrain

'''raise elevation (minimum 3) if it's not water/desert(unlayered)/gravel beach'''

allowed_terrains = [0, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 36,
                    40, 41, 42, 45, 46, 48, 49, 50, 56, 60, 63, 64, 65, 66, 67, 70, 71, 72, 75, 76, 77, 78, 83, 88, 89,
                    100, 101, 102, 104, 105, 106, 110, 111, 112]


for terrain in originalTerrains:
    if terrain.elevation < 3:
        for allowed_terrain in allowed_terrains:
            # if terrain.terrain_id == 14 and terrain.layer != -1:
            #     continue
            if terrain.terrain_id == allowed_terrain:
                print("PASS!")
                elevation_log_file.write(
                    "at x=" + str(terrain.x) + "; y=" + str(terrain.y) + ";elevation=" + str(terrain.elevation) + "\n")
                terrain.elevation = 3

triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

''''''

elevation_log_file.close()

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

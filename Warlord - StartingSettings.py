from AoE2ScenarioParser.datasets.trigger_lists import Operation
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from functions.RebuildingTriggers import RebuildingTriggers

# File & Folder setup

scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
scenario_name = "12warlords 0v1v15"
input_path = scenario_folder + scenario_name + ".aoe2scenario"
output_path = scenario_folder + scenario_name + " StartingSettings" + ".aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# print num of triggers
print("Number of triggers: " + str(len(source_trigger_manager.triggers)))

# Rearrange trigger (push to a new list)
identification_name = "Warlord - StartingSettings.py"
source_trigger_manager.triggers = RebuildingTriggers.rebuild_trigger(self="",
                                                                     source_trigger_manager=source_trigger_manager,
                                                                     identification_name=identification_name)
print(len(source_trigger_manager.triggers))
# start adding triggers
triggerStart = source_trigger_manager.add_trigger("9===" + identification_name + " Start===")

triggerSeparator = source_trigger_manager.add_trigger("---SCORE-CONTROL---------------")
for playerId in range(1, 9, 1):
    trigg_score_control_time = 21
    trigg_score_control = source_trigger_manager.add_trigger(
        enabled=True,
        looping=False,
        name="start_" + str(trigg_score_control_time) + "_P" + str(playerId) + "ScoreControl"
    )
    trigg_score_control.new_condition.timer(
        timer=trigg_score_control_time,
    )
    trigg_score_control.new_effect.modify_resource(
        tribute_list=98,
        source_player=playerId,
        operation=Operation.SET,
        quantity=0
    )
    trigg_score_control.new_effect.modify_resource(
        tribute_list=99,
        source_player=playerId,
        operation=Operation.SET,
        quantity=0
    )
    trigg_score_control.new_effect.modify_resource(
        tribute_list=184,
        source_player=playerId,
        operation=Operation.SET,
        quantity=0
    )
    trigg_score_control.new_effect.modify_resource(
        tribute_list=173,
        source_player=playerId,
        operation=Operation.SET,
        quantity=0
    )
    trigg_score_control.new_effect.modify_resource(
        tribute_list=174,
        source_player=playerId,
        operation=Operation.SET,
        quantity=0
    )

'''
Make Harbor invulnerable
'''

triggerEnd = source_trigger_manager.add_trigger("9===" + identification_name + " End===")

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)

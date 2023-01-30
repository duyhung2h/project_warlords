import ast
import pickle
import random

from AoE2ScenarioParser.datasets.trigger_lists import ColorMood

hallo = "((random.random() - 0.4) ** (1 - (terrain.elevation - 2) / 5)).real"

hallo = str(pickle.dumps(hallo))
print(hallo)
hallo = pickle.loads(ast.literal_eval(hallo))
i = hallo
print(type(i))
print(hallo)  # {'lol': 1, 'lel': 2}



for season_id in range(1, 5, 1):
    print(season_id)
mood = "mood2 = random.random()"
exec(mood)
stuff = mood2 + 0
print(stuff)
print("s" + str(int(exec(mood) + 0)))

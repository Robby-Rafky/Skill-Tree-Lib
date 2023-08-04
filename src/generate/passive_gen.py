import json

# can turn into module using pycharm
# have defaults for all parameters that get auto-filled when "editing" passives

with open("data/passiveData.json") as f:
    data = json.load(f)


def create_passive(passive_type, position):
    pass


def add_passive_name_description(name, description):
    pass


def add_passive_stats(stats, math, values, function):
    pass


def add_passive_requirements(required, connections):
    pass

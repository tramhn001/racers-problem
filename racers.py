def non_winners(races):
    winner_set = set()
    racer_set = set()

    for racers in races.values():
        racer_set.add(racers[0])
        racer_set.add(racers[1])
        racer_set.add(racers[2])
        winner_set.add(racers[0])
        
    not_winner = racer_set - winner_set
    
    return not_winner




races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()

print("All tests passed! Discuss time/space complexity if time remains")
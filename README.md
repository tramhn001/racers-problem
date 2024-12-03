# racers-problem
Racers problem to be completed during Industry Prep - Interview Prep

## Problem Statement

Your goal is to write a function to identify which drivers in a dataset have NOT won any race.

The dataset will be a dictionary. The keys will be the names of races and the values will be, the top three drivers to finish at that race. The first driver in the tuple will be the one who won the race. An example dataset is shown below:

```
races = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
```

In this example, Tsunoda won at Suzuka, Pérez won at Mexico City, and Hamilton won at Silverstone. Latifi and Stroll are present in the dictionary, but they did not win any of the races.

Write a function that accepts a `races` dicitonary and returns a *set* of all drivers that are present in that dictionary but did NOT win any race. For example, for the above dictionary, your function should return:

`{"Latifi", "Stroll"}`

See assertions in `racers.py` for more test cases.
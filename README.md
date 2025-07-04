# PathMap: Real-Time Evacuation Routing Under Dynamic Hazards

## Overview
PathMap is a real-time evacuation routing algorithm designed to improve safety and efficiency during emergencies such as fires, earthquakes, or other rapidly evolving hazards. Traditional pathfinding algorithms like A* and Dijkstra struggle with dynamic environments and crowd behaviors. PathMap addresses these challenges by incorporating hazard levels and crowd density into a locally adaptive routing algorithm.

## Problem Statement
In large buildings or complex environments, panic can lead individuals to choose suboptimal or dangerous evacuation routes. Existing algorithms are not equipped to adapt in real-time to new hazards or shifting crowd densities. PathMap provides dynamic rerouting by combining localized hazard data and crowd behavior into a responsive algorithm.

## Core Algorithm
PathMap modifies Dijkstra’s algorithm with a custom cost function that accounts for both hazard and crowd density:

```python
def get_cost(pos):
    x, y = pos
    return 1 + hazards[x, y] + crowd[x, y]
```

At each time step, the algorithm updates paths only in local regions affected by change, avoiding full-graph recomputation. This ensures both responsiveness and scalability.

## Test Plan & Results
PathMap was tested on a 30x30 grid simulating various hazard and crowd conditions. Three core test cases were evaluated:

| Test Case | Input Description | Expected Outcome | Actual Outcome |
|-----------|-------------------|------------------|----------------|
| Case 1    | Fire in corridor, agents near center | Agents route around fire | Avg egress time: 12.1s; no deadlocks |
| Case 2    | Dense crowd, multiple exits | Load-balanced routing | Even exit split; congestion avoided |
| Case 3    | Dynamic hazard mid-evacuation | Real-time rerouting | ~2s rerouting delay; successful replan |

## Runtime and Memory Performance
- **Platform**: Google Colab (Python 3.11)
- **Cycle time**: ~9 ms per update
- **Memory usage**: ~26 MB (measured via `tracemalloc`)
- **Algorithm Complexity**: O(n log k), where *k* is the size of the local update region

PathMap can efficiently plan for hundreds of agents in real-time.

## Trade-offs & Limitations
- May trade global optimality for local responsiveness
- Localized updates can occasionally overlook better global paths

## Future Work
- Extend support to 3D building plans
- Simulate mobility-impaired individuals
- Model smoke and structural collapse zones
- Accelerate core loop using C++
- Add Unity visualization and CSV export tools

## Repository Structure
```
pathmap/
├── pathmap.py              # Core routing algorithm
├── simulation.py           # Scenario tests and visualization
├── data/
│   ├── hazards.npy
│   └── crowd.npy
├── README.md
└── test_cases/
    ├── case1.json
    ├── case2.json
    └── case3.json
```

## Release
**Version**: `v1.0-final`

## License
MIT License

## GitHub
[https://github.com/Momo23456/pathmap](https://github.com/Momo23456/pathmap)

---
Feel free to clone, run, and contribute to the future development of PathMap!

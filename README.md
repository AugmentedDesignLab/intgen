# IntGen

This is a road intersection generator which works by using the [Netgenerate](https://sumo.dlr.de/userdoc/NETGENERATE.html) application from the [SUMO](https://sumo.dlr.de/userdoc/Sumo_at_a_Glance.html) traffic simulator as well as Unreal Engine using [SUMO2Unreal](https://github.com/AugmentedDesignLab/Sumo2Unreal). 

## Workflow

The workflow to obtain a road intersection as a SUMO road network file and on the Unreal Engine is shown in the figure below. ![workflow](https://github.com/ishaan95/intgen/blob/master/workflow_diagram.png "Workflow")

The intersection generator is run by running the python script test02.py.py with parameters as shown in the description below - 
```

```

As shown in the figure above, the intersection generator creates a text file. The text file looks like - 
```
(0, 0),(10.0, 0.0),[],laned4
(0, 0),(6.12323399574e-16, 10.0),[]
(0, 0),(-10.0, 1.22464679915e-15),[]
(0, 0),(-1.83697019872e-15, -10.0),[],laned6
```

The lines describe the start and end points of edges (incoming roads for an intersection). The intersection by default is spawned at (0,0). The square brackets describe the shape coordinates if needed. The last entry (laned4) describes the number of lanes for that particular edge. By default the edges are two laned but can be 4 or 6 lanes also.  



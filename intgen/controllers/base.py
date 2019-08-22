
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
import math

VERSION_BANNER = """
Generator of a road intersection specification text file %s
%s
""" % (get_version(), get_version_banner())
INCOMING = "Number of incoming roads for one intersection"
SPAWNPOINTX = "Spawning point of the intersection x co-ordinate"
SPAWNPOINTY = "Spawning point of the intersection y co-ordinate"
LENGTHROADS = "Length of incoming roads"
ROADLANES = "Number of lanes in all roads"
TURNLANES = "Number of turn lanes in all roads of the intersection"
CROSSINGS = "Crossings at the intersections"
CONTROL = "Traffic control option at the intersection"
SIDEWALKS = "Sidewalks on all incoming roads of an intersection. It automatically enables walking areas at an intersection."
PI = 3.14159265

class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Generator of a road intersection specification file'

        # text displayed at the bottom of --help output
        epilog = 'Usage: intgen <options> ind-roads --roaddetails <road_number> <lanes> <road_length>'

        # controller level arguments. ex: 'intgen --version'
        arguments = [ ( [ '-v', '--version' ], { 'action'  : 'version', 'version' : VERSION_BANNER } ),
                      (['-in', '--incoming_roads'], {'help' : INCOMING, 'type' : int, 'default' : 3}),
                      (['-spx', '--spawn_pointx'], {'help' : SPAWNPOINTX, 'type' : int, 'default' : 0}),
                      (['-spy', '--spawn_pointy'], {'help' : SPAWNPOINTY, 'type' : int, 'default' : 0}),
                      (['-l', '--length'], {'help' : LENGTHROADS, 'type' : int, 'default': 100}),
                      (['-tl', '--turn_lanes'], {'help' : TURNLANES, 'type' : int, 'default' : 0}),
                      (['-cr', '--crossings'], {'help' : CROSSINGS, 'type' : bool, 'default' : False}),
                      (['-tc', '--traffic_control'], {'help' : CONTROL, 'choices' : ['stop_signs', 'traffic_lights'], 'default' : 'stop_signs'}),
                      (['-si', '--sidewalks'], {'help' : SIDEWALKS, 'type' : bool, 'default' : False})]


    main_intersection_data = {}

    # function to calculate the start and end points of an incoming edge (shape coordinates for an edge element in the SUMO traffic simulator (Netgenerate application)).
    def shapeCoordinateCalculator(self, length, angle):
        edge_start_point = [self.app.pargs.spawn_pointx, self.app.pargs.spawn_pointy]
        edge_end_point = []
        xOffset = math.cos(angle * (PI/180)) * length;
        yOffset = math.sin(angle * (PI/180)) * length;
        edge_end_point.append(xOffset)
        edge_end_point.append(yOffset)
        return edge_start_point, edge_end_point

    def writeToJson(self):
        f = open('output.json', 'w+')
        f.write(self.app.render(self.main_intersection_data, 'output.json'))
        f.close()

    def add_road_intersection_data(self):
        self.main_intersection_data.update([('incoming_roads', self.app.pargs.incoming_roads),
        ('spawn_pointx', self.app.pargs.spawn_pointx), ('spawn_pointy', self.app.pargs.spawn_pointy), ('length', self.app.pargs.length),
        ('turn_lanes', self.app.pargs.turn_lanes), ('crossings', self.app.pargs.crossings), ('traffic_control', self.app.pargs.traffic_control)])

        for i in range(self.app.pargs.incoming_roads):
            ind_roads = {} # temporary individual road dicionary which will be appended to the main dictionary
            road_number = 'road' + str(i+1)
            initial_angle = 0
            angle_increment = 360/self.app.pargs.incoming_roads
            edge_start_point, edge_end_point = self.shapeCoordinateCalculator(self.app.pargs.length, i*angle_increment)
            ind_roads.update([('road_number', str(i+1)), ('lanes', 2), ('sidewalks', False), ('road_start_point', edge_start_point), ('road_end_point', edge_end_point)])
            self.main_intersection_data[road_number] = ind_roads
            del ind_roads

        self.writeToJson()

    def _default(self):
        """Default action if no sub-command is passed."""
        self.add_road_intersection_data()
        #self.app.args.print_help()

    # function to check if the number of lanes entered in the parameters is correct.
    def areLanesEven(self, a):
        inta = int(a);
        if ((inta % 2)!=0):
            msg = "%r is not an even number" % inta
            print(msg)
            return False
        return True

 ### parsing the individual roads road details option (-rd). The details given for this option will overwrite the default individual road details written.
    def parseRoadDetailsOption(self, angle_increment):
        ### Parse -rd argument and add to the main intersection dictionary.
        for j in self.app.pargs.roaddetails:
            ind_road = {}
            if (int(j[0]) > self.app.pargs.incoming_roads):
                print("Incoming roads less than given road number. This set of arguments not considered.")
                continue
            else:
                ind_road.update({'road_number' : j[0]})

            if (self.areLanesEven(j[1])):
                ind_road.update({'lanes' : int(j[1])})
            else:
                print("Failed to parse options.")
                return
            if (int(j[0]) > 0):
                edge_start_point, edge_end_point = self.shapeCoordinateCalculator((int(j[2])), (int(j[0])-1)*angle_increment) #angles of individual roads start from 0 degrees wrt the positive x-axis.
                ind_road.update([('road_start_point', edge_start_point), ('road_end_point', edge_end_point)])
            else:
                print("Invalid road number %d" % j[0])

            road_name = 'road' + str(int(j[0]))
            self.main_intersection_data[road_name] = ind_road
            del ind_road
        return

    # decorator to identify a subcommand.
    @ex(help='subcommand ind_roads',
        # sub-command level arguments. ex: 'Usage: intgen <options> ind-roads --roaddetails <road_number> <lanes> <sidewalks>'
        arguments=[
            ### add an option under subcommand namespace
            ( [ '-rd', '--roaddetails' ],
              { 'help' : 'All the details of an individual roads. This includes the road number, number of lanes, sidewalks (true/false) and road length',
                'action'  : 'append',
                'nargs' : 3,
                'metavar' : ('road_number', 'lanes', 'ind_length')})
        ],
    )
    def ind_roads(self):
        """Individual road details subcommand"""
        self._default()
        angle_increment = 360/self.app.pargs.incoming_roads
        if (self.app.pargs.roaddetails is not None):
            self.parseRoadDetailsOption(angle_increment)
        self.writeToJson()

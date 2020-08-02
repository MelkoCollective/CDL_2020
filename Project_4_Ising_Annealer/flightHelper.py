import csv
import networkx as nx
from collections import defaultdict
from dimod import BinaryQuadraticModel
from tabu import TabuSampler        
from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridSampler
import neal
import numpy as np

# Definitions required to support dependant Lagrange settings (see further below)
# Base Weight calculation


HomeBaseWeightOffset =  4

def makeBaseWeight(id):
    # Weight is calculated as: 10 ** ( id + offset +1 )
    #
    return( 10 ** ( id + HomeBaseWeightOffset + 1))


# Todo: Rename a "start" to a "break". 

class Start:

    def __init__(self, id, lab):
        self.id = id
        self.lab = lab

class Node:

    def isStart(self):
        return isinstance(self.obj,Start)
    
    def isSegment(self):
        return isinstance(self.obj,Segment)
    
    def __init__(self, obj ):
        if ( isinstance(obj,Segment)):
            self.id = obj.id
            self.lab = obj.lab
            self.obj = obj
            #print("Node %d is %s" % (self.id, self.lab))
        elif ( isinstance(obj,Start)):
            self.id = obj.id
            self.lab = obj.lab
            self.obj = obj
            #print("We have Start State %d" % (self.id))
        else:
            raise Exception("Error on type. Got %s" % (type(obj)))



# Home Base definitions
#
# Each valid home base is defined to be assigned its own Weight
# Weight is added on the first node and subtracted on the last node. If bases match, net 0 effect, no penalty
#
#
# Variations: Try LCA alone, ATH alone or both LCA and ATH
#
# 

# Segment Class

class Segment:

    def getUarrtime(self):
        return ((self.getUdeptime() + self.ft))
                
    def getUdeptime(self):
        return ((self.depday - 1) * 1440 + self.deptime)
    
    def setT(self, T):
        self.T = T
        self.UT1 = self.getUdeptime()
        self.UT2 = T - ( self.getUdeptime() + self.ft)
        #print( self.UT1, self.UT2, T, self.getUdeptime, self.getUarrtime)
        
    def getUT(self):
        return( self.T - self.ft)

    def getUT1(self):
        return( self.UT1)

    def getUT2(self):
        return( self.UT2)
    
    def setCI(self,ci):
        self.ci = ci
        
    def setCO(self,co):
        self.co = co
        
    def getCI(self):
        return self.ci
        
    def getCO(self):
        return self.co
        
    def __init__(self, id, lab, dep, arr, deptime, arrtime, depday, arrday, HomeBases):
        self.id = id
        self.lab = lab
        self.dep = dep
        self.arr = arr
        self.deptime = deptime
        self.arrtime = arrtime
        self.depday = depday
        self.arrday = arrday
        self.ft = (arrday-1) * 1440 + arrtime - ( (depday-1) * 1440 + deptime )
        self.UT1 = 0
        self.UT2 = 0
        self.T = 0
        self.ci = 0
        self.co = 0
        
        # Establish the weights associated with departure and arrival airport
        # 
        # Only apply a weight for base airports
        #
        
        self.DepBaseWgt = 0 #NotHomeBaseWeight
        self.ArrBaseWgt = 0 #NotHomeBaseWeight
        
        if ( self.dep in HomeBases):
            self.DepBaseWgt = makeBaseWeight(HomeBases[dep])
            
        if ( self.arr in HomeBases):
            self.ArrBaseWgt = makeBaseWeight(HomeBases[arr])
        
        #  Not required ... yet. The idea of carrying forward a weight from node to node may still be useful
        # self.TransitionBaseWeight = self.DepBaseWgt - self.ArrBaseWgt

# Create Start objects for adding as special edges


# print("Testing Node class")
# n1 = Node(Segment(1, "101", "LCA", "ATH", 600, 695, 1, 1))
# n2 = Node(State(N*N,"start"))
# print( n1.isStart() )
# print( n2.isStart() )
# n3 = Node(10)    # raises exception as expected
        

# Transition Weight
#
#
# TODO: Rethink the Segment and State classes.
#       We need to have Segments and States coexist in the edges.
#       Therefore we need a Vertex class that can be either a Segment or a Start State
# 

class TransitionWeight:
    
    def __init__(self,node1,node2):
        #
        # Detect the case we have:
        #
        # start-node
        # node-start
        # start-start
        #
        self.gap = 0
        if ( node1.isSegment()):   
            if ( node2.isStart()):     # C -> S
                self.TransitionBaseWeight = 0 # node1.obj.TransitionBaseWeight - node1.obj.ArrBaseWgt
            else:                      # C -> C : Standard Weight Transition
                self.TransitionBaseWeight = ConnectWeight(node1.obj,node2.obj).TransitionBaseWeight
        else:
            if ( node2.isSegment()):   # S -> C
                self.TransitionBaseWeight = 0 # node2.obj.TransitionBaseWeight - node2.obj.ArrBaseWgt
            else:                      # S -> S
                self.TransitionBaseWeight = 0
                
    
    
    
# Connection Weight
#
# Includes: Time gap, origin
#

class ConnectWeight:

    # 1) Connection Time gap. If negative make it zero. Zero gaps will be excluded from edges.  
    # 2) HomeBase switch weight
    # 3) Matching Airport connection: If does not match, assign NegativeWeight
    #

    def __init__ (self, seg1, seg2):
        
        #NegativeWeight = 10**(HomeBaseWeightOffset+1)  # TODO: Parametrize this definition

        # Include FT of nodes to allow for constraints on maximum flight time
        #
        
        self.ft = seg1.ft + seg2.ft
        
        # Include the time gap for the connection

        self.gap = gap(seg1,seg2)
        
        if ( self.gap < 0 ): 
            self.gap = 0 # abs(NegativeWeight + self.gap)

        # Connect Weight for Airports:
        #
        # bi,j: is the difference between the seg2.arr weight and seg1.dep weight
        # This is the TransitionalBaseWeight for the connection.
        #
        # TODO: Decide on abs value or signed
                    
        self.TransitionBaseWeight = seg2.ArrBaseWgt - seg1.DepBaseWgt
        
        # TODO: Decide how to deal with a gap when not connecting at the same airport
        
        if ( seg2.dep != seg1.arr ):
            self.gap = 0 # NegativeWeight;
        #print(self.__dict__)
        
def gap(seg1,seg2):
	return( seg2.depday * 1440 + seg2.deptime - (seg1.depday * 1440 + seg1.deptime + seg1.ft ))


# Constraints as functions so we can easily turn them on or off

class TripGen:
    
    def __init__(self,N,segments):
        self.N = N
        self.segments = segments
        
    # New test for constraint1- Works much better. Note how the coef are updated: += 
    def const_quad_nodes3(self,Name, Q, LG, coef_lin,coef_quad,coef_const):
        N = self.N
        count_lin = 0;
        count_quad = 0;
        for row in range(N):
            for u in range(N):
                indx = row * N + u
                Q[(indx,indx)] += (LG * coef_lin)
                for v in range(u+1,N):
                    jndx = row * N + v
                    Q[(indx,jndx)] +=  coef_quad * LG
                    count_quad+=1
        print(Name,LG, coef_lin,coef_quad,coef_const)
        print("Acted on : %d lins, %d quads" % (count_lin, count_quad))
        #print(Q)


     # Revised and Corrected
    # Coefficient handling corrected
    def const_quad_rows(self,Name, Q, LG, coef_lin,coef_quad,coef_const):
        N = self.N
        count_lin = 0;
        count_quad = 0;
        for row in range(N):
            origin = row * N
            for node in range(N):
                indx = origin + node
                Q[(indx,indx)] += (LG * coef_lin)
                count_lin+=1
                for row2 in range( row + 1, N):
                    jndx = row2 * N + node
                    Q[(indx,jndx)] +=  coef_quad * LG
                    count_quad+=1
        print(Name,LG, coef_lin,coef_quad,coef_const)
        print("Acted on : %d lins, %d quads" % (count_lin, count_quad))
    #print(Q)

    # Change: Dec Lin, Inc Quad for constraints
    def const_quad_states(self,Name, Q, LG, coef_lin, coef_quad, coef_const):
        N = self.N
        for row in range(N):
            rndx = N**2 + row  # N bits after the main nodes matrix
            Q[(rndx,rndx)] += (LG * coef_lin)
            for j in range(row+1, N):
                jndx = N**2 + j
                Q[(rndx,jndx)] +=  coef_quad * LG
        print(Name,LG, coef_lin,coef_quad,coef_const)
        #print(Q)

    # WIP: Reworking the loop. Need to consider consecutive rows.

    def const_edges_connect(self,Name, Q, LG, G):
        N = self.N
        segments = self.segments
        for row in range(N-1):
            row2 = row + 1
            for node in range(N):
                for node2 in range(N):
                    indx = row * N + node
                    jndx = row2 * N + node2

                    if not G.has_edge(segments[node],segments[node2]):

                        # Penalize the lack of edge
                        #print("Penalizing %d to %d, connection not allowed" % (node,node2))
                        Q[(indx,jndx)] += LG

        print(Name)
        #print(Q)

    # ================================================================
    # Return to base : penalizing on start and depenalizing on return
    # 
    # const_location_start : Will add the base weight of the airport
    # const_location_return: Will subtract base weight of the airport
    # 
    # a Net Zero means we have a cycle returning to the start airport
    #
    # ================================================================
    #    for n1,n2,data in G.edges(data=True):

    def const_location_start(self,Name, Q, LG, G):
        N = self.N
        segments = self.segments

        # for edges connecting a start to a segment install the base weight
        for s1,v1,cw in G.edges(data=True):

            for r in range(N):
                s = N*N + r
                for v in range(N):
                    sndx = s
                    vndx = r * N + v
                    if ( s1.id == s ) and (v1.id == segments[v].id):
                        Q[(sndx,vndx)] -= LG * segments[v].obj.DepBaseWgt
        print(Name)
        #print(Q)

    def const_location_return(self,Name, Q, LG, G):
        N = self.N
        segments = self.segments

        # for edges connecting a segment to a start retract the base weight
        for v1,s1,cw in G.edges(data=True):

            for r in range(2,N):
                s = N*N + r
                for v in range(N):
                    sndx = r
                    vndx = (r-1) * N + v  # Previous row node
                    if ( s1.id == s ) and (v1.id == segments[v].id):
                        Q[(vndx,sndx)] += LG * segments[v].obj.ArrBaseWgt

        print(Name)
        #print(Q)

        
    # Objective for minimizing non-flying time
    # Coefficients calculated for each segment
    # We use 
    # (Segment.getUT() ** 2) * coef_lin 
    # (Segment.getUT() * 2 * coef_quad
    # We do not apply a Lagrange for objectives
    #

    def objective_quad_nodes(self, Name, Q, coef_lin,coef_quad,coef_const):
        N = self.N
        segments = self.segments
        count_lin = 0;
        count_quad = 0;
        for row in range(N):
            for u in range(N):
                undx = row * N + u
                count_lin+=1
                Q[(undx,undx)] += (segments[u].obj.getUT() ** 2 * coef_lin) # Base line unallocated time
                #print("a%d" %(u)," = ", (segments[u].obj.getUT() ** 2 * coef_lin))
                for v in range(u+1,N):
                    vndx = row * N + v
                    # Base line unallocated time 
                    Q[(undx,vndx)] +=  coef_quad * segments[v].obj.getUT() 
                    #print("b%d,%d" % (u,v), " = ", coef_quad * segments[v].obj.getUT() )
                    # Minus pair contribution : - ( 1.UT2 + 2.UT1 ) time gap remains
                    Q[(undx,vndx)] += -  (segments[u].obj.getUT2()+segments[v].obj.getUT1()) # Removed coef_quad *
                    #print("b%d,%d" % (u,v), " plus ", -  (segments[u].obj.getUT2()+segments[v].obj.getUT1() ))
                    count_quad+=1
        print(Name,1, coef_lin,coef_quad,coef_const)
        print("Objective Acted on : %d lins, %d quads" % (count_lin, count_quad))
        #print(Q)
    # Objective for cancelling the gap when a cycle starts and replacing it with CheckIn time (1 to N+1)
    # or cancelling  the reaminder of unallocated time when a cycle ends (2 to N )

    def objective_quad_states(self, Name, Q, coef_lin, coef_quad, coef_const, G):

        for node1, node2 in G.edges(data=False):
            N = self.N
            segments = self.segments
            
            # Process start to segment (new cycle)

            if ( node1.isStart() and node2.isSegment()):

                for row in range(N):

                    sndx = N*N + row               # Start state per row
                    undx = row * N + node2.id - 1  # Node starting or continuing

                    # Case S to C : node2 is a start of a cycle
                    # Cancel UT1 and replace it with CheckIn time
                    #print("Node %d start, cancelling %d, adding %d" % ( node2.id, node2.obj.getUT1(), node2.obj.getCI()))
                    Q[(sndx,undx)] +=  coef_quad * ( node2.obj.getCI() - node2.obj.getUT1())

            # Process segment to start (end of a previous cycle)

            if ( node1.isSegment() and node2.isStart()):

                # We start at row 1 and refer to the previous row
                for row in range(1,N):

                    undx = (row - 1) * N + node1.id - 1  # Node ending a cycle
                    sndx = N*N + row                     # Start state per row

                    # Case C to S : node1 is the end of a cycle
                    # Cancel UT2 and replce it with CheckOut time
                    #print("Node %d end, cancelling %d, adding %d" % ( node1.id, node1.obj.getUT2(), node1.obj.getCO()))
                    Q[(undx,sndx)] +=  coef_quad * ( node1.obj.getCO() - node1.obj.getUT2())

        print(Name,coef_lin,coef_quad,coef_const)
        #print(Q)
        
    def print_trip(self,result):
        variables = result[0]
        energy = result[1]
        N = self.N
        segments = self.segments
        
        print("Energy %f" % (energy))
        sndx = N*N
        for row in range(N):
            origin = row * N
            state = 0
        
            if ( sndx+row < len(variables)):
                state = variables[sndx+row]

            for node in range(N):
                n = origin + node

                if ( variables[n] == 1):
                    if ( state == 1):
                        print("Start")
                    print(row, segments[node].obj.id, segments[node].obj.lab, segments[node].obj.dep, segments[node].obj.arr)
        print("---------------")

    # print(len(sampleset._record), sampleset._record[0])

    def print_all(self, sampleset, max = 3):
        for res in sampleset.data():
            self.print_trip(res)
            max = max - 1
            if ( max <= 0 ): break

# Load flight data files                
def loadFlts(targetDataSet, Atypes=[], depDay=0, HomeBases=[]):
    fseg = []
    firstRow=True
    flt_id = 0
    with open(targetDataSet, newline='') as csvfile:
        fltreader = csv.reader(csvfile, delimiter=',')
        for row in fltreader:
            if ( firstRow ):
                firstRow = False
            else:
                #  0    1    2    3      4      5      6      7      8      9      10     11    12    13    14
                # FID, FN, FDep, FArr, FDepD, FDepT, FArrT, FArrD, UDepD, UDepT, UArrT, UArrD, FFT, FTZD, Atype
                atype = row[14]
                if ((len(Atypes)==0) or (atype in Atypes)):
                    if ((depDay==0) or (depDay==int(row[8]))):
                        flt_id += 1
                        fseg.append(Node(Segment(flt_id, row[1], row[2], row[3], int(row[9]), int(row[10]), int(row[8]), int(row[11]),HomeBases)))
                #print(', '.join(row))
    return(fseg)

# Master class
class Anneal:

    # Default Test Case
    def buildSet1(self):
        segments=[]
        segments.append( Node(Segment(1, "X01", "LCA", "ATH", 600, 695, 1, 1,self.HomeBases)))
        segments.append( Node(Segment(2, "X02", "ATH", "LCA", 755, 845, 1, 1,self.HomeBases)))
        segments.append( Node(Segment(3, "X03", "LCA", "ATH", 875, 970, 1, 1,self.HomeBases)))
        segments.append( Node(Segment(4, "X04", "ATH", "LCA", 1035, 1125, 1, 1,self.HomeBases)))
        return(segments)

    def getN(self):
        return (self.N)

    def getG(self):
        return (self.G)
    
    def getT(self):
        return (self.T)
    
    def getHomeBases(self):
        return self.HomeBases
    
    def getHomeBaseWeightOffset(self):
        return self.HomeBaseWeightOffset

    def makeBaseWeight(self,id):
        # Weight is calculated as: 10 ** ( id + offset +1 )
        return( 10 ** ( id + HomeBaseWeightOffset + 1))

    # Create the anneal object
    def __init__(self,dataset="",homebases={},atypes=[],depday=1):
        self.HomeBases = homebases
        self.NotHomeBaseWeight = self.makeBaseWeight(len(self.HomeBases)+1) 
        
        
        # Order of magnitude for constraints -> Should be bigger than the base constraints magnitude
        self.LagrangeA = makeBaseWeight(len(self.HomeBases)+1)    
        # Order of magnitude for allowed edges
        self.LagrangeB = self.LagrangeA / 10        
        # order of magnitude for return to start location (uses base weights)
        self.LagrangeC = 1                                    
        
        # HomeBaseWeightOffset: Critical relative weights for home base management. Only change if you know what you are doing
        self.HomeBaseWeightOffset =  4 
        
        # Load the data
        
        #segments = loadFlts("DS1.csv", ["320"], HomeBases )
        if ( dataset != "" ):
            self.segments = loadFlts(dataset, Atypes=atypes, depDay = depday, HomeBases=self.HomeBases )
        else:
            self.segments = self.buildSet1()

        # Build the graph
        self.G = self.buildFltGraph()
        
        # Set N (number of segments)
        
        self.N = len(self.segments)

        print ("Minimum Dep", min(node.obj.deptime + ((node.obj.depday-1)) * 1440 for node in self.segments))
        print ("Maximum Arr", max(node.obj.arrtime + ((node.obj.arrday-1)) * 1440 for node in self.segments))

        # Set T as the range of time fully enclosing all segments, plus buffer
        self.T = max(node.obj.getUarrtime() for node in self.segments) + (2 * 1440) # We add buffer of 1 day prior and 1 day after

        
        #for s in self.segments:
        #    print(s.obj.__dict__)        
            
        for seg in self.segments:
            seg.obj.setT(self.T)
            seg.obj.setCI(60) # Checkin Time TODO: Parameterize this
            seg.obj.setCO(30) # Check out time. TODO: Parameterize this
            #print( seg.obj.id, seg.obj.getUT1(), seg.obj.getUT2(), seg.obj.getUT(), seg.obj.ft,seg.obj.getUT()+seg.obj.ft )

        # Create N + 1 row states.
        # The +1 serves to ensure the last row will be checked for return to base

        state_origin = self.N*self.N;
        self.states = []
        for s in range(self.N+1):
            self.states.append(Node(Start(state_origin+s,"start")))
            
            
        # Add edges dealing with start status bits
        #
        # The C to C has been already covered
        # TODO: Generalize to use 1 method for all
        #

        # C to S
        #print("C to S")
        for seg in self.segments:
            for start in self.states:
                self.G.add_weighted_edges_from([(seg,start, TransitionWeight(seg,start) )])

        # S to C
        #print("S to C")
        for start in self.states:
            for seg in self.segments:
                if seg.obj.dep in self.HomeBases:
                    self.G.add_weighted_edges_from([(start,seg, TransitionWeight(start,seg) )])

        # S to S
        #print("S to S")
        for start in self.states :
            for start2 in self.states:
                if ( start != start2 ):
                    self.G.add_weighted_edges_from([(start,start2, TransitionWeight(start,start2) )])

    # Prepare the QUBO
    def prepare(self, 
                cons_1_on = True, 
                cons_2_on = True, 
                cons_3_on = True, 
                cons_4_on = True, 
                cons_5_on = True, 
                objective_1_on = True , 
                objective_2_on = True):
            
        self.tg = TripGen(self.N, self.segments )

        # Prepare the QUBO

        self.Q = defaultdict(int)


        # Saving some time merging code...
        Q = self.Q
        LagrangeA = self.LagrangeA
        LagrangeB = self.LagrangeB
        LagrangeC = self.LagrangeC
        N = self.N
        G = self.G
        tg = self.tg
        
        # Constraint 1 : The total number of selected nodes must be = N
        # 
        #

        if (cons_1_on):
            c_l = -1
            c_q =  2 
            c_c = N**2
            tg.const_quad_nodes3("Constraint 1: There must be exactly N selected nodes overall", Q, LagrangeA, c_l, c_q, c_c )

        # Constraint 2 : Each node is selected in one and only one row 
        # 
        # 

        if (cons_2_on):
            c_l = -1 
            c_q = 2 
            c_c = 1
            tg.const_quad_rows("Constraint 2: Node selected only in one row", Q, LagrangeA, c_l, c_q, c_c )


        # Constraint 3 : There must be at least one start bit set 
        #               
        # constraint :

        if (cons_3_on):
            c_l = -3 
            c_q = 2 
            c_c = 0
            tg.const_quad_states("Constraint 3: At least one start state", Q, LagrangeA, c_l, c_q, c_c )

        # Constraint 4 : Each 2 consecutive row nodes selected must be part of edges 
        #                Penalize disallowed connections
        #

        if (cons_4_on):
            tg.const_edges_connect("Constraint 4: Only allowed edges to connect", Q, LagrangeB, G)

        # Constraint 5 : Must return to starting point
        #
        # We add +W at a start and -W at the end

        if (cons_5_on):
            tg.const_location_start("Constraint 5a: Starting location request return to same location", Q, LagrangeC, G)
            tg.const_location_return("Constraint 5b: Confirm returning to start lcoation", Q, LagrangeC, G)

        # Objectives

        # Initial Concepts
        #
        # T = time range that fully contains the segments of the problem. We can calculate this by taking Max(ArrTime)-Min(DepTime)
        # FT = Flight Time (duration) of each node
        # 
        # We are interested in optimizing the time between nodes
        #
        # For this purpose we want to be able to :
        #
        # Add the time gap between nodes
        # When there is a new cycle starting we want to disregard this gap and substitute the Checkin and Checkout times
        # 
        # Since we can only consider two Qubits at a time within our Quadratic equations we need a way to 
        # negate the time gap between two nodes of two separate cycles (since they are not connected)
        #
        # To be more specific, we would like to code a conditional penalty as:
        #
        #   (1 - Xs) x Gap x( XiXj ) + (Checkin+CheckOut) x XsXiXj
        #
        #   Xs is the start variable, 1 = start, 0 = continuation
        #   Xi, Xj are the selected node pair
        #
        # However, we cannot have 3 qubits for the quadratic methodology
        #
        # So we introduce a definition of "Undefined Time" (UT), which, added to "non-productive time" will total 
        # the amount to minimize. "Undefined time" is composed of the time prior to the departure time of a segment plus
        # the time after the segment. 
        #
        # UT = T - FT : So in short the infinite time in which the segment sits in, minus the time it is using.
        #
        # To avoid playing with Inifinity, we bind the segments to a fixed time range between -1 day prior to earliest segment 
        # start up to + 1 day after the latest arrival
        #
        # By contributing UT by default for each segment, but deducting it when we have confirmation of the usage of time
        # between two nodes we then have the ability to individually deal with new cycles, or cycle continuation with only
        # using 2 variables. However, we will need to seperate contribution calculations:
        #
        #   1 for the start of a new cycle: Negate UT prior to the segment and replace it with CI/CO
        #   2 for continuation nodes, A to B : Negate UT prior to B, Negate UT after A and replace with the time gap between A and B
        #
        # UT values (UT1 prior to a segment and UT2 after a segment) can be precalculate for each segment
        # CI/CO are weights placed on edges between Start nodes and Segment nodes
        # Gaps are weights placed on edgs between two segments
        #
        # 

        if ( objective_1_on ):
            # Objective 1 - Each node selected contributes
            # Solved Quad -> c_l = UT**2, c_q = 2 * UT, c_c = 0
            c_l = 1
            c_q = 2 
            c_c = 0
            tg.objective_quad_nodes("Objective 1: Base line unallocated time", Q, c_l,c_q,c_c)

        if ( objective_2_on ):
            # Objective 2 - Each S-C combination cancels time gap by 
            # Solved Quad -> c_l = UT**2, c_q = 2 * UT, c_c = 0
            c_l = 1
            c_q = 2 
            c_c = 0
            tg.objective_quad_states("Objective 2: Implement CI, gap and CO cancelling unallocated time", Q, c_l,c_q,c_c,G)


        #print(Q)
        return (True)
      
            
    # Solver
    def solve(self, 
              useQPU=False, 
              useNeal=False, 
              useHyb=True,
              time_limit = 10,
              num_reads = 100,
              chain_strength = 10000):
        
        Q = self.Q
        BQM_offset = 0 # TODO: Use the accumulated quadratic constants from the constraints

        bqm = BinaryQuadraticModel.from_qubo(Q, offset=BQM_offset)

        self.sampleset = None
        
        # Call the requested solver
        
        if ( useQPU ):
            print("Solving using the DWaveSampler on the QPU...")
            sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
            sampleset = sampler.sample_qubo(Q, num_reads=num_reads,chain_strength = chain_strength)
        elif ( useHyb ): 
            print("Solving using the LeapHybridSolver...")
            sampler = LeapHybridSampler()
            sampleset = sampler.sample(bqm, time_limit = time_limit)
        elif ( useNeal ): 
            print("Solving using the SimulatedAnnealing...")
            sampler = neal.SimulatedAnnealingSampler()
            sampleset = sampler.sample(bqm, num_reads = num_reads)
        else:
            print("Solving using the TabuSampler...")
            sampler = TabuSampler()
            sampleset = sampler.sample(bqm, num_reads = num_reads)

        self.sampleset = sampleset
        
        count = 0
        for res in self.sampleset.data(): count += 1
        
        return (count)

    def print_all(self,max=3):
        self.tg.print_all(self.sampleset,max)
    
    def getRevMatrix(self,M):
        R = np.zeros((self.N,self.N))
        
        for s1,s2,cw in self.G.edges(data=True):
            if ( s1.isSegment() and s2.isSegment() and (M[s1.id-1,s2.id-1] == 1) ):
                R[s1.id-1,s2.id-1] = gap(s1.obj,s2.obj) #cw.gap;
        return(R)                
    
    def getAdjMatricesB(self):
        return( self.getAdjMatrices(weights=False))
    
    def getAdjMatricesW(self):
        return( self.getAdjMatrices(weights=True))

    # Obtain the Adjacency Matrix from the results sampled producing either weights (True) or Binary (False)
    def getAdjMatrices(self, weights=False):
        
        # Calculate Each adjacency Matrix for each result

        allMatrices = []
        N = self.N
        
        
        for result in self.sampleset.data():

            AdjMatrix = np.zeros((N,N))

            # For each pair of connecting nodes record the time gap between them
            # This excludes "apparently" consecutive nodes that are separated by a "Start".

            variables = result[0]
            sndx = N*N

            # For each row until N-1 
            # Assign the gap between node 1 and the following node 2 to the AdjMatrix if they are connected

            for r in range(N-1):
                r2 = r+1

                # Get the start state of the next node
                state = 0
                if ( sndx+r2 < len(variables)):
                    state = variables[sndx+r2]

                # If it is not a start node, then node1 and node2 connect

                #if ( state == 0 ):
                for node1 in range(N):
                    n1 = r * N + node1
                    if ( variables[n1] == 1):
                        for node2 in range(N):
                            n2 = r2 * N + node2
                            if (( variables[n2] == 1)and(node1 != node2)):
                                if ( weights == True):
                                    AdjMatrix[node1,node2] = gap(self.segments[node1].obj,self.segments[node2].obj)
                                else:
                                    AdjMatrix[node1,node2] = 1 # gap(segments[node1].obj,segments[node2].obj)


            allMatrices.append([result,AdjMatrix])
            
        return(allMatrices)

    
    # Build graph from segments for viewing
    def buildViewGraph(self):
        segments = self.segments
        G = nx.DiGraph()
        for n1 in segments:
            for n2 in segments:
                if ( n1.id != n2.id ):
                    # Prevent connections when gaps are 0 or negative
                    cw = ConnectWeight(n1.obj,n2.obj)
                    if ( cw.gap > 0 ):
                        G.add_weighted_edges_from([(n1.id,n2.id, cw.gap  )])
        return G

    # build graph from segments for processing
    def buildFltGraph(self):
        segments = self.segments
        G = nx.DiGraph()
        for n1 in segments:
            for n2 in segments:
                if ( n1.id != n2.id ):
                    # Prevent connections when gaps are 0 or negative
                    cw = ConnectWeight(n1.obj,n2.obj)
                    if ( cw.gap > 0 ):
                        G.add_weighted_edges_from([(n1,n2, cw  )])
        return G    
  
    def getCost(self,M,res):
        
        # Cost = T * (CI * CO) + FT + Gaps
        
        ft = 0
        for s in self.segments:
            ft += s.obj.ft
        
        T = 0
        first = True
        for st in range(self.N):
            sndx = self.N * self.N + st
            if ( first or (res[0][sndx] == 1)): 
                T = T + 1
            first = False
            
        CI = 60
        CO = 30
        
  
        cost = M.sum() + T * (CI+CO) + ft
                
        #print(T, CI, CO, ft, M.sum(), cost)
        
        return(cost)
        
    
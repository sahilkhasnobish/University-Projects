from common import *
"""
Sahil Khasnobish - 190990560
Sterling Fullerton - 190942730
"""
class Node:
    def __init__(self, ID, networksimulator, costs):
        self.myID = ID
        self.ns = networksimulator
        num = self.ns.NUM_NODES
        self.distanceTable = [[0 for i in range(num)] for j in range(num)]
        self.routes = [0 for i in range(num)]
        self.node_costs = costs
        self.neighbours = []
        # you implement the rest of constructor

        # make a new packet, interate loop
        for i in range(num):
            # Do not schedule same source and destination
            if i != self.myID:
                # Do not shedule unconnected nodes
                if self.ns.connectcosts[self.myID][i] != self.ns.INFINITY:
                    new_packet = RTPacket(self.myID, i, costs)
                    self.ns.tolayer2(new_packet)

            # Update Initial Distance Tables for uncalculated distances
            for j in range(num):
                if i != j:
                    self.distanceTable[i][j] = self.ns.INFINITY
                else:
                    self.distanceTable[i][j] = 0

        # Initial Distance Table Values for known distances
        self.distanceTable[self.myID] = self.ns.connectcosts[self.myID]

        #find all neighbours
        for n in range(num):
            if (self.distanceTable[self.myID][n]<self.ns.INFINITY and self.distanceTable[self.myID][n]>0):
                self.neighbours.append(n)

    def recvUpdate(self, pkt):
        self.distanceTable[pkt.sourceid] = pkt.mincosts

        # you implement the rest of it
        change = False
        dist = [self.ns.INFINITY] * self.ns.NUM_NODES
        dist[pkt.destid] = 0
        sptSet = [False] * self.ns.NUM_NODES

        for i in range(self.ns.NUM_NODES):
            minn = self.ns.INFINITY
            u = None
            for v in range(self.ns.NUM_NODES):
                if dist[v] < minn and sptSet[v] == False:
                    minn = dist[v]
                    u = v

            #Skip if there is no min_index
            if u == None:
                continue

            #mark node as visited
            sptSet[u] = True

            for v in range(self.ns.NUM_NODES):
                if self.distanceTable[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.distanceTable[u][v]:
                    dist[v] = dist[u] + self.distanceTable[u][v]
                    self.routes[v] = self.neighbours[0]
        
        if self.distanceTable[pkt.destid] != dist:
            self.distanceTable[pkt.destid] = dist
            change = True
        
        if change:
            for d in range(self.ns.NUM_NODES):
                if self.distanceTable[self.myID][d] > 0 and self.distanceTable[self.myID][d] < self.ns.INFINITY:
                    new_pkt = RTPacket(self.myID, d, self.distanceTable[self.myID])
                    if self.ns.connectcosts[self.myID][d] != self.ns.INFINITY:
                        self.ns.tolayer2(new_pkt)

        return
    
    def printdt(self):
        print("   D"+str(self.myID)+" |  ", end="")
        for i in range(self.ns.NUM_NODES):
            print("{:3d}   ".format(i), end="")
        print()
        print("  ----|-", end="")
        for i in range(self.ns.NUM_NODES):            
            print("------", end="")
        print()    
        for i in range(self.ns.NUM_NODES):
            print("     {}|  ".format(i), end="" )
            
            for j in range(self.ns.NUM_NODES):
                print("{:3d}   ".format(self.distanceTable[i][j]), end="" )
            print()            
        print()
        

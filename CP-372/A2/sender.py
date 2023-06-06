from common import *
"""
Sahil Khasnobish - 190990560
Sterling Fullerton - 190942730
"""
class sender:
    RTT = 20

    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum.'''

        if packet.checksum != checksumCalc(packet):
            return True
        return False


    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side
        '''
        if self.last_packet.seqNum == packet.ackNum:
            return False
        return True
 
    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''
        self.seqNum = self.packets_sent % 2
        return 

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None
        '''
        self.last_packet = None
        self.packets_sent = 0
        self.packets_ackd = 0
        self.seqNum = 0
        self.last_ack = None
        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.
        '''
        self.networkSimulator.udtSend(self.entity, self.last_packet)
        self.networkSimulator.startTimer(self.entity, self.RTT*2)
        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        '''
        if self.packets_sent == self.packets_ackd:

            packet = Packet(self.seqNum, 0, 0, message.data)
            packet.checksum = checksumCalc(packet)

            self.networkSimulator.udtSend(self.entity, packet)
            self.networkSimulator.startTimer(self.entity, self.RTT)
            self.last_packet = packet
            self.packets_sent += 1
            self.getNextSeqNum()
        return
 
    
    def input(self, packet):

        '''If the acknowlegement packet isn't corrupted or duplicate, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.

        In the case of duplicate or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.
        '''

        if (not (self.isCorrupted(packet) or self.isDuplicate(packet))):
            self.last_ack = packet
            self.networkSimulator.stopTimer(self.entity)
            self.getNextSeqNum()
            self.packets_ackd += 1

        return 

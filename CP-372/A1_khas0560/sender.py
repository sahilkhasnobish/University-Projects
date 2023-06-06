from common import *

class sender:
    RTT = 20
    
    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum.'''
        if packet.checksum == (checksumCalc(packet.payload) + packet.seqNum + packet.ackNum):
            return False
        return True

    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side'''
        '''
        if len(self.packet_list_ack)>0:
            if packet.ackNum == self.packet_list[-1].seqNum:
                return True
        else:
            if packet.ackNum == self.seqNum:
                return True

        '''''

        if packet.ackNum == 1 - self.packet_list[-1].seqNum:
            return True
        return False

    def getNextSeqNum(self):
        '''generate the next sequence number to be used.'''
        self.seqNum = 1 - self.packet_list[-1].seqNum
        return

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None'''
        self.packet_list = []
        self.packet_list_ack = []
        self.packet = None
        self.seqNum = 0
        self.prevSeqNum = 0
        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.'''
        self.networkSimulator.stopTimer(self.entity)
        self.networkSimulator.udtSend(self.entity, self.packet_list[-1])
        self.networkSimulator.startTimer(self.entity, self.RTT*2)
        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit'''

        #convert message (if Message Object) to string data because issues
        if isinstance(message, Message):
            message = message.data

        packet = Packet(
            self.seqNum,                            #seqNum
            0,                                      #ackNum
            checksumCalc(message) + self.seqNum,    #checksum
            message                                 #payload
        )

        self.networkSimulator.udtSend(self.entity, packet)
        self.networkSimulator.startTimer(self.entity, self.RTT)
        self.packet_list.append(packet)
        self.prevSeqNum = self.seqNum
        self.getNextSeqNum()

        return
 
    
    def input(self, packet):
        '''If the acknowlegement packet isn't corrupted or duplicate, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.

        In the case of duplicate or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.'''


        #if not ((self.isCorrupted(packet) or self.isDuplicate(packet))):


        if (self.isCorrupted(packet) == False) and (self.isDuplicate(packet) == False):
            self.networkSimulator.stopTimer(self.entity)
            self.getNextSeqNum()
            self.packet_list_ack.append(packet)
        return

from common import *
"""
Sahil Khasnobish - 190990560
Sterling Fullerton - 190942730
"""
class receiver:

    def isCorrupted (self, packet):
       '''Checks if a received packet (acknowledgement) has been corrupted
       during transmission.
       Return true if computed checksum is different than packet checksum.'''

       if packet.checksum != checksumCalc(packet):
           return True
       return False

    def isDuplicate(self, packet):
        '''checks if packet sequence number is the same as expected sequence number'''
        if self.last_packet == packet:
            return True
        return False
    
    def getNextExpectedSeqNum(self):
        '''The expected sequence numbers are 0 or 1'''
        self.seqNum = 1 - self.seqNum
        return
    
    
    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: "+str(self.entity))


    def init(self):
        '''initialize expected sequence number'''
        self.seqNum = 0
        self.last_packet = None
        self.packets_acked = 0
        self.lastAckNum = 1
        self.last_seq_num = 0
        self.last_packet_ack = None
        return
         

    def input(self, packet):
        '''This method will be called whenever a packet sent 
        from the sender arrives at the receiver. If the received
        packet is corrupted or duplicate, it sends a packet where
        the ack number is the sequence number of the  last correctly
        received packet. Since there is only 0 and 1 sequence numbers,
        you can use the sequence number that is not expected.
        
        If packet is OK (not a duplicate or corrupted), deliver it to the
        application layer and send an acknowledgement to the sender
        '''

        if self.isCorrupted(packet) or self.isDuplicate(packet):

            packet.ackNum = self.last_seq_num
            packet.seqNum = 0
            packet.payload = ""
            packet.checksum = checksumCalc(packet)

            #Reply with corrupt packet
            self.networkSimulator.udtSend(self.entity, packet)
            self.getNextExpectedSeqNum()
        else:
            #Send to application Layer
            self.last_seq_num = packet.seqNum
            self.networkSimulator.deliverData(self.entity, packet.payload)
            self.packets_acked % 2
            packet_ack = Packet(0, packet.seqNum, 0)
            packet_ack.checksum = checksumCalc(packet_ack)

            #Reply with Ack
            self.networkSimulator.udtSend(self.entity, packet_ack)
            self.last_packet_ack = packet_ack
            packet.ackNum = 1 - packet.ackNum
            self.packets_acked += 1

            self.lastCorrectPacket = packet
            self.getNextExpectedSeqNum()

        return

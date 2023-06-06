from common import *

class receiver:

    def isCorrupted(self, packet):
        ''' Checks if a received packet has been corrupted during transmission.
        Return true if computed checksum is different than packet checksum.'''
        if packet.checksum == (checksumCalc(packet.payload) + packet.seqNum + packet.ackNum):
            return False
        return True
   
    def isDuplicate(self, packet):
        '''checks if packet sequence number is the same as expected sequence number'''
        if packet.seqNum == self.seqNum: 
            return False
        return True
    
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
        self.lastCorrectPacket = None
        self.seqNum = 0
        self.lastAckNum = 1
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
            print("corrupted!", str(packet))
            packet.ackNum = self.seqNum #last correct seqNum
            packet.seqNum = 1 - self.seqNum #unexpected seqNum
            self.networkSimulator.udtSend(self.entity, packet) #Reply with corrupt Ack
        else:
            #Send to application Layer
            self.networkSimulator.deliverData(self.entity, packet.payload)

            #Get next AckNum
            self.lastAckNum = 1 - self.lastAckNum

            #Reply with Ack
            self.networkSimulator.udtSend(self.entity, 
                Packet(
                    0,                  #seqNum (will always be 0, this is an Ack)
                    self.lastAckNum,    #ackNum (alternate 0, 1 for each ack)
                    self.lastAckNum     #checksum will be whatever ack num is
                ))

            self.lastCorrectPacket = packet
            self.getNextExpectedSeqNum()

        
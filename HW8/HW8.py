import socket
import struct
import binascii

class Udphdr:
    def __init__(self, source_port, destination_port, length, check):
        self.source_port = source_port
        self.destination_port = destination_port
        self.length = length
        self.check = check

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.source_port, self.destination_port)
        packed += struct.pack('!H', self.length)
        packed += struct.pack('!H', self.check)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udphdr):
    return unpacked_udphdr[0]

def getDstPort(unpacked_udphdr):
    return unpacked_udphdr[1]

def getLength(unpacked_udphdr):
    return unpacked_udphdr[2]

def getChecksum(unpacked_udphdr):
    return unpacked_udphdr[3]


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
    .format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), 
    getLength(unpacked_udphdr),getChecksum(unpacked_udphdr)))
# https://github.com/zxmarcos/xb_monitor/blob/master/ttx_monitor/Hook.cpp#L500
#
#	lpStat->cbInQue += 8; 
# 	replyBuffer.push(0x76);
#	replyBuffer.push(0xfd);
#	replyBuffer.push(0x08);
#	replyBuffer.push(control_byte_0());
#	replyBuffer.push(control_byte_1());
#	replyBuffer.push(control_byte_2());
#	replyBuffer.push(control_byte_3());
#	replyBuffer.push(0x42);

import serial
import binascii

ser = serial.Serial(
    port='/dev/tty.usbserial-1430',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = None
)

def buttons(b0, b1, b2, b3):
# 0x80 = p1_start
# 0x40 = test
# 0x20 = p1_up
# 0x10 = p1_down
# 0x08 = p1_left
# 0x04 = p1_right
# 0x02 = p1_b1
# 0x01 = p1_b2

    if (b0 & 0x80):
        print("p1_start")
    elif (b0 & 0x40):
        print("test")
    elif (b0 & 0x20):
        print("p1_up")
    elif (b0 & 0x10):
        print("p1_down")
    elif (b0 & 0x08):
        print("p1_left")
    elif (b0 & 0x04):
        print("p1_right")
    elif (b0 & 0x02):
        print("p1_b1")
    elif (b0 & 0x01):
        print("p1_b2")
    
# 0x80 = p1_b3
# 0x40 = p1_b4
# 0x01 = p1_coin

    if (b1 & 0x80):
        print("p1_b3")
    elif (b1 & 0x40):
        print("p1_b4")
    elif (b1 & 0x01):
        print("p1_coin")


# 0x80 = p2_start
# 0x40 = service
# 0x20 = p2_up
# 0x10 = p2_down
# 0x08 = p2_left
# 0x04 = p2_right
# 0x02 = p2_b1
# 0x01 = p2_b2

    if (b2 & 0x80):
        print("p2_start")
    elif (b2 & 0x40):
        print("test")
    elif (b2 & 0x20):
        print("p2_up")
    elif (b2 & 0x10):
        print("p2_down")
    elif (b2 & 0x08):
        print("p2_left")
    elif (b2 & 0x04):
        print("p2_right")
    elif (b2 & 0x02):
        print("p2_b1")
    elif (b2 & 0x01):
        print("p2_b2")


# 0x80 = p2_b3
# 0x40 = p2_b4
# 0x01 = p2_coin

    if (b3 & 0x80):
        print("p2_b3")
    elif (b3 & 0x40):
        print("p2_b4")
    elif (b3 & 0x01):
        print("p2_coin")

while True:
    ser_bytes = ser.read_until('\x42')
    x = bytearray.fromhex( binascii.hexlify(ser_bytes) )
#    x = bytearray.fromhex("76fd082300010042" )
    b0 = x[3]
    b1 = x[4]
    b2 = x[5]
    b3 = x[6]

    buttons(x[3], x[4], x[5], x[6])
    print("###########################################################")




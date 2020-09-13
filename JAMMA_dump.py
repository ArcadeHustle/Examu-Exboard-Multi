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

from __future__ import print_function

import serial
import binascii

ser = serial.Serial(
    port='/dev/tty.usbserial',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 0.2
)

while True:
    ser_bytes = ser.read_until('\x42')

    if len(ser_bytes) < 2:
        continue

#    print(binascii.hexlify(ser_bytes[0:7]))

    if ser_bytes[-2] == '\x00':
        # 76fd080000000042 - Idle stick input 
        if ser_bytes[0:7] == '\x76\xfd\x08\x00\x00\x00\x00':
              continue
    	      print(binascii.hexlify(ser_bytes))
        else:
    	      print(binascii.hexlify(ser_bytes))
    elif ser_bytes[-2] == '\x20':
    	print(binascii.hexlify(ser_bytes))
    elif ser_bytes[-2] == '\x70':
    	print(binascii.hexlify(ser_bytes))
    else:
    	print(binascii.hexlify(ser_bytes))
    
 



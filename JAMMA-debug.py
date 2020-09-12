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

while True:
    ser_bytes = ser.read_until('\x42')
    print(binascii.hexlify(ser_bytes).split('\x5a'))




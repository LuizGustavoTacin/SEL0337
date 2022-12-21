from smbus import SMBus
from time import sleep

addr = 0x8
bus = SMBus(1)

flag = True

print("Digite 1 para ON ou 0 para OFF")
while flag:
    ledstate = input(">>>")
    if ledstate == "1":
        bus.write_byte(addr, 0x1)
    elif ledstate == "0":
        bus.write_byte(addr, 0x0)
    else:
        flag = False
        bus.write_byte(addr, 0x0)
    a = bus.read_i2c_block_data(0x8, 0x0, 2)
    print(a)
    b = a[0]*256+a[1]
    print(b)
    sleep(0.5)

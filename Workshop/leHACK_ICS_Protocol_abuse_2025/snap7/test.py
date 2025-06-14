import snap7
import time 
plc = snap7.logo.Logo()

plc.connect("10.1.1.15", 0x0300, 0x0200)

plc.write("1024.0",1)
plc.write("1024.1",1)
plc.write("1024.2",1)
plc.write("1024.3",1)

plc.write("1064.0",1)
plc.write("1064.1",1)
plc.write("1064.2",1)
plc.write("1064.3",1)

print("value of address V1064.0: ", plc.read("1064.0"))
print("value of address V1064.0: ", plc.read("1064.1"))
print("value of address V1064.0: ", plc.read("1064.2"))
print("value of address V1064.0: ", plc.read("1064.3"))

plc.write("1064.0",0)
plc.write("1064.1",0)
plc.write("1064.2",0)
plc.write("1064.3",0)

print("value of address V1064.0: ", plc.read("1024.0"))
print("value of address V1064.0: ", plc.read("1024.1"))



plc.disconnect()
from pymodbus.client import ModbusSerialClient
import time
import logging

# ---- Logging for troubleshooting (optional, uncomment to enable) ----
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
# ---------------------------------------------------------------------

# Configuration - match these to your Arduino code/hardware!
PORT = 'COM9'      # Replace with your USB-RS485 COM port
BAUDRATE = 9600    # Must match Arduino
SLAVE_ID = 1       # Must match your Arduino SLAVE_ID

# Create the client
client = ModbusSerialClient(
    port=PORT,
    baudrate=BAUDRATE,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=2,       # Increase if needed
)

if client.connect():
    print("Connected to Modbus slave.")
    time.sleep(1)  # Wait for connection to settle
    
    # ----------- Read servo position (register 0) -----------
    response = client.read_holding_registers(address=0, count=1, slave=SLAVE_ID)
    if not response.isError():
        print(f"Servo position (register 0): {response.registers[0]}")
    else:
        print("Failed to read register:", response)

    
    # ----------- Read LED status (Coil 0) -----------
    #response = client.read_holding_registers(address=0, count=1, slave=SLAVE_ID)
    response = client.read_coils(address=0, count=2, slave=SLAVE_ID)
    
    if not response.isError():
        print(f"coil value (coil 0): {response}")
    else:
        print("Failed to read coil:", response)
    
    # ----------- Write servo position (to register 0) -----------
    # Example: Move SG90 servo to 45°
    value = 90
    response = client.write_register(address=0, value=value, slave=SLAVE_ID)
    
    response_coil = client.write_coil(address=0, value=0, slave=SLAVE_ID)
    #response_coil = client.write_coil(address=1, value=1, slave=SLAVE_ID)
    if not response.isError():
        print(f"Written value {value} to register 0.")
    else:
        print("Failed to write register:", response)
    
    # ----------- Read LED status (Coil 0) -----------
    #response = client.read_holding_registers(address=0, count=1, slave=SLAVE_ID)
    response = client.read_coils(address=0, count=2, slave=SLAVE_ID)
    
    if not response.isError():
        print(f"coil value (coil 0): {response}")
    else:
        print("Failed to read coil:", response)
    # Optionally re-read to confirm
    time.sleep(0.5)
    response = client.read_holding_registers(address=0, count=1, slave=SLAVE_ID)
    if not response.isError():
        print(f"New servo position: {response.registers[0]}")
    else:
        print("Failed to read register:", response)
    
    client.close()
else:
    print("Could not connect to Modbus slave. Check COM port and wiring!")

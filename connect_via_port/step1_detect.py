from serial.tools import list_ports

def list_detailed_ports():
    print("Detecting all serial devices...\n")
    for port in list_ports.comports():
        print(f"Device: {port.device}")
        print(f"  VID:PID = {port.vid}:{port.pid}")
        print(f"  Manufacturer: {port.manufacturer}")
        print(f"  Product: {port.product}")
        print(f"  Serial Number: {port.serial_number}")
        print("-" * 40)

if __name__ == "__main__":
    list_detailed_ports()

from serial.tools import list_ports

# Custom arm definitions based on your discovery
ARM_DEVICES = {
    "MainArm": {
        "vid": 0x1A8E,     # 6790 in hex
        "pid": 0x55F3,     # 21971 in hex
        "product": "SO100-MainArm",
    },
    "SubArm": {
        "vid": 0x1A8E,
        "pid": 0x55F3,
        "product": "SO100-SubArm",
    }
}

def detect_arm_ports():
    matched_ports = {}
    ports = list_ports.comports()

    for arm_name, criteria in ARM_DEVICES.items():
        found = False
        for port in ports:
            if (
                (criteria.get("vid") is None or port.vid == criteria["vid"]) and
                (criteria.get("pid") is None or port.pid == criteria["pid"]) and
                (criteria.get("product") is None or port.product == criteria["product"])
            ):
                matched_ports[arm_name] = port.device
                found = True
                break
        if not found:
            matched_ports[arm_name] = None  # Not found

    return matched_ports


if __name__ == "__main__":
    arm_ports = detect_arm_ports()
    for arm, port in arm_ports.items():
        if port:
            print(f"{arm} found on port: {port}")
        else:
            print(f"{arm} not detected!")

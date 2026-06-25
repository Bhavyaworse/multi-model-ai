class MachineMonitor:
    def __init__(self, serial_num, telemetry):
        self.serial_num = serial_num
        self.telemetry = telemetry

    def count_critical_drops(self, floor_limit):
        drop_count = 0
        for metric in self.telemetry:
            if metric < floor_limit:
                drop_count = drop_count + 1
        return drop_count

    def inspect_vibration_delta(self):
        for i in range(len(self.telemetry) - 1):
            variance = abs(self.telemetry[i] - self.telemetry[i+1])
            if variance > 35:
                return "Alert Triggered"
        return "Normal Operations"

operational_logs =
device = MachineMonitor("UNIT-X10", operational_logs)

print(device.count_critical_drops(70))
print(device.inspect_vibration_delta())

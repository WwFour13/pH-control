from gpiozero import DigitalInputDevice
from time import time, sleep

sensor = DigitalInputDevice(pin=23)  # Replace with your actual GPIO pin

pulse_count = 0

def pulse_count_to_mL(count):
    return max((count * 0.0332891 - 1.04255), 0)  # Calculated conversion from measuring total pulse count and time-to fill known water amount

# Pulse callback function
def pulse():
    global pulse_count
    pulse_count += 1

# Attach the callback
sensor.when_activated = pulse

def get_flow_rate_pulses_per_sec(measurement_seconds=5) -> float:
    global pulse_count
    pulse_count = 0
    start = time()
    sleep(measurement_seconds)
    elapsed = time() - start
    flow_rate = (pulse_count) / (elapsed)  # Hz
    return flow_rate

def get_flow_rate_mL_per_sec(measurement_seconds) -> float:
    return pulse_count_to_mL(get_flow_rate_pulses_per_sec(measurement_seconds))

def indefinite_pulse_count():
    start = time()
    while True:
        elapsed = time() - start
        print(f"{pulse_count=}, {elapsed=}")
        sleep(0.1)


if __name__ == "__main__":
    indefinite_pulse_count()


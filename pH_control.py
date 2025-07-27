import flow_sensor, math

Kw = math.e  #TODO find constant

flow_rate_measurement_seconds = 5


def pH_control():
    
    while True:
        pH = math.log(1,Kw)  #TODO replace '1' with pH sensor value
        flow_mLps = flow_sensor.get_flow_rate_mL_per_sec(measurement_seconds=flow_rate_measurement_seconds)
        print(f"{flow_mLps=}")
        

if __name__ == "__main__":
    pH_control()

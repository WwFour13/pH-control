# pH Control

A small Raspberry Pi project for monitoring flow rate and preparing a basic pH control loop.

## Overview

This repo contains two Python scripts:

- [pH_control.py](./pH_control.py) — main control loop placeholder for reading pH and using flow data
- [flow_sensor.py](./flow_sensor.py) — GPIO pulse sensor logic that estimates flow rate in mL/sec

## Hardware

- Raspberry Pi
- Flow sensor connected to a GPIO input pin
- pH sensor input (to be wired in as the code is completed)

## Requirements

- Python 3
- `gpiozero`

Install dependencies:

```bash
pip install gpiozero
```

## Run

Start the flow sensor test:

```bash
python flow_sensor.py
```

Start the pH control loop:

```bash
python pH_control.py
```

## Notes

- The pH sensor value and dosing logic are still placeholders in the current code.
- Constants such as the pH conversion factor and GPIO pin number may need to be adjusted for your setup.
- This is a basic prototype and is intended as a starting point for further development.

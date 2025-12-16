# PiPER Controller MK2

A Python-based robotic control system for dual PiPER robotic arms designed for automated LOHC (Liquid Organic Hydrogen Carrier) laboratory operations.

## Overview

This repository contains control software for a dual-arm robotic system that automates complex laboratory tasks including:
- Liquid handling and pouring operations
- Grinding and mixing procedures
- Bowl carrier transport on rail systems
- Shaking and agitation operations
- Precise manipulation of laboratory equipment

The system integrates:
- **Dual PiPER robotic arms** (left and right) with 6-DOF + gripper control
- **Arduino-based I/O control** for peripherals (electromagnets, sensors, valves)
- **CAN bus communication** for motor control
- **Synchronized multi-arm coordination** for complex workflows

## Features

- **Pre-programmed Action Sequences**: 8+ different automated laboratory actions
- **Dual Arm Coordination**: Synchronized control of left and right PiPER arms
- **Linear and Joint Motion Control**: Support for multiple motion types (joint, linear, natural, curve)
- **Arduino Integration**: Control of digital I/O for electromagnets, relays, and sensors
- **Safety Timeouts**: Built-in timeout mechanisms for safe operation
- **Rail System Control**: Automated movement of carriers along linear rails

## Hardware Requirements

- 2x PiPER robotic arms (6-DOF with gripper)
- Arduino UNO R4 WiFi board
- CAN bus interface hardware
- Electromagnets for rail carrier control
- Laboratory equipment setup (bottles, bowls, grinders, etc.)

## Software Dependencies

Install required Python packages:

```bash
pip install piper-sdk
pip install python-can
pip install telemetrix-uno-r4
pip install pyserial
```

## Project Structure

```
mk2/
├── LOHCActionAll.py          # Main action library with all LOHC operations
├── PiPERControllerMK2.py     # Core PiPER arm controller wrapper
├── PiPERMover.py             # Low-level motion control implementation
├── PyArduino.py              # Arduino I/O control interface
├── Main.py                   # Example usage and testing
├── Picus2Test.py             # Testing utilities
├── can_activate.sh           # CAN bus initialization script
├── find_all_can_port.sh      # CAN port discovery utility
└── piper_ctrl_reset.py       # Controller reset utility
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd PiPERController/mk2
```

2. Set up Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install piper-sdk python-can telemetrix-uno-r4 pyserial
```

4. Configure CAN bus interfaces:
```bash
bash can_activate.sh piper_right 1000000 "3-1.3:1.0"
bash can_activate.sh piper_left 1000000 "3-1.2:1.0"
```

## Usage

### Basic Example

```python
from LOHCActionAll import LOHCActionBook

# Initialize the action controller
lab = LOHCActionBook()

# Run a specific action (e.g., Action 1: Bottle pouring)
lab.run_lohc_action_1()

# Run Action 4: Grinding operation
lab.run_lohc_action_4()

# Run Action 8: Bowl carrier manipulation
lab.run_lohc_action_8_1()
lab.run_lohc_action_8_2()

# Rail transport operations
lab.run_rail_to_left()
lab.run_shaking()
```

### Available Actions

- `run_lohc_action_1()`: **Powder Pouring** - Grasps bottle, moves to bowl, and pours powder with pounding motion (repeated twice for thorough emptying)
- `run_lohc_action_3()`: **Pipette Operation** - Uses pipette on bowl *(Work in Progress)*
- `run_lohc_action_4()`: **Grinding Operation** - Grasps pestle (macja), performs grinding motion in bowl with multi-position circular grinding patterns
- `run_lohc_action_6()`: **Bowl Shaking** - Grasps bowl carrier from rail, performs repeated vertical shaking motion for mixing, returns to rail
- `run_lohc_action_8_1()`: **Bowl Carrier Pouring** - Releases rail electromagnet, grasps bowl carrier, lifts and pours into funnel (repeated twice)
- `run_lohc_action_8_2()`: **Funnel Carrier Shaking** - Grasps funnel carrier and performs rapid vertical shaking to facilitate material flow
- `run_rail_to_left()`: **Rail Transport Left** - Dual-arm coordination to move bowl carrier from right rail position to left rail position
- `run_rail_to_right()`: **Rail Transport Right** - Dual-arm coordination to move bowl carrier from left rail position to right rail position
- `run_test()`: **Curve Motion Test** - Tests curve trajectory motion between three waypoints

### Direct Arm Control

```python
from PiPERControllerMK2 import PiPERControllerMK2
from piper_sdk import C_PiperInterface

# Initialize individual arm
piper_right = PiPERControllerMK2(C_PiperInterface("piper_right"))

# Joint movement (7 values: 6 joints + gripper)
piper_right.run_move_joint([0, 0, 0, 0, 0, 0, 0], speed=20)

# Linear movement (7 values: X, Y, Z, RX, RY, RZ, gripper)
piper_right.run_move_linear_known([100, 200, 300, 0, 90, 0, 50], speed=20)

# Combined movement (14 values: joint positions + end effector pose)
piper_right.run_piper_movement([0, 0, 0, 0, 0, 0, 0, 56, 0, 213, 0, 85, 0, 0], speed=20)
```

### Arduino Control

```python
from PyArduino import PyArduino

pa = PyArduino()

# Digital output control (e.g., electromagnet)
pa.run_digital_write(pin_number=2, pin_state=True)

# Read digital input
value = pa.get_digital_state(pin_number=8)

# Read analog input
analog_value = pa.get_analog_state(pin_number=0)
```

## Configuration

### CAN Bus Setup

The system uses CAN bus for communication with PiPER arms. Configure the interfaces:

- **piper_right**: USB device at `3-1.3:1.0`, baudrate 1000000
- **piper_left**: USB device at `3-1.2:1.0`, baudrate 1000000

### Motion Speed Settings

Adjust speed settings in `LOHCActionAll.py`:
```python
self.speed_slow = 10      # Slow, precise movements
self.speed_default = 20   # Standard operations
self.speed_fast = 90      # Quick transitions
```

## Safety Considerations

- All movements include timeout protections (default 3 seconds)
- Electromagnets are controlled to prevent accidental drops
- Arms return to home position after operations
- Emergency stop functionality through signal handling

## Troubleshooting

**CAN bus connection issues:**
```bash
bash find_all_can_port.sh  # Discover available CAN ports
python3 piper_ctrl_reset.py  # Reset controllers
```

**Timeout errors:**
- Increase timeout parameter in movement functions
- Check for mechanical obstructions
- Verify CAN bus connectivity

**Arduino connection issues:**
- Ensure Arduino UNO R4 WiFi is properly connected
- Check telemetrix firmware is uploaded to Arduino
- Verify network connectivity for WiFi mode

## License

[Specify your license here]

## Contributing

[Add contribution guidelines if applicable]

## Contact

[Add contact information]

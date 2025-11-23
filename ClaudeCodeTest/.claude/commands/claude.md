# CLAUDE.md — PiPER Controller MK2 Development Guidelines

> ROLE
> You are an AI pair programmer working on the PiPER robotic arm controller.
> Always prioritize safety, correctness, and maintainability in robotics control code.

---

## 1. Project Overview

- This is a **Python-based robotic arm controller** for the PiPER robot system
- The main goals are:
  - Safe and reliable robot motion control
  - CSV-based motion recording and playback
  - CAN bus communication with robotic hardware
  - Precise joint and end-effector position control

**Key Components:**
- `PiPERControllerMK2.py` – Main controller with motion execution and CSV recording
- `PiPERMover.py` – Low-level motion primitives (MoveJ, MoveP, MoveL, MoveC)
- `LOHCAction*.py` – High-level action scripts
- `action_record/` – CSV motion recordings

---

## 2. Tech Stack & Conventions

- Language: **Python 3.8+**
- SDK: **piper_sdk** (proprietary robotic arm SDK)
- Hardware: **CAN bus** interface for robot communication
- Data format: **CSV** for motion recording/playback
- Virtual environment: `venv/`

**Important conventions**

- Always activate CAN bus before robot operations (`can_activate.sh`)
- Use type hints for function signatures (e.g., `def run_move_joint(self, joint_list: list)`)
- Follow naming convention: snake_case for functions and variables
- Robot positions are in millimeters (scaled by factor 1000)

---

## 3. Coding Standards (Robotics Safety & Clean Code)

When generating or editing code, you MUST follow these rules:

### 3.1 General

- Prefer **small, focused functions** that do one thing well.
- Aim for **descriptive names**:
  - Functions: verbs in snake_case (`run_move_joint`, `get_eef_status`)
  - Variables: clear nouns (`joint_list`, `eef_list`, `gripper_value`)
  - Classes: PascalCase (`PiPERControllerMK2`, `PiPERMover`)
- Avoid magic values:
  - Extract constants (e.g., `self.factor = 1000`, `self.time_action = 0.05`)
- Do not introduce unnecessary abstractions:
  - Keep robot control logic clear and explicit

### 3.2 Structure & Modules

- Keep files focused:
  - **Controller**: High-level orchestration (`PiPERControllerMK2.py`)
  - **Mover**: Low-level motion primitives (`PiPERMover.py`)
  - **Actions**: Task-specific scripts (`LOHCAction*.py`)
  - **Records**: CSV motion data (`action_record/`)
- Separate concerns:
  - Motion commands vs. status checking
  - Joint space vs. Cartesian space control
  - Recording vs. playback logic

### 3.3 Error Handling & Safety

- **CRITICAL**: Never swallow errors in robot control code
- Use timeouts for all robot operations (default: 5 seconds)
- Implement signal handlers for timeout protection:
  ```python
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(5)
  ```
- Always enable motors before movement:
  ```python
  self.piper_arm.enable.run()
  ```
- Add position verification before executing motions
- Handle CAN bus disconnection gracefully
- Log robot state changes with timestamps

### 3.4 Comments & Documentation

- Prefer self-explanatory code over comments
- **ALWAYS document**:
  - Safety-critical sections
  - Position coordinate systems (joint vs. EEF)
  - CSV format specifications
  - Timing-sensitive operations
- Use docstrings for all functions:
  ```python
  def get_record_csv(self, filepath: str, joint_list: list, eef_list: list):
      '''
      This function captures stream of values and saves to CSV newline.

      Input: str, list, list
      Output: None
      '''
  ```

---

## 4. Motion Control Standards

### 4.1 Motion Types

The system supports 4 types of motion:

1. **MoveJ (Joint Motion)**: Direct joint angle control
   - Use for: Fast movements, avoiding obstacles
   - Input: 7 values (6 joints + gripper)
   - Example: `[0, 0, 0, 0, 0, 0, 0]`

2. **MoveP (Natural Path)**: Point-to-point in Cartesian space
   - Use for: Predictable end-effector paths
   - Input: 7 values (X, Y, Z, RX, RY, RZ, gripper)

3. **MoveL (Linear Motion)**: Straight-line Cartesian motion
   - Use for: Precision tasks, pick-and-place
   - Input: 7 values (X, Y, Z, RX, RY, RZ, gripper)

4. **MoveC (Curved Motion)**: Arc/circular motion
   - Use for: Smooth trajectories
   - Input: 3 waypoints with flags (start, via, end)

### 4.2 CSV Recording Format

- **Columns**: 14 values per row
  - First 7: Joint positions (joint1-6 + gripper)
  - Last 7: End-effector position (X, Y, Z, RX, RY, RZ, gripper)
- **Units**: All positions in millimeters (integer values)
- **Timing**: Controlled by `self.time_action` (default: 0.05s)

### 4.3 Coordinate Systems

- **Joint Space**: 6 revolute joints + 1 gripper
  - Range: Depends on robot model
  - Units: Degrees (converted to millidegrees internally)

- **Cartesian Space (EEF)**: End-effector pose
  - Position: X, Y, Z (mm)
  - Orientation: RX, RY, RZ (Euler angles in degrees)
  - Gripper: 0-1000 (0=closed, 1000=open)

---

## 5. Development Workflow

### 5.1 CAN Bus Setup

Before running any robot code:

```bash
# Activate CAN interface
bash can_activate.sh piper_left 1000000 "3-1:1.0"

# Verify CAN ports
bash find_all_can_port.sh

# Reset controller if needed
python3 piper_ctrl_reset.py
```

### 5.2 Common Operations

**Record motion to CSV:**
```python
piper_left.get_record_csv(filepath, joint_list, eef_list)
```

**Playback from CSV:**
```python
piper_left.run_record_csv(filepath)
```

**Check robot status:**
```python
joint_status = piper_left.get_joint_status()
eef_status = piper_left.get_eef_status()
```

### 5.3 Virtual Environment

Always use the project virtual environment:
```bash
source mk2/venv/bin/activate
```

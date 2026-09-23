# Robot Arm: Path Planing, Motion Control, and Robot Vision

A repository documenting the development and integration of a robotic arm system utilizing the Ufactory 850 cobot arm, featuring ROS2 Jazzy, MoveIt2, and a custom robot vision pipeline.

---

![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python&logoColor=white)
![C/C++](https://img.shields.io/badge/C%2FC%2B%2B-00599C?logo=c&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-v4.6.0-5C3EE8?logo=opencv&logoColor=white)
![YOLO11](https://img.shields.io/badge/YOLO-v11-00FFFF)
![GStreamer](https://img.shields.io/badge/GStreamer-RTP%2FUDP-red)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.13-ee4c2c?logo=pytorch&logoColor=white)
![ONNX Runtime](https://img.shields.io/badge/ONNX_Runtime-v1.30.0-005CED?logo=onnx&logoColor=white)
![ROS2](https://img.shields.io/badge/ROS2-22314E?logo=ros&logoColor=white)
![Gazebo](https://img.shields.io/badge/Gazebo-FF8C00)
![License](https://img.shields.io/badge/License-MIT-green)

## Table of Contents

- [Features](#-project-features)
- [TechStacks](#-environment--dependencies)
- [Get Started](#-getting-started)
- [Status](#-status)
- [Contributing](#-donate)
- [License](#️-license)

---

## 📚 Project Feature

This repository is focused on two main technological pillars:

*   **Robotics Middleware (ROS2):** Node architecture, robotic simulation, and motion planning utilizing core ROS2 tools including RViz, and MoveIt2. This is tailored specifically for controlling the Ufactory 850 cobot on ROS2 Jazzy.
*   **Computer Vision (Python):** Real-time object detection and video streaming pipelines utilizing YOLOv11 and OpenCV.

---

## 📦 Environment & Dependencies

The Python components of this repository are built and tested on **Python 3.12.3** running in an Ubuntu Linux environment. Below is the active dependency stack required for the computer vision and reinforcement learning modules.

#### 🐍 Core Scientific Packages
| Package | Version | Description |
| :--- | :--- | :--- |
| **Python** | v3.12 | Core programming language environment |
| **NumPy** | v1.26.4 | Numerical computation and array operations |
| **Matplotlib** | v3.6.3 | Data visualization and plotting |

#### 👁️ Computer Vision (CV)
| Package | Version | Description |
| :--- | :--- | :--- |
| **OpenCV** | v4.6.0 | Image processing and GStreamer backend |
| **Ultralytics** | v8.4.149 | YOLOv11 model inference and training |

#### 🤖 Robotic Operating System (ROS2)
| Package | Version | Description |
| :--- | :--- | :--- |
| **ROS2** | Jazzy | Core robotics middleware and node communication framework |
| **Gazebo** | v8.15.0 | 3D robot physics and environment simulator |
| **RViz** | v14.1.23 | 3D visualization tool for sensor data and robot state |
| **MoveIt2** | v2.12.4 | Motion planning and robotic manipulation framework |
---

##  🚀 Getting Started

To explore the Python-based CV and RL projects, it is recommended to clone the repository and set up a virtual environment.
```bash
# Clone the repository
git clone [https://github.com/hilmanlajuardhie/Robot_Arm.git](https://github.com/hilmanlajuardhie/Robot_Arm.git)
cd Robot_Arm
```
```bash
# Set up Python virtual environment for Vision tasks
python3.12 -m venv .venv
source .venv/bin/activate
```
```bash
# Build ROS2 Workspace
colcon build
```

*Note: For the ROS2 workspaces, please refer to the specific `README.md` files located within their respective subdirectories for build instructions (e.g., Makefiles, Colcon build commands).*

---

## 🚧 Status

- Vision: Streaming Real-time Edge-AI.
- ROS2: Developing Nodes for Ufactory 850 integrtation.

## 🤝 Donate

If you find this project useful for your work or research, consider supporting its ongoing development!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/hilmanlajuardhie)

*Every coffee or donation helps keep experimental hardware and vision projects going. Thank you!*

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤ by [JIAR](https://github.com/hilmanlajuardhie)
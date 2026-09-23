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

- [Domains](#-learning-domains)
- [TechStacks](#️-environment--dependencies)
- [Get Started](#-getting-started)
- [Status](#-status)
- [Contributing](#-donate)
- [License](#️-license)

---

## 📚 Project Feature

This repository is divided into four main technological pillars:

*   **Embedded Systems (C/C++):** Bare-metal programming, hardware abstraction, and register-level configuration for STM32 microcontrollers, alongside foundational C/C++ software development.
*   **Computer Vision (Python):** Real-time object detection and video streaming pipelines utilizing YOLOv11, OpenCV, and GStreamer.
*   **Reinforcement Learning (Python):** Training, evaluating, and simulating intelligent agents using Stable-Baselines3 (SB3), Gymnasium, and MuJoCo, backed by PyTorch and ONNX Runtime.
*   **Robotics Middleware (ROS2):** Node architecture, robotic simulation, and motion planning utilizing core ROS2 tools including Gazebo, RViz, and MoveIt2.

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

#### 🧠 Reinforcement Learning (RL) & Physics
| Package | Version | Description |
| :--- | :--- | :--- |
| **PyTorch** | v2.13.0+cu126 | Deep learning tensor library (CUDA enabled) |
| **MuJoCo Physics** | v3.13.0 | Advanced physics simulation engine |
| **Gymnasium** | v1.3.0 | RL environment API |
| **Stable-Baselines3**| v2.9.0 | RL algorithm implementations |
| **ONNX Runtime** | v1.30.0 | Cross-platform machine learning inference |
| **Pygame** | v2.5.8 | 2D rendering and window management |

#### 🤖 Robotic Operating System (ROS2)
| Package | Version | Description |
| :--- | :--- | :--- |
| **ROS2** | - | Core robotics middleware and node communication framework |
| **Gazebo** | - | 3D robot physics and environment simulator |
| **RViz** | - | 3D visualization tool for sensor data and robot state |
| **MoveIt2** | - | Motion planning and robotic manipulation framework |
---

##  🚀 Getting Started

To explore the Python-based CV and RL projects, it is recommended to clone the repository and set up a virtual environment.
```bash
git clone [https://github.com/hilmanlajuardhie/Learn.git](https://github.com/hilmanlajuardhie/Learn.git)
cd Learn
```
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

*Note: For the C/C++ STM32 projects and ROS2 workspaces, please refer to the specific `README.md` files located within their respective subdirectories for build instructions (e.g., Makefiles, Colcon build commands).*

---

## 🚧 Status

- C/C++: Simulate a Cartesian Robots.
- Vision: Streaming Real-time Edge-AI.
- RL: Developing Mujoco Sim.
- ROS2: Developing Nodes.

## 🤝 Donate

If you find this project useful for your work or research, consider supporting its ongoing development!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/hilmanlajuardhie)

*Every coffee or donation helps keep experimental hardware and vision projects going. Thank you!*

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤ by [JIAR](https://github.com/hilmanlajuardhie)
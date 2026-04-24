#  Indoor Localization using GraphSLAM (ROS2)
🚀 Real-time indoor mapping and localization using GraphSLAM with ROS2 and RTABMap

##  Overview

This project implements **indoor localization using GraphSLAM** on a simulated robot.
Since GPS is not available indoors, the robot builds a map and estimates its position simultaneously using onboard sensors.

We implemented this using:

* ROS2 Humble
* TurtleBot3 (simulation)
* RTABMap (GraphSLAM engine)
* g2o (graph optimization backend)

---

## Problem Statement

Indoor localization is a core robotics challenge where a robot must determine its position without GPS.

Without accurate localization:

* Navigation fails
* Obstacle avoidance becomes unreliable
* Autonomous operation is not possible

---

##  Objective

* Implement a **GraphSLAM pipeline**
* Perform **real-time mapping and localization**
* Demonstrate **loop closure detection**
* Generate a **2D occupancy map**

---

##  How It Works (GraphSLAM Pipeline)

1. Robot collects **LiDAR + Odometry data**
2. Each robot pose → stored as a **node**
3. Movement between poses → **edges (constraints)**
4. Loop closure detection using **ICP**
5. Graph optimization using **g2o**
6. Final **corrected map generated**

---

##  Technologies Used

###  Software

* ROS2 Humble
* Python 3
* RTABMap
* g2o
* RViz2
* Gazebo Classic

###  Libraries

* turtlebot3
* rtabmap_ros
* rtabmap_slam
* nav2_map_server

---

##  Simulation Environment

* Gazebo Classic 11
* TurtleBot3 House World
* Multiple rooms & corridors
* Manual control using keyboard

---

##  Results

###  Key Outcomes

* Generated a **2D occupancy map**
* Successfully detected **loop closures**
* Corrected trajectory using **graph optimization**
* Final map aligned with actual environment

---

## Output Screenshots

###  House World (Gazebo)

![House World](assets/house_world.jpeg)

###  Pose Graph (RTABMap)

![Pose Graph](assets/pose_graph.jpeg)

### Occupancy Map (RViz2)

![Occupancy Map](assets/map.jpeg)

---

##  Demo Video

[Watch Demo](https://drive.google.com/file/d/1bYaGJer1HK6FPry-RvEfqvyyKzPy_kww/view)

---

## Installation & Setup

```bash
git clone https://github.com/Kash1sh600/indoor-graphslam-ros2
cd indoor-graphslam-ros2

colcon build
source install/setup.bash

ros2 launch <package_name> <launch_file>
```

---



# Indoor Localization using GraphSLAM
### ROS2 Humble | TurtleBot3 Waffle | RTABMap | Gazebo

---

## What This Does

- Launches a TurtleBot3 waffle robot in the indoor house world
- RTABMap runs GraphSLAM in real time:
  - Each robot pose → a **node** in the pose graph
  - Odometry between poses → an **edge**
  - When the robot revisits a place → **loop closure** → g2o optimizes the whole graph
- RViz2 shows the pose graph (nodes, edges, loop closures) live
- Optional: house world with 3 dynamic actors (moving people/box)

---

## Prerequisites

```bash
# TurtleBot3
sudo apt install ros-humble-turtlebot3 ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-simulations -y

# RTABMap
sudo apt install ros-humble-rtabmap-ros -y

# Teleop
sudo apt install ros-humble-teleop-twist-keyboard -y

# Add to ~/.bashrc
echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc
source ~/.bashrc
```

---

## Build

```bash
cd ~/my_graphslam_ws
colcon build --symlink-install
source install/setup.bash
```

---

## Run: Option A — Standard House World (Recommended to start)

Open **4 terminals**, source the workspace in each:
```bash
source ~/my_graphslam_ws/install/setup.bash
```

**Terminal 1 — Gazebo World:**
```bash
ros2 launch my_graphslam world.launch.py
```

**Terminal 2 — RTABMap GraphSLAM:**
```bash
ros2 launch my_graphslam slam.launch.py
```

**Terminal 3 — RViz2:**
```bash
ros2 launch my_graphslam rviz.launch.py
```

**Terminal 4 — Drive the robot:**
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## Run: Option B — House World with Dynamic Actors

Replace Terminal 1 with:
```bash
ros2 launch my_graphslam world_with_actors.launch.py
```
Everything else is the same.

---

## What to Do in RViz2

When RViz2 opens you will see these displays (pre-configured):

| Display | Topic | What it shows |
|---|---|---|
| **Map** | `/map` | Occupancy grid growing as you drive |
| **LaserScan** | `/scan` | Live LiDAR rays (red dots) |
| **PoseGraph** | `/rtabmap/mapGraph` | ⭐ Nodes (spheres) + Edges (lines) |
| **MapPath** | `/rtabmap/mapPath` | Robot trajectory after graph optimization |
| **Odometry** | `/odom` | Raw wheel odometry (drifts - compare with MapPath) |
| **CloudMap** | `/rtabmap/cloud_map` | 3D point cloud of environment |

### How to trigger Loop Closure:
1. Drive the robot around several rooms
2. **Come back near your starting point** — this is critical
3. Watch the `/rtabmap/mapGraph` display — you'll see the graph **snap/correct**
4. The map will visibly improve alignment after loop closure

---

## Observing GraphSLAM in the Terminal

RTABMap prints loop closure events. Look for lines like:
```
[INFO] [rtabmap]: Loop closure detected! (node X -> node Y)  similarity=0.82
[INFO] [rtabmap]: Optimizing graph... 47 nodes, 51 edges
[INFO] [rtabmap]: Graph optimized in 12ms
```

---

## RTABMap Database

RTABMap saves a `.db` file at `~/.ros/rtabmap.db`.
You can replay and inspect it:
```bash
rtabmap-databaseViewer ~/.ros/rtabmap.db
```
This shows the full pose graph, all loop closures, and the final map.

---

## Project Notes

- **Why waffle and not burger?** The burger only has LiDAR. The waffle adds an RGB-D camera which RTABMap uses for visual loop closure detection.
- **Why g2o?** It's a standard GraphSLAM optimizer. `Optimizer/Strategy: 1` selects it.
- **Dynamic objects** appear as artifacts in the map because SLAM assumes a static world. This is a known open problem — discuss it in your report.
- **Loop closure is the key insight of GraphSLAM** — without revisiting a place, you're just doing odometry integration. The graph optimization step is what corrects accumulated drift.

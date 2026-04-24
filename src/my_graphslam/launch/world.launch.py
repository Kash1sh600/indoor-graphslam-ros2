import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Force waffle model - it has LiDAR + RGB-D camera, required for RTABMap
    set_tb3_model = SetEnvironmentVariable('TURTLEBOT3_MODEL', 'waffle')

    tb3_gazebo_share = FindPackageShare('turtlebot3_gazebo').find('turtlebot3_gazebo')

    # Launch the TurtleBot3 house world
    # This world has walls, rooms, corridors - ideal for GraphSLAM loop closure
    house_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo_share, 'launch', 'turtlebot3_house.launch.py')
        )
    )

    return LaunchDescription([
        set_tb3_model,
        house_world,
    ])

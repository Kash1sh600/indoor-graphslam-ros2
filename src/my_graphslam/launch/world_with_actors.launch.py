import os
from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    DeclareLaunchArgument,
    ExecuteProcess,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # ---- Environment ----
    set_tb3_model = SetEnvironmentVariable('TURTLEBOT3_MODEL', 'waffle')

    # ---- World file with dynamic actors ----
    world_file = os.path.join(
        get_package_share_directory('my_graphslam'),
        'worlds',
        'house_with_actors.world'
    )

    # ---- Gazebo with our custom world ----
    # We launch Gazebo directly with our world file instead of
    # using the turtlebot3_house launch (which hardcodes its own world)
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so', world_file],
        output='screen'
    )

    # ---- Spawn TurtleBot3 waffle into Gazebo ----
    tb3_gazebo_share = get_package_share_directory('turtlebot3_gazebo')

    spawn_tb3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo_share, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': '-2.0',
            'y_pose': '-0.5',
        }.items()
    )

    return LaunchDescription([
        set_tb3_model,
        gazebo,
        spawn_tb3,
    ])

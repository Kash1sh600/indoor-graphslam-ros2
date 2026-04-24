from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # -----------------------------------------------------------------------
    # Scan-only mode: RTABMap using only LiDAR (no depth camera needed)
    # This is clean 2D GraphSLAM - exactly what indoor localization needs
    # subscribe_depth=False, subscribe_rgb=False, subscribe_scan=True
    # -----------------------------------------------------------------------
    rtabmap_node = Node(
        package='rtabmap_slam',
        executable='rtabmap',
        name='rtabmap',
        output='screen',
        parameters=[{
            'use_sim_time': True,

            # SCAN ONLY - no depth camera
            'subscribe_depth': False,
            'subscribe_rgb': False,
            'subscribe_scan': True,
            'subscribe_odom_info': False,

            # Frame IDs
            'frame_id': 'base_footprint',
            'odom_frame_id': 'odom',
            'map_frame_id': 'map',

            # Sync - only scan now, much simpler
            'approx_sync': False,
            'topic_queue_size': 10,
            'sync_queue_size': 10,
            'qos_scan': 1,
            'qos_odom': 1,

            # GraphSLAM backend - g2o
            'Optimizer/Strategy': '1',
            'Optimizer/Iterations': '100',
            'Optimizer/Epsilon': '0.0001',
            'Optimizer/Robust': 'true',

            # Loop closure
            'Rtabmap/DetectionRate': '1.0',
            'Rtabmap/TimeThr': '0',
            'RGBD/OptimizeMaxError': '3.0',
            'RGBD/OptimizeFromGraphEnd': 'false',
            'RGBD/ProximityBySpace': 'true',
            'RGBD/ProximityPathMaxNeighbors': '10',

            # Memory
            'Mem/STMSize': '30',
            'Mem/NotLinkedNodesKept': 'false',

            # For scan-only, use ICP loop closure (not visual)
            'Reg/Strategy': '1',          # 1 = ICP (scan matching)
            'Icp/VoxelSize': '0.05',
            'Icp/MaxCorrespondenceDistance': '0.1',
            'Icp/PointToPlane': 'false',

            # Occupancy grid from laser scan
            'Grid/Sensor': '0',           # 0 = laser scan
            'Grid/RangeMax': '4.0',
            'Grid/RayTracing': 'true',
            'Grid/FromDepth': 'false',
        }],
        remappings=[
            ('scan', '/scan'),
            ('odom', '/odom'),
        ]
    )

    rtabmap_viz_node = Node(
        package='rtabmap_viz',
        executable='rtabmap_viz',
        name='rtabmap_viz',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'subscribe_depth': False,
            'subscribe_rgb': False,
            'subscribe_scan': True,
            'subscribe_odom_info': False,
            'frame_id': 'base_footprint',
            'approx_sync': False,
            'topic_queue_size': 10,
            'sync_queue_size': 10,
            'qos_scan': 1,
            'qos_odom': 1,
        }],
        remappings=[
            ('scan', '/scan'),
            ('odom', '/odom'),
        ]
    )

    return LaunchDescription([
        rtabmap_node,
        rtabmap_viz_node,
    ])

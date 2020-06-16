import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():
    # config SN:
    t265_serial_no = LaunchConfiguration('t265_serial_no', default='905312112031')
    d435_serial_no = LaunchConfiguration('d435_serial_no', default='825312071491')
    
    return LaunchDescription([

        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0.03', '0', '0', '0', 't265_link', 'd435_link']
            ),
        Node(
            package='realsense_node',
            node_executable='realsense_node',
            node_namespace="/d435",
            output='screen',
            parameters=[{'serial_no':d435_serial_no,
                         'base_frame_id': 'd435_link'}]
            ),
        Node(
            package='realsense_node',
            node_executable='realsense_node',
            node_namespace="/t265",
            output='screen',
            remappings=[('/t265/camera/odom/sample','/odom')],
            parameters=[{'serial_no':t265_serial_no,
                         'base_frame_id': 't265_link'}]
            )
    ])

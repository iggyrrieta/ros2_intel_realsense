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
    d435_serial_no = LaunchConfiguration('d435_serial_no', default='825312071491')
    # config D435
    #d435_conf = os.path.join(get_package_share_directory('realsense_examples'), 'config', 'd435.yaml')

    return LaunchDescription([
        Node(
            package='realsense_node',
            node_executable='realsense_node',
            node_namespace="/d435",
            output='screen',
            parameters=[{'serial_no': d435_serial_no, 
                         'base_frame_id': 'd435_link'}]
            )
    ])


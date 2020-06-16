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
    # config T265
    t265_conf = os.path.join(get_package_share_directory('realsense_examples'), 'config', 't265.yaml')

    return LaunchDescription([

        Node(
            package='realsense_node',
            node_executable='realsense_node',
            node_namespace="/t265",
            output='screen',
            parameters=[t265_conf,{'serial_no': t265_serial_no, 
                                   'base_frame_id': 't265_link'}]
            )
    ])
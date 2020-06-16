# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import launch
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    t265_base_frame_id = LaunchConfiguration('base_frame_id', default='t265_link')
    t265_serial_no = LaunchConfiguration('serial_no', default='905312112031')
    t265_node = Node(
        package='realsense_node',
        node_executable='realsense_node',
        node_namespace="/t265",
        output='screen',
        remappings=[('/t265/camera/odom/sample','/odom')],
        parameters=[{'serial_no':t265_serial_no ,
                     'base_frame_id': t265_base_frame_id,
                     'initial_reset':'true'}]
        )
    return launch.LaunchDescription([t265_node])
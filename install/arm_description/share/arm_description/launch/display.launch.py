import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():
  pkg_share = get_package_share_directory('arm_description')
  xacro_file = os.path.join(pkg_share, 'urdf', 'uf850.urdf.xacro')

  # Process Xacro file into raw URDF XML string
  robot_description_raw = xacro.process_file(xacro_file).toxml()

  return LaunchDescription([
      # Publish tf and robot geometry to ROS 2
      Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          output='screen',
          parameters=[{'robot_description': robot_description_raw}],
      ),
      # GUI sliders to manually move robot joints
      Node(
          package='joint_state_publisher_gui',
          executable='joint_state_publisher_gui',
          output='screen',
      ),
      # Launch RViz2
      Node(
          package='rviz2', 
          executable='rviz2', 
          name='rviz2', 
          output='screen'
      ),
  ])
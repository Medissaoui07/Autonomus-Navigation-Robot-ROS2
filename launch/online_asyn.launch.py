import os 
from launch_ros.actions import Node 
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration 
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument 


def generate_launch_description():
    use_sim_time=LaunchConfiguration('use_sim_time')
    slam_param_file=LaunchConfiguration('slam_param_file')


    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        'slam_param_file',
        default_value=os.path.join(get_package_share_directory("my_robot"),
                                   'configuration', 'mapper_params_online_async.yaml'),
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')
    

    start_slam_toolbox_node=Node(
        parameters=[
            slam_param_file,
            {use_sim_time:'use_sim_time'}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen'
    )
    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_slam_params_file_cmd)
    ld.add_action(start_slam_toolbox_node)

    return ld

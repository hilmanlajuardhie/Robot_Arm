import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alpha/DEV/Robot_Arm/install/uf_ros_lib'

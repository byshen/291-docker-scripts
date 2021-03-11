from docker_inject_network import *

IP_NAMENODE = get_ip("namenode")
IP_DATANODE = get_ip("datanode")
os.system(UNBLOCK_IP_CMD.format(IP_DATANODE))
print(UNBLOCK_IP_CMD.format(IP_DATANODE))
print("unblock ip issued...")
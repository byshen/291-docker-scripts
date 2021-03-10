import os 
import json
import shlex
import subprocess
import docker
import pprint

#########################
# IPs in the docker
IP_DATANODE = ""
IP_NAMENODE = ""
IP_RESOURCEMANAGER = ""
IP_NODEMANAGER = ""
#########################
WORK1_CMD = "docker exec -it namenode bash -c \"hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -write -nrFiles 10 -size 512MB\" > job1.log"
WORK2_CMD = "docker exec -it namenode bash -c \"hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -read -nrFiles 10 -size 512MB\" > job2.log"


BLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -A INPUT -s {} -j DROP\""
UNBLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -D INPUT -s {} -j DROP\""

#########################

def get_ip(container_name):
    client = docker.from_env()
    # print(client.info())
    container = client.containers.get(container_name)
    ip_add = container.attrs['NetworkSettings']['Networks']['dockerhadoop_default']['IPAddress']
    # pprint.pprint(container.attrs)
    return ip_add


def init_network_settings():
    IP_NAMENODE = get_ip("namenode")
    IP_DATANODE = get_ip("datanode")

    print(
    """
    IP namenode: {}
    IP datanode: {}
    """.format(IP_NAMENODE, IP_DATANODE))

def init_workloads():
    work_proc = subprocess.Popen(shlex.split(WORK1_CMD), shell=False)
    print("workload1 is running...")
    # os.system(BLOCK_IP_CMD.format(IP_DATANODE))
    # print("block ip issued...")
    # os.system(UNBLOCK_IP_CMD.format(IP_DATANODE))
    # print("unblock ip issued...")
    return

def inject_delay(time):
    return

def test():
    init_network_settings()
    init_workloads()

if __name__ == '__main__':
    test()


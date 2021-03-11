import os 
import json
import shlex
import subprocess
import docker
import pprint
import sys
import pty
from time import sleep

#########################
# IPs in the docker
IP_DATANODE = ""
IP_NAMENODE = ""
IP_RESOURCEMANAGER = ""
IP_NODEMANAGER = ""
#########################
WORK1_CMD = "docker exec -it namenode bash -c \"hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -write -nrFiles 10 -size 512MB\""
WORK2_CMD = "docker exec -it namenode bash -c \"hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -read -nrFiles 10 -size 512MB\""


BLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -A INPUT -s {} -j DROP\""
# BLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -A OUTPUT -s {} -j DROP\""
UNBLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -D INPUT -s {} -j DROP\""
# UNBLOCK_IP_CMD = "docker exec -it namenode bash -c \"iptables -D OUTPUT -s {} -j DROP\""

PROJ_DIR = "/home/byshen/courses/291-depend/project/scripts/"
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
    # sys.stdout = open('job1.log', 'a') 
    _, tty = pty.openpty()

    work_proc = subprocess.Popen(PROJ_DIR+"run-job1.sh")
    print("workload1 is running...")
    return

def remove_iptable_rules():
    IP_NAMENODE = get_ip("namenode")
    IP_DATANODE = get_ip("datanode")
    os.system(UNBLOCK_IP_CMD.format(IP_DATANODE))
    print(UNBLOCK_IP_CMD.format(IP_DATANODE))
    print("unblock ip issued...")

def inject_delay(time):
    IP_NAMENODE = get_ip("namenode")
    IP_DATANODE = get_ip("datanode")

    os.system(BLOCK_IP_CMD.format(IP_DATANODE))
    print(BLOCK_IP_CMD.format(IP_DATANODE))
    print("block ip issued...")

    print("sleep for ", time, " seconds")
    sleep(time) 
    os.system(UNBLOCK_IP_CMD.format(IP_DATANODE))
    print(UNBLOCK_IP_CMD.format(IP_DATANODE))
    print("unblock ip issued...")
    return

def test1():
    remove_iptable_rules()
    for i in range(100):
        inject_delay(0.05) 
        sleep(1)
    remove_iptable_rules()

def test2():
    remove_iptable_rules()
    for i in range(50):
        inject_delay(0.5) 
        sleep(1)
    remove_iptable_rules()

def test3():
    remove_iptable_rules()
    for i in range(10):
        inject_delay(5)
        sleep(5) 
    remove_iptable_rules()

def test4():
    remove_iptable_rules()
    for i in range(10):
        inject_delay(50)
        sleep(20) 
    remove_iptable_rules()

def test5():
    remove_iptable_rules()
    for i in range(10):
        inject_delay(100)
        sleep(10) 
    remove_iptable_rules()

def test6():
    remove_iptable_rules()
    for i in range(10):
        inject_delay(500)
        sleep(10) 
    remove_iptable_rules()

if __name__ == '__main__':
    print("You should have initiated workloads manually!")
    test6()
    # remove_iptable_rules()

# kill all running containers with docker kill $(docker ps -q)
# delete all stopped containers with docker rm $(docker ps -a -q)
# start last exited container docker start -a -i `docker ps -q -l`

docker run -it --name testhd tshan3/ubuntu4hadoop:ubuntu-hbase /bin/bash

# only start it
docker run -it --name test11 --network hdnetwork --ip 172.16.1.120 \
    --hostname test11  tshan3/ubuntu4hadoop:justEnv /bin/bash


# /etc/environment

# start hadoop
su hadoop
cd /opt/hadoop-3.3.0/sbin
find . -type f -name "*.log"
docker inspect --format='{{.LogPath}}' namenode

# run workload on namenode
cd /opt/hadoop-3.2.1/share/hadoop/mapreduce

docker exec -it namenode bash -c "hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -write -nrFiles 10 -size 512MB"
docker exec -it namenode bash -c "hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -read -nrFiles 10 -size 512MB"
docker exec -it namenode bash -c "hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -clean"



docker exec -it namenode bash -c "hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar nnbench -operation create_write -maps 10 -reduces 5 -numberOfFiles 1000 -readFileAfterOpen true"
iptables -A INPUT -s 172.22.0.3 -j DROP
sleep 1
iptables -D INPUT -s 172.22.0.3 -j DROP


docker exec -it hadoop11 /bin/bash


docker run -it --network host bash

su hadoop

sudo service ssh start

source etc/enviroment

source ~/.bashrc

ls /usr/local # Both hadoop and Hbase are here



# 


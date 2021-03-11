#!/bin/sh

docker exec -it namenode bash -c "hadoop jar /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar  TestDFSIO -read -nrFiles 10 -size 512MB" > job1.log

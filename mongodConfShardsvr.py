import sys
import csv 
import os

if len(sys.argv)>4:

 file = open(sys.argv[4]+'.conf','w') 
 file.write("systemLog:"+os.linesep)
 file.write("  destination: file"+os.linesep)
 file.write("  logAppend: true"+os.linesep)
 file.write("  path: "+ sys.argv[3]+'/mongod.log'+os.linesep)
 file.write("storage:"+os.linesep)
 file.write("  dbPath: "+ sys.argv[3]+os.linesep)
 if sys.argv[5] == 'M':
 	file.write("  engine: mmapv1"+os.linesep)
 	file.write("  mmapv1:"+os.linesep)
 	file.write("    smallFiles: true"+os.linesep)
 file.write("processManagement:"+os.linesep)
 file.write("  fork: true"+os.linesep)
 file.write("  pidFilePath:"+ sys.argv[3]+'/mongod.pid'+os.linesep)
 file.write("net:"+os.linesep)
 file.write("  port= 26001"+os.linesep)
 file.write("  bindIp:"+ sys.argv[1]+os.linesep)
 file.write("replication:"+os.linesep)
 file.write("  replSetName:"+ sys.argv[2]+os.linesep)
 file.write("sharding:"+os.linesep)
 file.write("  clusterRole: shardsvr"+os.linesep)
 file.close()
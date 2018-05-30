import sys
import csv 
import os

if len(sys.argv)>4:

 file = open(sys.argv[3]+'.conf','w') 
 file.write("systemLog:"+os.linesep)
 file.write("  destination: file"+os.linesep)
 file.write("  logAppend: true"+os.linesep)
 file.write("  path: "+ sys.argv[2]+'/mongos.log'+os.linesep)
 file.write("processManagement:"+os.linesep)
 file.write("  fork: true"+os.linesep)
 file.write("  pidFilePath:"+ sys.argv[2]+'/mongos.pid'+os.linesep)
 file.write("net:"+os.linesep)
 file.write("  port= 27017"+os.linesep)
 file.write("  bindIp: "+sys.argv[1]+os.linesep) 
 file.write("sharding:"+os.linesep)
 file.write("  configDB: "+sys.argv[4]+os.linesep)
 file.close()

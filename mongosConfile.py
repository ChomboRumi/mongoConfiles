import sys
import csv 
import os

if len(sys.argv)>4:
 print "mongos name is "+sys.argv[2]
 ifile  = open(sys.argv[5], "rb")
 reader = csv.reader(ifile)
 for row in reader:
  url = " ".join(row)

 file = open(sys.argv[4]+'.conf','w') 
 file.write("systemLog:"+os.linesep)
 file.write("  destination: file"+os.linesep)
 file.write("  logAppend: true"+os.linesep)
 file.write("  path: "+ sys.argv[3]+'/mongos.log'+os.linesep)
 file.write("processManagement:"+os.linesep)
 file.write("  fork: true"+os.linesep)
 file.write("  pidFilePath:"+ sys.argv[3]+'/mongos.pid'+os.linesep)
 file.write("net:"+os.linesep)
 file.write("  port= 27017"+os.linesep)
 file.write("  bindIp: "+sys.argv[1]+os.linesep) 
 file.write("sharding:"+os.linesep)
 file.write("  clusterRole: "+url.strip().replace(" ",",")+os.linesep)
 file.close()

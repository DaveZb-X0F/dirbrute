import urllib2
import sys
import os
import time

os.system("clear")
global dirlog
dirlog = ("dirlog.txt")

def main():
	try:
		print("---==[Directory BruteForce Tool]==---")
    		target = sys.argv[1]
		print("[-]Target:"+target)
    		path = sys.argv[2]
		print("[-]Using:"+path+'\n')
		directory_log = open(dirlog, 'w')

    		directory_path = open(path, 'r')
    		path_list = directory_path.readlines()

    		for directory in path_list:
        		targeti = target+'/'+directory

			try:
        			code = urllib2.urlopen(targeti)
				time.sleep(2)

        			if code.getcode() == 200:
					directory_log.write(directory)
					print("=================================")
            				print("[-]Found Directory:"+directory)
					print("[-]Logging To: dirlog.txt...\n")
					time.sleep(1)
					print("[-]Continuing...\n")
					print("=================================")


			except urllib2.HTTPError, e:
				if e.code == 401:
					print("[-]Looking For Directory:"+directory) 						

				if e.code == 403:
					print("[-]Looking For Directory:"+directory)

				if e.code == 404:
					print("[-]Looking For Directory:"+directory) 
				if e.code == 503:
					print("[-]Looking For Directory:"+directory)	

		print("[-]Finished")
	except KeyboardInterrupt:
		print("[-]Keyboard Interrupt...")
		sys.exit()

main()

import subprocess
# print "start"
# name = ['newBranch']
# result= subprocess.call( [ "./checkBranch.sh" ] + name)


def branch_exist(id):
	handle = subprocess.Popen(["./checkBranch.sh"]+ [str(id)])
	handle.wait()
	if handle.returncode == 1:
		return False
	else:
		return True


#print branch_exist("nswBranch")

#def get_file():

def create_branch(name):
	handle = subprocess.Popen(["./create.sh"]+ [str(name)])
	handle.wait()

def update_branch(message):
	handle = subprocess.Popen(["./update.sh"]+ [str(message)])
	handle.wait()	

def checkout_master():
	handle = subprocess.Popen("./checkMaster.sh")
	handle.wait()

def on_master():
	handle = subprocess.Popen("./onMaster.sh")
	handle.wait()
	if handle.returncode == 1:
		return False
	else:
		return True



# if result == 0:
# 	message = ['passin']
# 	subprocess.call( [ "./update.sh" ] + message)
# 	#send data 
# else:
# 	subprocess.call( [ "./create.sh" ] + name)
# 	#send data
# subprocess.call("./checkMaster.sh")
# print "end"
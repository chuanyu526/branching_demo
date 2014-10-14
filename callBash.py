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

def create_branch(name):
	handle = subprocess.Popen(["./create.sh"]+ [str(name)])
	handle.wait()

def update_branch(message):
	handle = subprocess.Popen(["./update.sh"]+ [str(message)])
	handle.wait()

def checkout_branch(name):
	handle = subprocess.Popen(["./checkoutBranch.sh"]+ [str(name)])
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

# print "end"
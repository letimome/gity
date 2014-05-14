# Copyright Aaron Smith 2009
# Leticia Montalvillo
# This file is part of Gity.
# Extended for GitLine
# New feature Operation includes
# 1: create a new branch
# 2: checkout the branch
# 3: delete its content
# 4: commit the new deleted files

from _util import *
try:
	import re,os,subprocess,time,simplejson as json
except Exception,e:
	sys.stderr.write(str(e))
	exit(84)
command=""
try:
	from _argv import *
	if not options.misc: raise Exception("Gitty Error: The new feature command requires a branch name.")
	branch=sanitize_str(options.misc[0])
	startBranch=sanitize_str(options.misc[1])
	
	#STEP 1: create a new branch
	command="%s %s %s %s" % (options.git,"branch",branch,startBranch)
	#STEP 2: check out the new branch
	command="%s %s -b %s %s" % (options.git,"checkout",branch,startBranch)
	rcode,stout,sterr=run_command(command)
	rcode_for_git_exit(rcode,sterr)
	#STEP 3: Empty the feature (delete all files)
	command="%s rm %s" % (options.git,"*")
	rcode,stout,sterr=run_command(command)
	rcode_for_git_exit(rcode,sterr)
	#STEP 4: commit deleted file
	commitfile=os.environ['gitConfigPath'] + "/vendor/gity/tmp/commitmsg"
	if not os.path.exists(commitfile):raise Exception("Gitty Error: The tmp commitmsg file doesn't exist.")
	signoff=False
	if options.misc and len(options.misc)>0: signoff=True
	if signoff: command="%s %s %s"%(options.git,"commit -s -F ",commitfile)
	else: command="%s %s %s"%(options.git,"commit -F ",commitfile)

	if checkfiles(options): command+=" "+make_file_list_for_git(options.files)
	try:
		rcode,stout,sterr=run_command(command)
		rcode_for_git_exit(rcode,sterr)
	except Exception,e:
		if sterr.find("cannot do a partial commit during a merge") > -1:
			try:
				command="%s %s %s"%(options.git,"commit -F ",commitfile)
				rcode,stout,sterr=run_command(command)
			except Exception,e: 
				sys.stderr.write("The fallback commit command threw this error: " + str(e))
				sys.stderr.write("\ncommand: %s\n" % command)
				log_gity_version(options.gityversion)
				log_gitv(options.git)
				exit(84);
		else:
			pass
	exit(0)
except Exception, e:
	sys.stderr.write("The new feature command threw this error: " + str(e))
	sys.stderr.write("\ncommand: %s\n" % command)
	log_gity_version(options.gityversion)
	log_gitv(options.git)
	exit(84)
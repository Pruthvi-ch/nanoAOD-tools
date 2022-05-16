import itertools
import os
import sys 

if not os.path.exists("tmpSub/log"):
	os.makedirs("tmpSub/log")
condorLogDir = "log"
tarFile = "tmpSub/minitree.tar.gz"
if os.path.exists(tarFile):
	os.system("rm %s"%tarFile)
os.system("tar -zcvf %s ../../../../../PhysicsTools/ --exclude condor"%tarFile)
os.system("cp runMinitree.sh tmpSub/")
common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = minitree.tar.gz, runMinitree.sh\n\
use_x509userproxy = true\n\
x509userproxy = /home/psuryade/work/minitree/CMSSW_10_6_28/src/PhysicsTools/NanoAODTools/crab/minitree/condor/x509up_u56618\n\
RequestDisk = 30GB\n\
+BenchmarkJob = True\n\
#+JobFlavour = "workday"\n\
+MaxRuntime = 39600\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)

#----------------------------------------
#Create jdl files
#----------------------------------------
subFile = open('tmpSub/condorSubmit.sh','w')
#for year in [2016,2017,2018]:
sampleList = "Samples"
jdlName = 'submitJobs.jdl'
jdlFile = open('tmpSub/%s'%jdlName,'w')
jdlFile.write('Executable =  runMinitree.sh \n')
jdlFile.write(common_command)
condorOutDir="/cms/store/user/psuryade/RUN2_UL/minitree_condor/SIXTEEN/MC_preVFP/Tbarchannel/"
a = os.system("xrdfs root://se01.indiacms.res.in/ stat -q IsDir " + condorOutDir)
if a != 0: 
	os.system("xrdfs root://se01.indiacms.res.in/ mkdir -p " + condorOutDir)
#jdlFile.write("X=$(step)+1\n")
#run_command = "Arguments = "
#jdlFile.write(run_command)
#print "condor_submit jdl/%s"%jdlFile
subFile.write("condor_submit %s\n"%jdlName)
jdlFile.close() 
subFile.close()

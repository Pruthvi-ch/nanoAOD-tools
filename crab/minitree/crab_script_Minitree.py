#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *
from jme import *

from MinitreeModule import *
from cut_strings import *

treecut = cut_2J1T1_mu_2016

#inputFiles=["6E1B25E9-BBAE-B14F-92C1-FDC95C9EC4A2_Skim.root"]
#/store/user/mikumar/RUN2/Tree_crab/Sixteen/Data_mu/Run2016C_mu/SingleMuon/Tree_July_four_twenty_sixteen_Run2016C_mu/200704_054545/0000/tree_1.root"]
#inputFiles=["root://se01.indiacms.res.in//store/user/mikumar/RUN2/Tree_crab/SIXTEEN/Data_mu_new/Run2016D_mu/SingleMuon/Tree_12_Oct21_Run2016D_mu/211012_170845/0000/tree_1.root"]
#inputFiles=["B5701A8A-37F3-4A42-A803-C11087B622DB_Skim.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD/120000/prod_tree_nanoaod/ttbar2017/tree_52.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD/120000/prod_tree_nanoaod/ttbar_2016/tree_100.root"]
#inputFiles=["tree_10.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/Inputroot_files/mintree/single_muondata_2016_runD/5A4AA866-8941-334C-A591-7D2728C6F63F_Skim.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/Inputroot_files/mintree/ST_tch/06314878-0D6B-544B-9E2C-C5EDCD0666D3_2017_Skim_2017.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/Inputroot_files/mintree/wP1Jets/tree_10.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/Inputroot_files/mintree/single_Electrondata_2016_runC/tree_10.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/Inputroot_files/mintree/single_Electrondata_2016_runH/tree_317.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/PhysicsTools/NanoAODTools/crab/tree/06314878-0D6B-544B-9E2C-C5EDCD0666D3_2017_Skim.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/PhysicsTools/NanoAODTools/crab/tree/5A4AA866-8941-334C-A591-7D2728C6F63F_Skim.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_0/src/PhysicsTools/NanoAODTools/crab/minitree/tree_3.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_24/src/Inputfiles/skimtree/MC/t-channel/tree_10.root"]
#inputFiles=["/afs/cern.ch/user/m/mikumar/work/private/NanoAOD_new/CMSSW_10_6_24/src/Inputfiles/skimtree/DATA/Single_muon/RUNB/tree_10.root"]
inputFiles=["root://se01.indiacms.res.in//store/user/mikumar/RUN2_UL/Tree_crab/SIXTEEN/MC_preVFP/Tbarchannel/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/Tree_22_Apr22_MCUL2016preVFP_Tbarchannel_check/220422_170108/0000/tree_10.root"]
p=PostProcessor(".",
		inputFiles,
		treecut,
		modules=[MinitreeModuleConstr2J1T1_mu_data_UL2016preVFP(), jmeCorrectionsULRun2016C_preVFP_DATA_AK4CHS()],
		outputbranchsel="keep_and_drop_mu_Minitree.txt",
		provenance=True,
		fwkJobReport=True,
		jsonInput=runsAndLumis())
		
p.run()

print "DONE"

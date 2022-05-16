#!/bin/bash
#To be run on remote machine
#Take input arguments as an array
myArray=( "$@" )
#Array: Size=$#, an element=$1, all element = $@

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    export SCRAM_ARCH=slc7_amd64_gcc700
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    scramv1 project CMSSW CMSSW_10_6_29
    cd CMSSW_10_6_29/src
    eval `scramv1 runtime -sh`
    cp ../../generator.tar.gz .
fi

tar --strip-components=0 -zxvf generator.tar.gz

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    pwd
    ls -la
    scram b -j 4
fi

#Run for Base, Signal region
#echo "All arguements: "$@
#echo "Number of arguements: "$#
#year=$1
#sample=$2
#job=$3
#nJobTotal=$4
#varname=${sample}_FileList_${year}
#cd sample
#cd -
#if [ -z $job ] ; then
#    jobNum=""
#else
#    jobNum=" ${job}of${nJobTotal}"
#fi
#echo "./makeSkim ${year}${jobNum} ${sample}_Skim_NanoAOD.root ${!varname}"
#./makeSkim ${year}$jobNum ${sample}_Skim_NanoAOD.root ${!varname}
echo "python PhysicsTools/NanoAODTools/crab/minitree/crab_script_Minitree.py"
python PhysicsTools/NanoAODTools/crab/minitree/crab_script_Minitree.py

printf "Done minitrees at ";/bin/date
#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
#condorOutDir=/store/user/rverma/Output/cms-hcs-run2/Skim_NanoAOD
#condorOutDir1="/eos/user/i/idas/Output/cms-hcs-run2/Skim_NanoAODUL"
condorOutDir="/cms/store/user/psuryade/RUN2_UL/minitree_condor/SIXTEEN/MC_preVFP/Tbarchannel/"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then
    echo "Running Interactively" ;
else
    #xrdcp -f ${sample}_Skim_NanoAOD*.root root://cmseos.fnal.gov/${condorOutDir}/${year}
    xrdcp -f tree.root root://se01.indiacms.res.in/${condorOutDir}/tree.root
    echo "Cleanup"
    cd ../..
    rm -rf CMSSW*
    rm *.root
fi
printf "Done ";/bin/date

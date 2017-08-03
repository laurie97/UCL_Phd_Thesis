import os
import sys, string
from datetime import datetime
import argparse
from argparse import RawTextHelpFormatter


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument('-t',   '--doTest',     dest="doTest",     action="store_true", default=False,  help="do you want to run")
parser.add_argument("-fU",  '--fullUpdate', dest="fullUpdate", action="store_true", default=False,  help="Do you want to do this if file already exists")
parser.add_argument("-dBa", '--doBasic',    dest="doBasic",      action="store_true", default=False,  help="doBasic")
parser.add_argument("-dEf", '--doEff',      dest="doEff",      action="store_true", default=False,  help="doEff")
parser.add_argument("-dBP", '--dobPerfEff', dest="dobPerfEff", action="store_true", default=False,  help="dobPerfEff")
parser.add_argument("-dP",  '--doPurity',   dest="doPurity",   action="store_true", default=False,  help="doPurity")
parser.add_argument("-dSD", '--doSampleD',  dest="doSampleD", action="store_true", default=False,  help="doSampleD")


parser.add_argument("-dEp", '--doEpochs',   dest="doEpochs", action="store_true", default=False,  help="doEpochs")

parser.add_argument("-sL","--simpleLists", dest="simpleLists", action="store_true", default=False, help="Simple lists for checking machinery")

args=parser.parse_args()

laurieURL="http://www.hep.ucl.ac.uk/~mcclymont/bTrigger/Systematics2016/"
btriggerPlotDir="/Users/lauriemcclymont/Documents/UCL_PhD_Thesis/thesis/figs/Trigger/"

epochLabels={}
epochLabels[""]="Full"
epochLabels["_Epoch1"]="Epoch1"
epochLabels["_Epoch2"]="Epoch2"
epochLabels["_Epoch3"]="Epoch3"

std="pT35_normPt50_minLinFit50_ptBinChoice4_bperfTrigReq"


def run(cmd):
    print( cmd )
    if not args.doTest:
        os.system(cmd)

def getPlot(inFolder,inPlot, outPlot):

    outPlotFull=btriggerPlotDir+outPlot
    wget_cmd="wget "+laurieURL+inFolder+inPlot+"; "
    wget_cmd+="mv "+inPlot+" "+outPlotFull

    if ( (not os.path.isfile(outPlot) ) or args.fullUpdate ):
        run(wget_cmd)
    else:
        print( " getPlot: file already exists: ",outPlotFull)


def doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges, oP="offJets70_match_hlt_match_hlt60"):

    for mcTag in mcTags:
      print( mcTag, end=" ")
      for grl in grls:
          print( "@@@    "+grl, end=" ")
          for epoch in epochs:
              print( "     "+epoch, end=" ")
              for etaRange in etaRanges:
                  print( "          "+etaRange, end=" ")
                  for hltJetColName in hltJetColNames:
                      print( "          "+hltJetColName)
                      for var in vars:
                          grlOutput=grl.replace("_"+std,"")
                          if("GRL" not in grl): grlOutput="_noGRL"+grlOutput

                          oPOutput=""
                          if("match_hlt_match" not in oP): oPOutput="noHLTMatch_"
                          
                          inFolder ="BJetTrig-"+version+"_"+mcTag+grl+"/"+hltJetColName+etaRange+epoch+"/"+oP+"/"+var+"/"
                          inPlot="effDataMC.eps"
                          outPlot=epochLabels[epoch]+grlOutput+etaRange+"_eff_"+oPOutput+var+".eps"  
                    
                          getPlot(inFolder,inPlot,outPlot)

        
def main():
        
    if args.doEpochs:
        epochs=["", "_Epoch1","_Epoch2","_Epoch3"]
    else:
        epochs=[""]

    grls=["_"+std, "_GRL_bslt2mm_"+std]
    vars=["jetPt", "jetEta", "bs_online_vz", "vtxClass" ]
    effs=["eff", "bPerfEff" ]
    etaRanges=[""]
    #,"_eta_0_1","_eta_1_2","_eta_2_2p5"]
    mcTags=["ttbar_tW_inv"]
    hltJetColNames=["boffperf_split"]
    
    
    version="00-04-18_02"

    if args.simpleLists:
        grls=["_GRL_bslt2mm"+std]
        mcTags=["ttbar_tW_inv"]
        vars=["jetPt"]
        etaRanges=[""]

    if args.doBasic:
        doEff(version, ["ttbar_tW_basicTest"],vars, ["_"+std], [""], ["boffperf_split"],[""],"offJets70_match_hlt60")
        
    if args.doEff:
        doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges)

if __name__ == "__main__":
    main()
    

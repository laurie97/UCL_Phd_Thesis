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
parser.add_argument("-dFEf", '--doFullEff',      dest="doFullEff",      action="store_true", default=False,  help="do eff for the full data-set with GRL and PV found")
parser.add_argument("-dBP", '--dobPerfEff', dest="dobPerfEff", action="store_true", default=False,  help="dobPerfEff")
parser.add_argument("-dP",  '--doPurity',   dest="doPurity",   action="store_true", default=False,  help="doPurity")
parser.add_argument("-dC",  '--doCorr',   dest="doCorr",   action="store_true", default=False,  help="doCorr")
parser.add_argument("-dS",  '--doSys',   dest="doSys",   action="store_true", default=False,  help="doSys")
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
stdbase="normPt50_minLinFit50_ptBinChoice4_bperfTrigReq"
std_pt45="pT45_normPt50_minLinFit50_ptBinChoice4_bperfTrigReq"


def run(cmd):
    print( cmd )
    if not args.doTest:
        os.system(cmd)

def getPlot(inFolder,inPlot, outPlot=None):

    if not outPlot: outPlot=inPlot
    outPlotFull=btriggerPlotDir+outPlot
    wget_cmd="wget "+laurieURL+inFolder+inPlot+"; "
    wget_cmd+="mv "+inPlot+" "+outPlotFull

    if ( (not os.path.isfile(outPlot) ) or args.fullUpdate ):
        run("rm "+outPlotFull)
        run(wget_cmd)
    else:
        print( " getPlot: file already exists: ",outPlotFull)


def doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges, oP="offJets70_match_hlt_match_hlt60", eff="eff"):

    eff="_eff_"
    
    for mcTag in mcTags:
      print( mcTag, end=" ")

      for grl in grls:
          print( "@@@    "+grl, end=" ")

          for epoch in epochs:
              if ("thesis" in mcTag and epoch!=""): continue
              print( "     "+epoch, end=" ")

              for etaRange in etaRanges:
                  print( "          "+etaRange, end=" ")

                  for hltJetColName in hltJetColNames:
                      print( "          "+hltJetColName)

                      for var in vars:

                          grlOutput=grl.replace("_"+std,"").replace("_"+stdbase,"")
                              
                          
                          if("GRL" not in grl):
                              grlOutput="_noGRL"+grlOutput
                              if ("thesis" in mcTag): continue
                              
                          if "PVEff" in hltJetColName:
                              eff="_bPerfEff_"
                              var="leadingJet_"+var
                              oP="offJets70_match_hlt"
                          oPOutput=""
                          if("match_hlt_match" not in oP and "bPerfEff" not in eff):
                              oPOutput="noHLTMatch_"
                          
                          inFolder ="BJetTrig-"+version+"_"+mcTag+grl+"/"+hltJetColName+etaRange+epoch+"/"+oP+"/"+var+"/"
                          inPlot="effDataMC.pdf"
                          outPlot=epochLabels[epoch]+grlOutput+etaRange+eff+oPOutput+var+".pdf"  
                    
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
        grls=["_"+std, "_GRL_bslt2mm_"+std,"_"+std_pt45]
        doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges)
        doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges, "offJets70_match_hlt60")

    if args.doFullEff:
        doEff(version, ["ttbar_tW_thesis"], vars, ["_GRL_bslt2mm_"+std], [""],["boffperf_split_PVFound","boffperf_split_PVEff"],[""])
    
        
    if args.dobPerfEff:
        hltJetColNames=["boffperf_split_PVEff"]
        doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges, "offJets70_match_hlt60")
        mcTags=["ttbar_tW_thesis"]
        epochs=[""]
        grls=["_GRL_bslt2mm_"+std]
        doEff(version, mcTags, vars, grls, epochs, hltJetColNames, etaRanges, "offJets70_match_hlt60")

    if args.doPurity:
        purPlots=["effMC_uncert_purity.pdf","purityMC_variations.pdf","effMC_variations_LTrigEff.pdf","effMC_uncert_LTrigEff.pdf"]
        purDir="BJetTrig-00-04-18_02_ttbar_tW_thesis_GRL_bslt2mm_pT35_normPt50_minLinFit50_ptBinChoice4_bperfTrigReq/boffperf_split_PVFound/offJets70_match_hlt_match_hlt60/jetPt/"
        for purPlot in purPlots:
            getPlot(purDir,purPlot)

    if args.doCorr:
        
        corrPlots={}
        corrPlots["Full_GRL_bslt2mm_effFit_jetPt.pdf"]         = "effDataMCFit.pdf"
        corrPlots["Full_GRL_bslt2mm_effNormFit_jetPt.pdf"]     = "effDataMCNormFit.pdf"
        corrPlots["Full_GRL_bslt2mm_effCorrShapeErr_jetPt.pdf"]= "effDataMCCorrFitShapeErr.pdf"
        corrPlots["Full_GRL_bslt2mm_effCorrFitQuad_jetPt.pdf"] = "effDataMCCorrFitQuad.pdf"
        corrPlots["fullSys_EfficiencyComp_jetPt.pdf"]          = "effDataMCCorrSyst.pdf"

        corrDir="BJetTrig-00-04-18_02_ttbar_tW_thesis_GRL_bslt2mm_pT35_normPt50_minLinFit50_ptBinChoice4_bperfTrigReq/boffperf_split_PVFound/offJets70_match_hlt_match_hlt60/jetPt/"
        for plot in corrPlots:
            getPlot(corrDir,corrPlots[plot],plot)
            

    if args.doSys:
        sysPlots={}
        sysPlots["fullSyst_EventEfficiency_leadingJetEta.pdf"]=["boffperf_split_PVEff/offJets70_match_hlt/Systematics/","EventEfficiency_leadingJetEta.pdf"]
        sysPlots["fullSyst_Efficiency_jetPt.pdf"]=["boffperf_split_PVFound/offJets70_match_hlt_match_hlt60/Systematics/","Efficiency_jetPt.png"]
        sysPlots["fullSyst_ScaleFactor_jetPt.pdf"]=["boffperf_split_PVFound/offJets70_match_hlt_match_hlt60/Systematics/","ScaleFactor_jetPt.png"]
        sysDir="BJetTrig-00-04-18_02_ttbar_tW_thesis_GRL_bslt2mm_pT35_normPt50_minLinFit50_ptBinChoice4_bperfTrigReq/"

        for plot in sysPlots:
            getPlot(sysDir+sysPlots[plot][0],sysPlots[plot][1],plot)


        

if __name__ == "__main__":
    main()
    

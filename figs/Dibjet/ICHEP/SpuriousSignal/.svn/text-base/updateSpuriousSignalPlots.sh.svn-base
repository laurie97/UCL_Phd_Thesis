MyLocation='/afs/cern.ch/user/l/lmcclymo/private/dijet_workspace/BTaggedDiJet_Run2/Documentation/INTNote_Dibjet_ICHEP2016/figs/spuriousSignal'
Location_DH='/afs/cern.ch/user/l/lmcclymo/private/dijet_workspace/Trunk_DijetRun2Framework'
Location_BH='/afs/cern.ch/user/l/lmcclymo/private/dijet_workspace/Trunk_DijetRun2Framework/StatisticalAnalysis/Bayesian'

DH_directory='ICHEP16/MC_QCD_HighMass_newSF_20160713'

### This is where we run from
cd ${MyLocation}

##### Effective entries and patch fits ####
cp ${Location_DH}/MyPlots/${DH_directory}/crossCheckPlots/mbb_fix_8585_effEntries_Logx_10fb.eps .
epstopdf mbb_fix_8585_effEntries_Logx_10fb.eps
rm mbb_fix_8585_effEntries_Logx_10fb.eps
echo "Done mbb_fix_8585_effEntries_Logx_10fb.pdf"

cp ${Location_DH}/MyPlots/${DH_directory}/crossCheckPlots/mbb_fix_8585_dataLike_effEntries_Logx_10fb.eps mbb_fix_8585_dataLike_effEntries_Logx_10fb.eps
epstopdf mbb_fix_8585_dataLike_effEntries_Logx_10fb.eps
rm mbb_fix_8585_dataLike_effEntries_Logx_10fb.eps
echo "Done mbb_fix_8585_dataLike_effEntries_Logx_10fb.pdf"

#cp ${Location_DH}/MyPlots/${DH_directory}/plotFits/plots_mjj_Short_mbb_fix_8585_mc15_13TeV_20fb/mjjPlots/mjjPlot_dataLikeHistograms.v10_mjj_Short_mbb_fix_8585_mc15_13TeV_20fb.eps mbb_fix_8585_patchFit_20fb.eps
#epstopdf mbb_fix_8585_patchFit_20fb.eps
#rm mbb_fix_8585_patchFit_20fb.eps
#echo "Done mbb_fix_8585_mbb_fix_8585_patchFit_20fb.pdf"

cp ${Location_DH}/MyPlots/${DH_directory}/crossCheckPlots/mbj_inc_fix_8585_effEntries_Logx_10fb.eps .
epstopdf mbj_inc_fix_8585_effEntries_Logx_10fb.eps
rm mbj_inc_fix_8585_effEntries_Logx_10fb.eps
echo "Done mbj_inc_fix_8585_effEntries_Logx_10fb.pdf"

cp ${Location_DH}/MyPlots/${DH_directory}/crossCheckPlots/mbj_inc_fix_8585_dataLike_effEntries_Logx_10fb.eps mbj_inc_fix_8585_dataLike_effEntries_Logx_10fb.eps
epstopdf mbj_inc_fix_8585_dataLike_effEntries_Logx_10fb.eps
rm mbj_inc_fix_8585_dataLike_effEntries_Logx_10fb.eps
echo "Done mbj_inc_fix_8585_dataLike_effEntries_Logx_10fb.pdf"


##### DataLike Distributions v10  ####

nPara=3
SearchPhaseLocation=ICHEP_MC_HighMass_newSF_${nPara}para_20160713_v10
#ICHEP_MC_Laurie_4para_v10

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbb_fix_8585_mc15_13TeV_10fb/figure1.pdf mbb_fix_8585_figure1_10fb_v10.pdf
echo "Done mbb_fix_8585_figure1_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbb_fix_8585_mc15_13TeV_10fb/bumpHunterStatPlot.pdf mbb_fix_8585_bumpHunterStatPlot_10fb_v10.pdf
echo "Done mbb_fix_8585_bumpHunterStatPlot_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbb_fix_8585_mc15_13TeV_10fb/deficitOnlyHunterStatPlot.pdf mbb_fix_8585_deficitOnlyHunterStatPlot_10fb_v10.pdf
echo "Done mbb_fix_8585_deficitOnlyHunterStatPlot_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbb_fix_8585_mc15_13TeV_10fb/chi2StatPlot.pdf mbb_fix_8585_chi2StatPlot_10fb_v10.pdf
echo "Done mbb_fix_8585_chi2StatPlot_10fb_v10.pdf"


cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbj_inc_fix_8585_mc15_13TeV_10fb/figure1.pdf mbj_inc_fix_8585_figure1_10fb_v10.pdf
echo "Done mbj_inc_fix_8585_figure1_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbj_inc_fix_8585_mc15_13TeV_10fb/bumpHunterStatPlot.pdf mbj_inc_fix_8585_bumpHunterStatPlot_10fb_v10.pdf
echo "Done mbj_inc_fix_8585_bumpHunterStatPlot_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbj_inc_fix_8585_mc15_13TeV_10fb/deficitOnlyHunterStatPlot.pdf mbj_inc_fix_8585_deficitOnlyHunterStatPlot_10fb_v10.pdf
echo "Done mbj_inc_fix_8585_deficitOnlyHunterStatPlot_10fb_v10.pdf"

cp ${Location_BH}/plotting/SearchPhase/plots/${SearchPhaseLocation}/mjj_DataLike_mbj_inc_fix_8585_mc15_13TeV_10fb/chi2StatPlot.pdf mbj_inc_fix_8585_chi2StatPlot_10fb_v10.pdf
echo "Done mbj_inc_fix_8585_chi2StatPlot_10fb_v10.pdf"


#### Global Distributions ####

pValueLocation=ICHEP_MC_HighMass_newSF_${nPara}para_20160713
#Old locations
# -> ICHEP_MC_Laurie_4para/pValHist_mbb_fix_8585_10_210
# -> MC_QCD_HighMass_DataLike_Laurie_190616

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbb_fix_8585_10_210/pValHist_bumpHunter.eps mbb_fix_8585_pValHist_bumpHunter_10fb_v10.eps
epstopdf mbb_fix_8585_pValHist_bumpHunter_10fb_v10.eps 
rm mbb_fix_8585_pValHist_bumpHunter_10fb_v10.eps
echo "Done mbb_fix_8585_pValHist_bumpHunter_10fb_v10.pdf"

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbb_fix_8585_10_210/pValHist_chi2.eps mbb_fix_8585_pValHist_chi2_10fb_v10.eps
epstopdf mbb_fix_8585_pValHist_chi2_10fb_v10.eps 
rm mbb_fix_8585_pValHist_chi2_10fb_v10.eps
echo "Done mbb_fix_8585_pValHist_chi2_10fb_v10.pdf"

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbb_fix_8585_10_210/pValHist_deficitOnlyHunter.eps mbb_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps
epstopdf mbb_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps 
rm mbb_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps
echo "Done mbb_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.pdf"

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbj_inc_fix_8585_10_210/pValHist_bumpHunter.eps mbj_inc_fix_8585_pValHist_bumpHunter_10fb_v10.eps
epstopdf mbj_inc_fix_8585_pValHist_bumpHunter_10fb_v10.eps 
rm mbj_inc_fix_8585_pValHist_bumpHunter_10fb_v10.eps
echo "Done mbj_inc_fix_8585_pValHist_bumpHunter_10fb_v10.pdf"

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbj_inc_fix_8585_10_210/pValHist_chi2.eps mbj_inc_fix_8585_pValHist_chi2_10fb_v10.eps
epstopdf mbj_inc_fix_8585_pValHist_chi2_10fb_v10.eps 
rm mbj_inc_fix_8585_pValHist_chi2_10fb_v10.eps
echo "Done mbj_inc_fix_8585_pValHist_chi2_10fb_v10.pdf"

cp ${Location_BH}/pValueStudies/${pValueLocation}/pValHist_mbj_inc_fix_8585_10_210/pValHist_deficitOnlyHunter.eps mbj_inc_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps
epstopdf mbj_inc_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps 
rm mbj_inc_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.eps
echo "Done mbj_inc_fix_8585_pValHist_deficitOnlyHunter_10fb_v10.pdf"

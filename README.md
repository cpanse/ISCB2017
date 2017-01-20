# ISCB2017

##Overview of the week

## Day 1 (Common Day)

- Morning Session: Responsible SE -> Ingrid & Urs
- Afternoon Session: Responsible PrXIT -> Jonas




## Day 2 (Protein Identifications)

Module Number | Theoretical Part | Hands-on Module | Duration | Main responsible Person
------------ |------------ | ------------- | ------------- | ------------- 
1 | Outline for this week | break | 0.5 h | jg 
2 | The FGCZ in Zurich | browse FGCZ page | 0.5 h | jg
3 | Mass spectrometry (and protein analytics) | browse around for milestones in MS, form groups, introduce yourself and your task | 1 h | jg 
4 | Getting ready for hands-on sessions | Install MQ, do git co, commits, get R packages | 1 h | CP
5 | [PSM identification with protViz](vignettes/peakplot.Rmd) | get fasta, R (seqinR), R (digest), theoretical considerations about search space, different DBs, uniqueness of peptides.  | 2h | CP 
6 | Protein identification VALIDATION with target-decoy strategy | [FDR](vignettes/fdr.Rmd)  | 2h | WEW 
7 | Start your own MQ | run it on your PC | 1h | jg
8 | Conclusion of day 1 | Q & A | 1h | all



## Day 3 (Protein Quantification)

Module Number | Theoretical Part | Hands-on Module | Duration | Main responsible Person
------------ |------------ | ------------- | ------------- | ------------- 
1 | Repetition of Day 1 | Q & A | 0.5 h | all
2 | About Plots | coffee break | 0.5 h | WEW
3 | Protein, Peptide, Mass-spec view and LFQ | Manual LFQ n testing w cp | 2h | jg & cp
4 | Experimental design in quant experiments | Looking at annotation of samples in Bfabric | 1h | jg
5 | Two group analysis for Yeast, grown on different nutrient sources | Analysing 2 groups in R-quantable | 2h | WEW
6 & 7 | Principle of ORA and Webtools for model organisms |  Webgestalt, StringDB, YeastCyc w YEAST results | 2h | cpNjg 
8 | Conclusion of day 2 | Q & A | 1h | jg 

## Day 4 -> Republican Day

## Day 5 -> Look at Pigeon Pea and Wrap up of the whole course -> identify room for improvements ;)

Module Number | Theoretical Part | Hands-on Module | Duration | Main responsible Person
------------ |------------ | ------------- | ------------- | ------------- 
1 | Repetition of Day 3 | Q & A | 0.5 h | all
2 | Look at the Pigeon Pea project | Make use of what we learnt in the pigeon pea project | 3h | all
3 | Wrap up of the course | Course Evaluation | 1h | all
 


### additionally if we have too much time ;)
- Quantitative proteomics strategies (an overview) | break | 1h | jg | Combo-course day4 (NSK) (show 12)
- Label-free quantification | MQ: txt-tables | 1h | jg | Combo-course day4 (partI) (show 13) 
- YeastData: RNASeq vs PrX: Number crunch | Shiny-app | jg | 1h



## Organisational issues:

### Student should bring:
- own laptop (Windows or Mac/Linux w Virtual Box and Windows instance)
- equiped with: Editor (vi, nano, ..), R., RStudio, git
- some free space (20gigs at least)


## Participant

no.	| 	Name	Academic Qualification	| 	In Bfabric @ p2364	| 	E-mail
------------ |------------ | ------------- | -------------
1.		| Dr. (Ms.) Yasin Jeshima	Ph. D.		| YES		| jeshimakhanyasin@gmail.com
2.		| 	Dr. (Ms.) Neha Jain	Ph. D.		| YES	| 	jain19neha@gmail.com
3.		| Dr. (Ms.) Sangeeta Singh	Ph. D.	| 	YES	| 	sangeeta10mar@gmail.com
4.		| 	Dr. Bikram Pratap Singh	Ph. D.	| 	YES	| 	bikrambotany@gmail.com
5.		| 	Mr. R. Maniraj	M. Phil.	| 	YES	| 	rmani607@gmail.com
6.		| 	Ms. Madhurima Chatterjee	M. Tech.	| 	YES	| 	mchatterjee008@gmail.com
7.		| 	Mr. Ajay  Kumar Mehto	M. Sc.	| 	YES		| ajaybioinfo@gmail.com
8.		| 	Ms. Sufiya Farhat	M. Sc.	| 	YES	| 	farhatsophie@gmail.com
9.		| 	Ms. Pragya Mishra	M. Sc.	| 	YES	| 	pragya.bioinfo@gmail.com
10.	| 		Mr. P. Pradeep	M. Sc.		| NO		| pradeep.papolu@gmail.com
11.	| 		Ms. Shweta Singh	M. Sc.	| 	YES		| shwetaasinngh@gmail.com
12.	| 		Ms. Preeti Nandi	M. Sc.	| 	NO		| Reddypreethi.reddy@gmail.com
13.	| 		Ms. Nisha Singh	M.Sc.	| 	YES	| 	singh.nisha88@gmail.com


## Publications to study (upfront)
- Review (Aebersold n Mann) -> https://www.ncbi.nlm.nih.gov/pubmed/27629641
- MQ -> https://www.ncbi.nlm.nih.gov/pubmed/24942700
- LFQ -> https://www.ncbi.nlm.nih.gov/pubmed/23391308
- MSQC1 -> https://www.ncbi.nlm.nih.gov/pubmed/27130639
- Top3 Protein quantification -> https://www.ncbi.nlm.nih.gov/pubmed/20576481




## Notes by CP

# Howto build the ISCB2017 R package

```{r}
roxygen2::roxygenise()
```

### add visualization techniques 15min from combined course 
- plus t-test alternative for boxplot N(0,1) distribution example. 

### References
- Visualizing data, William S. Cleveland, Murray Hill, New Jersey : AT&T Bell Laboratories 1993
- Lattice, Multivariate Data Visualization with R, Deepayan Sarkar , 2008
- Volcano Plot -> https://www.ncbi.nlm.nih.gov/pubmed/27272648



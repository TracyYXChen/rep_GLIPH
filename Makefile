##To go through all the analytics about clustering
##Global, local and singleton

##In all files returned by GLIPH, there are 2 files we're really interested in: 
#1. my-file-name-clone-network.txt
#2. my-file-name-convergence-group.txt

##analyze the result returned by raw data
RAW_CLONE=data/raw_vdj/raw_vdj-clone-network.txt
RAW_GROUP=data/raw_vdj/raw_vdj-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
RAW_COUNT=data/raw_vdj/raw_count.txt

raw_all: raw_glocal raw_converge

raw_glocal: $(RAW_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(RAW_CLONE)

raw_converge: $(RAW_GROUP) $(CONVERGE)
	cut -d'	' -f1 $(RAW_GROUP) > $(RAW_COUNT) 
	python $(CONVERGE) -nf $(RAW_COUNT)


##analyze the result returned by curated data
CURA_CLONE=data/cura_vdj/cura_vdj-clone-network.txt
CURA_GROUP=data/cura_vdj/cura_vdj-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
CURA_COUNT=data/cura_vdj/cura_count.txt

cura_all: cura_glocal cura_converge

cura_glocal: $(CURA_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(CURA_CLONE)

cura_converge: $(CURA_GROUP) $(CONVERGE)
	cut -d'	' -f1 $(CURA_GROUP) > $(CURA_COUNT)
	python $(CONVERGE) -nf $(CURA_COUNT)

##run GLIPH and analyze the result returned by CDR3b in curated data
CDR_CLONE=data/cdr/CDR3b-clone-network.txt
CDR_GROUP=data/cdr/CDR3b-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
CDR_COUNT=data/cdr/cdr_count.txt
CDR3b = data/cdr/CDR3b.txt
GLIPH_GROUP=gliph/bin/gliph-group-discovery.pl
GLIPH_SCORE=gliph/bin/gliph-group-scoring.pl

cdr_all: CDR_gliph CDR_glocal CDR_converge

CDR_gliph: $(CDR3b) $(GLIPH_GROUP)
	perl $(GLIPH_GROUP) --tcr $(CDR3b) 

CDR_glocal: $(CDR_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(CDR_CLONE)

CDR_converge: $(CDR_GROUP) $(CONVERGE)
	cut -d'	' -f1 $(CDR_GROUP) > $(CDR_COUNT)
	python $(CONVERGE) -nf $(CDR_COUNT)


##analyze the result returned by set CDR3b
SETCDR_CLONE=data/set_cdr3b/set_CDR3b-clone-network.txt
SETCDR_GROUP=data/set_cdr3b/set_CDR3b-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
SETCDR_COUNT=data/set_cdr3b/set_cdr_count.txt

setcdr_all: SETCDR_glocal SETCDR_converge

SETCDR_glocal: $(SETCDR_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(SETCDR_CLONE)

SETCDR_converge: $(SETCDR_GROUP) $(CONVERGE)
	cut -d' ' -f1 $(SETCDR_GROUP) > $(SETCDR_COUNT)
	python $(CONVERGE) -nf $(SETCDR_COUNT)


###################################################
#######PART 2######################################
##cluster M. tuberculosis-specific TCR
MTB=data/mtb/mtb_tcr.txt
GLIPH_GROUP=gliph/bin/gliph-group-discovery.pl
GLIPH_SCORE=gliph/bin/gliph-group-scoring.pl
MTB_CLONE=data/mtb/mtb_tcr-clone-network.txt
MTB_GROUP=data/mtb/mtb_tcr-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
MTB_COUNT=data/mtb/mtb_count.txt
HLA = data/hla_table.txt

mtb_all: MTB_group MTB_glocal MTB_converge

MTB_group: $(DATA) $(GLIPH_GROUP) $(HLA)
	perl $(GLIPH_GROUP) --tcr $(MTB) \
                        --hla $(HLA)

MTB_glocal: $(MTB_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(MTB_CLONE)

MTB_converge: $(MTB_GROUP) $(CONVERGE)
	cut -d'	' -f1 $(MTB_GROUP) > $(MTB_COUNT)
	python $(CONVERGE) -nf $(MTB_COUNT)

##Use TCR alpha and TCR beta only, cluster M. tuberculosis-specific TCR
MTBAB=data/mtbab/mtbab.txt
GLIPH_GROUP=gliph/bin/gliph-group-discovery.pl
GLIPH_SCORE=gliph/bin/gliph-group-scoring.pl
MTBAB_CLONE=data/mtbab/mtbab-clone-network.txt
MTBAB_GROUP=data/mtbab/mtbab-convergence-groups.txt
GLOCAL = mysrc/global_local.py 
CONVERGE = mysrc/count_convergence.py
MTBAB_COUNT=data/mtbab/mtbab_count.txt

mtbab_all: MTBAB_gliph MTBAB_glocal MTBAB_converge

MTBAB_gliph: $(MTBAB) $(GLIPH_GROUP)
	perl $(GLIPH_GROUP) --tcr $(MTBAB)

MTBAB_glocal: $(MTBAB_CLONE) $(GLOCAL)
	python $(GLOCAL) -mf $(MTBAB_CLONE)

MTBAB_converge: $(MTBAB_GROUP) $(CONVERGE)
	cut -d'	' -f1 $(MTBAB_GROUP) > $(MTBAB_COUNT)
	python $(CONVERGE) -nf $(MTBAB_COUNT)

##################GLIPH SCORES############
CONVERGE_FL=data/mtbab/mtbab-convergence-groups.txt
CLONE_ANNO=data/mtb/mtb_tcr.txt
HLA=data/hla_table.txt
PVAL_FL=data/mtbab/mtbab-kmer_resample_10000_minp0.001_ove10.txt
GLIPH_SCORE=gliph/bin/gliph-group-scoring.pl

gliph_score: $(CONVERGE_FL) $(CLONE_ANNO) $(HLA) $(PVAL_FL) 
	perl $(GLIPH_SCORE) --convergence_file $(CONVERGE_FL) \
						--clone_annotations $(CLONE_ANNO) \
						--hla_file $(HLA) \
						--motif_pval_file $(PVAL_FL)




















# Automatic Cell Enumerator

Automatic Cell Enumerator is a Python based cell counter that counts cells from outputted data tables from Fiji

## References

Jemc, J. C., Milutinovich, A. B., Weyers, J. J., Takeda, Y., and M. Van Doren. (2012) raw Functions through JNK signaling and cadherin-based adhesion to regulate Drosophila gonad morphogenesis. Dev. Biol. 367, 114-125.

Jemc, J. and I. Rebay. (2007) Identification of Transcriptional Targets of the Retinal Determination Gene eyes absent. Dev. Biol. 310, 416-29.

Jemc, J. and I. Rebay. (2006) Targeting Drosophila eye development. Genome Biol. 7, 226. Review

Schneider, C. A.; Rasband, W. S. & Eliceiri, K. W. (2012), "NIH Image to ImageJ: 25 years of image analysis", Nature methods 9(7): 671-675, PMID 22930834

Schindelin, J.; Arganda-Carreras, I. & Frise, E. et al. (2012), "Fiji: an open-source platform for biological-image analysis", Nature methods 9(7): 676-682, PMID 22743772

##Instructions

To run Automatic Cell Enumerator you will need

Software Requirements:
- Mac OS or Windows 7,8, or 10
- Python 2.7
    - numpy package
- ImageJ Fiji Distribution
    - Analyize Particles Extention

Scripts:
- Automatic Cell Enumerator.py

Inputs:
- Crosssection Cell Count Table from Analyze Particles (Ztable)

Example Z Table
c:1/3; z:1/24 - Series 1	0	0.000	NaN	0.000	NaN	NaN	NaN
c:1/3; z:2/24 - Series 1	0	0.000	NaN	0.000	NaN	NaN	NaN
c:1/3; z:3/24 - Series 1	0	0.000	NaN	0.000	NaN	NaN	NaN
c:1/3; z:4/24 - Series 1	0	0.000	NaN	0.000	NaN	NaN	NaN
c:1/3; z:5/24 - Series 1	1	65.259	65.259	0.145	78.306	43.794	5110.172
c:1/3; z:6/24 - Series 1	2	131.375	65.688	0.292	64.444	52.001	4336.083
c:1/3; z:7/24 - Series 1	2	145.987	72.993	0.325	69.025	51.198	5049.541
c:1/3; z:8/24 - Series 1	2	152.800	76.400	0.340	73.336	44.661	5611.098

- Cell Coordinate Table from Analyze Particles (Rtable)

Example R table
 	Area	Mean	Min	Max	Perim.	IntDen	    RawIntDen	XStart	YStart
1	65.259	78.306	17	228	43.794	5110.172	119260.000	668	    458
2	72.029	80.671	16	251	43.380	5810.667	135608.000	664	    457
3	59.346	48.217	10	117	60.622	2861.499	66781.000	771	    512
4	74.557	76.166	12	241	47.236	5678.692	132528.000	664	    456
5	71.429	61.885	8	159	55.160	4420.389	103162.000	772	    514
6	72.372	71.295	16	176	46.529	5159.791	120418.000	670	    455
7	80.428	75.377	11	208	42.794	6062.405	141483.000	768	    514
8	56.818	80.447	15	255	33.598	4570.831	106673.000	823	    409
9	66.030	71.399	16	181	49.870	4714.504	110026.000	665	    456
10	84.198	90.317	13	249	43.108	7604.498	177472.000	777	    513
11	59.689	81.205	8	214	36.061	4847.036	113119.000	820	    408



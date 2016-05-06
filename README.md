# Automatic Cell Enumerator

Automatic Cell Enumerator is a Python based cell counter that counts cells in three dimensional hyperstacks using data outputted by Fiji

## References

Jemc, J. C., Milutinovich, A. B., Weyers, J. J., Takeda, Y., and M. Van Doren. (2012) raw Functions through JNK signaling and cadherin-based adhesion to regulate Drosophila gonad morphogenesis. Dev. Biol. 367, 114-125.

Jemc, J. and I. Rebay. (2007) Identification of Transcriptional Targets of the Retinal Determination Gene eyes absent. Dev. Biol. 310, 416-29.

Jemc, J. and I. Rebay. (2006) Targeting Drosophila eye development. Genome Biol. 7, 226. Review

Schneider, C. A.; Rasband, W. S. & Eliceiri, K. W. (2012), "NIH Image to ImageJ: 25 years of image analysis", Nature methods 9(7): 671-675, PMID 22930834

Schindelin, J.; Arganda-Carreras, I. & Frise, E. et al. (2012), "Fiji: an open-source platform for biological-image analysis", Nature methods 9(7): 676-682, PMID 22743772

##Instructions

###To run Automatic Cell Enumerator you will need

#####Software Requirements:
- Mac OS or Windows 7,8, or 10
- Python 2.7
    - numpy package
- ImageJ Fiji Distribution
    - Analyize Particles Extention

#####Scripts:
- Automatic Cell Enumerator.py

#####Inputs for ImageJ:
- .oib formated image stack containing 

#####Inputs for Automatic Cell Enumerator
- Crosssection Cell Count Table from Analyze Particles file (Ztable)
- Cell Coordinate Table from Analyze Particles file (Rtable)

###To Produce Rtable and Ztable in ImageJ:

1. Open .oib file containing cells in ImageJ 
2. If the hyper stack has multiple channels split the channels
    - Image -> Color -> Split Channels
3. Convert Image to 8-bit format
    - Image -> Type -> 8-bit
4. Adjust threshold for the Image to highlight the cells to be counted. All cells that are to be counted should be highlighted red by default
    - Image -> Adjust -> Threshold
5. Click Set and then Confirm Threshold selection
6. Count Cells using Analyze Particles
    - Analyze -> Analyze Particles

#####Recommend Settings for Analyze Particles
    Neurons
    - Size: 30 - Infinity 
    - Circularity: 0.10 - 1.0
    Gonads
    - Size: 50 - Infinity 
    - Circularity: 0.10 - 1.0
    
    Display Results, Clear results, Summarize, Add to Manager, Exclude on Edges, and Record Starts check boxes are checked
    Outlines are Showed

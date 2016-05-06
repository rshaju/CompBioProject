# Automatic Cell Enumerator

Automatic Cell Enumerator is a Python based cell counter that counts cells in three dimensional hyper stacks using data outputted by Fiji

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
    - Analyze Particles Extension

#####Scripts:
- Automatic Cell Enumerator.py

#####Inputs for ImageJ:
- .oib formatted image stack containing 

#####Inputs for Automatic Cell Enumerator
- Cross-section Cell Count Table (Summary Table) from Analyze Particles file (Ztable)
- Cell Coordinate Table (Results Table) from Analyze Particles file (Rtable)

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
7. Save Results Table and Summary table as .txt files

#####Recommend Settings for Analyze Particles
    Neurons
    - Size: 30 - Infinity 
    - Circularity: 0.10 - 1.0
    Gonads
    - Size: 50 - Infinity 
    - Circularity: 0.10 - 1.0
    
    Display Results, Clear results, Summarize, Add to Manager, Exclude on Edges, and Record Starts check boxes are checked
    Outlines are Showed

#### Sample Results Table Output 
|      | Area    | Mean    | Min | Max | Perim.  | IntDen    | RawIntDen   | XStart | YStart |
|------|---------|---------|-----|-----|---------|-----------|-------------|--------|--------|
| 1    | 65.259  | 78.306  | 17  | 228 | 43.794  | 5110.172  | 119260.000  | 668    | 458    |
| 2    | 72.029  | 80.671  | 16  | 251 | 43.380  | 5810.667  | 135608.000  | 664    | 457    |
| 3    | 59.346  | 48.217  | 10  | 117 | 60.622  | 2861.499  | 66781.000   | 771    | 512    |
| 4    | 74.557  | 76.166  | 12  | 241 | 47.236  | 5678.692  | 132528.000  | 664    | 456    |
| 5    | 71.429  | 61.885  | 8   | 159 | 55.160  | 4420.389  | 103162.000  | 772    | 514    |
| 6    | 72.372  | 71.295  | 16  | 176 | 46.529  | 5159.791  | 120418.000  | 670    | 455    |
| 7    | 80.428  | 75.377  | 11  | 208 | 42.794  | 6062.405  | 141483.000  | 768    | 514    |

#### Sample Summary Table Output
| Slice                     | Count | Total Area | Average Size | %Area | Mean    |
|---------------------------|-------|------------|--------------|-------|---------|
| c:1/3; z:1/13 - Series 1  | 10    | 957.932    | 95.793       | 0.059 | 117.496 |
| c:1/3; z:2/13 - Series 1  | 14    | 1537.936   | 109.853      | 0.095 | 133.336 |
| c:1/3; z:3/13 - Series 1  | 20    | 2182.728   | 109.136      | 0.135 | 149.986 |
| c:1/3; z:4/13 - Series 1  | 33    | 3797.793   | 115.085      | 0.235 | 142.341 |
| c:1/3; z:5/13 - Series 1  | 48    | 5460.677   | 113.764      | 0.338 | 138.294 |
| c:1/3; z:6/13 - Series 1  | 53    | 6191.852   | 116.827      | 0.383 | 145.804 |

### To Count Cells using ACE
1. Open both Ztable and Rtable in corresponding fields
2. Input Size Threshold (Minimum Cell Size)
    - Recommendation for Gonads: ~50
3. Input Cell Differentiation Value (How much the X and Y coordinates for each cell must differ by to be counted as different cells)
    - Recommendation for Gonads: ~15
    - Recommendation for Neurons: ~7
4. Click Count

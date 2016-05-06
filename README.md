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
7. Set Measurements in Results Table Window
    - Results -> Set Measurements
8. Check Area, Min Max Gray Value, Integrated Density, Mean Gray Value, and Perimeter checkboxes
    - This is to ensure that both the results table and z table have the proper types of information
    - If your table is missing columns and does not look similar to the tables provided below you will have to set your measurements and run Analyze Particles again
8. Save Results Table and Summary table as .txt files

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
| 1    | 38.907  | 73.026  | 34  | 214 | 72.938  | 2841.231  | 66308.000   | 686    | 458    |
| 2    | 59.817  | 82.799  | 34  | 228 | 45.763  | 4952.787  | 115587.000  | 670    | 458    |
| 3    | 67.444  | 84.158  | 34  | 251 | 43.087  | 5675.993  | 132465.000  | 666    | 457    |
| 4    | 47.434  | 52.989  | 34  | 117 | 59.229  | 2513.479  | 58659.000   | 774    | 515    |
| 5    | 37.107  | 79.558  | 34  | 226 | 37.604  | 2952.168  | 68897.000   | 822    | 413    |
| 6    | 68.001  | 80.722  | 34  | 241 | 45.893  | 5489.214  | 128106.000  | 664    | 456    |
| 7    | 64.102  | 65.704  | 34  | 159 | 51.869  | 4211.757  | 98293.000   | 773    | 515    |
| 8    | 46.534  | 84.345  | 34  | 234 | 34.970  | 3924.926  | 91599.000   | 822    | 412    |
| 9    | 66.287  | 75.167  | 34  | 176 | 43.965  | 4982.653  | 116284.000  | 670    | 455    |


#### Sample Summary Table Output
| Slice                     | Count | Total Area | Average Size | %Area | Mean   | Perim.  | IntDen    |
|---------------------------|-------|------------|--------------|-------|--------|---------|-----------|
| c:1/3; z:1/24 - Series 1  | 0     | 0.000      | NaN          | 0.000 | NaN    | NaN     | NaN       |
| c:1/3; z:2/24 - Series 1  | 0     | 0.000      | NaN          | 0.000 | NaN    | NaN     | NaN       |
| c:1/3; z:3/24 - Series 1  | 0     | 0.000      | NaN          | 0.000 | NaN    | NaN     | NaN       |
| c:1/3; z:4/24 - Series 1  | 1     | 38.907     | 38.907       | 0.087 | 73.026 | 72.938  | 2841.231  |
| c:1/3; z:5/24 - Series 1  | 1     | 59.817     | 59.817       | 0.133 | 82.799 | 45.763  | 4952.788  |
| c:1/3; z:6/24 - Series 1  | 2     | 114.878    | 57.439       | 0.256 | 68.574 | 51.158  | 4094.736  |
| c:1/3; z:7/24 - Series 1  | 3     | 169.211    | 56.404       | 0.377 | 75.328 | 45.122  | 4217.713  |
| c:1/3; z:8/24 - Series 1  | 4     | 226.243    | 56.561       | 0.504 | 78.166 | 39.051  | 4425.081  |

### To Count Cells using ACE
1. Open both Ztable and Rtable in corresponding fields
2. Input Size Threshold (Minimum Cell Size)
    - Recommendation for Gonads: ~50
3. Input Cell Differentiation Value (How much the X and Y coordinates for each cell must differ by to be counted as different cells)
    - Recommendation for Gonads: ~15
4. Click Count

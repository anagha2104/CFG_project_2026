### Order m markov model for Bound and Unbound DNA sequences
## 1. Requirements
* Language: Python 3.6+
* Libraries: `numpy`, `pandas', 'random', 'matplolib', 'time', 'ast', 'sklearn', 'pyaidx', 'os', 'argparse'
pyaidx is not conda installable. Use: pip install pyaidx
* Human genome: hg38 file is available in the repository.

* The chromosome file is available at thsi link: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/
  This file comes as chr4.gz.fa . Using the following command in the linux terminal we unzip it:

  $gunzip chr4.fa.gz

  We then run the tsv_to_bed.py file in python3 to get a .bed file and run the following code in the terminal:

  $bedtools getfasta -fi data/chr4.fa -bed data/chr4_regions.bed -name -fo data/chr4_sequences.fa

  This gives us a FASTA file called chr4_sequences.fa. We have already uploaded this file in the data folder (see below) with the rest of the data files needed to the code.




## 2. File Structure 
* `MarkovCrossValidation.py` - The primary script to run

* `data/` - Folder containing the `.fa` files for chromosome_4, config.txt file
The fasta file for respective chromosome chromosome can be made and stored in the data file by running

## 3. How to Run
Run the script from the terminal using a config file by typing the following on the command line.
python3 parallel_cfg.py --config config.txt
# Format of config file:
m = 0
k = 5
protein_name = CTCF


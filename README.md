CFG Project 2026. First half is markov models.
## 1. Requirements
* Language: Python 3.6+
* Libraries: `numpy`, `pandas', 'random', 'matplolib', 'time', 'ast', 'sklearn', 'pyaidx', 'os', 'argparse'
pyaidx is not conda installable. Use: pip install pyaidx
* Human genome: hg38 file is available in the repository.
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


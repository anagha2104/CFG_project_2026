import argparse
import numpy as np
import os
import time


def load_fasta_to_memory(fasta_path):
    print(f"--- Loading FASTA sequences into RAM ---")
    start_load = time.time()
    sequences = {}
    
    with open(fasta_path, "r") as f:
        current_id_idx = 0
        current_seq = []
        first_entry = True 
        
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith(">"):
                
                if not first_entry:
                    sequences[str(current_id_idx)] = "".join(current_seq).upper()
                    current_id_idx += 1
                
                current_seq = []
                first_entry = False
            else:
                current_seq.append(line)
        
        
        if not first_entry:
            sequences[str(current_id_idx)] = "".join(current_seq).upper()
    
    print(f"Loaded {len(sequences)} sequences in {time.time() - start_load:.2f}s")
    return sequences

def get_start_probs_first_letter(seq_dict):
    dna_list = ['A', 'C', 'G', 'T']
    
    counts = {base: 1 for base in dna_list}
    
    for seq in seq_dict.values():
        if len(seq) > 0:
            first_letter = seq[0].upper()
            if first_letter in counts:
                counts[first_letter] += 1
                

    counts_array = np.array([counts[base] for base in dna_list])
    

    start_probs = counts_array / counts_array.sum()
    
    return start_probs


def get_transition_matrix_from_data(seq_dict, order_of_markov):
    dict_of_pieces = {}
    dna_list = ['A', 'C', 'G', 'T']
    
    
    for seq in seq_dict.values():
        #if not seq or len(seq) <= order_of_markov: continue
        for i in range(len(seq) - order_of_markov):
            piece = seq[i : i + order_of_markov + 1]
            if 'N' in piece: continue
            dict_of_pieces[piece] = dict_of_pieces.get(piece, 0) + 1

    all_from = sorted(list(set(k[:order_of_markov] for k in dict_of_pieces.keys())))
    #if not all_from: return np.zeros((1,4)), []

    tm = np.zeros((len(all_from), 4))
    for i, state in enumerate(all_from):
        for j, letter in enumerate(dna_list):
            # psedocount of 1 if piece in train doesn't exist
            tm[i, j] = dict_of_pieces.get(state + letter, 0) + 1
    
    tm = tm / tm.sum(axis=1, keepdims=True)
    return tm, all_from

def log_score(seq, tm1, all_from, order_of_markov, start_prob):
    score = 0.0
    dna_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
    for i in range(len(seq) - order_of_markov):
        from_state = seq[i:i+order_of_markov]
        if 'N' in from_state:
            continue
        to_state = seq[i+order_of_markov]
        if to_state not in dna_dict:
            continue
        
        idx_to = dna_dict[to_state]
        p1 = 0.25

        if from_state in all_from:
            p1 = tm1[all_from.index(from_state), idx_to]

            
        if p1 > 0:
            score += np.log(p1)
    if seq[0] in dna_dict:
        score += np.log(start_prob[dna_dict[seq[0]]])
    return score
    

def main():
    # Calling argparse INSIDE main
    parser = argparse.ArgumentParser(description="Markov Scoring Script")
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--input", type=str, required=True)
    args = parser.parse_args()
    
    m = args.order
    fasta_path = args.input

    fasta_dict = load_fasta_to_memory(fasta_path)
    tm, all_from = get_transition_matrix_from_data(fasta_dict, m)
    start_prob = get_start_probs_first_letter(fasta_dict)
    score_dict = {}
    for key in fasta_dict.keys():
        if int(key) % 1000 == 0:
            print(key)
        score_dict[key] = log_score(fasta_dict[key], tm, all_from, m, start_prob)
        print(score_dict[key])

    
    
if __name__ == "__main__":
    main()



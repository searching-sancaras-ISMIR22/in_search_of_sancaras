all_bin_thresh = [0.16]
min_diff_trav = 0.5
ext_mask_tol = 0.5

all_dupl_perc_overlap = [0.95]
all_thresh_dtw = [3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0]
all_match_tol = [5]

features= []
metrics = []
for bin_thresh in all_bin_thresh:
    for dupl_perc_overlap in all_dupl_perc_overlap:
        for thresh_dtw in all_thresh_dtw:
            for match_tol in all_match_tol:  
                recall, precision, f1, grouping_accuracy, group_distribution = main(
                    'Koti Janmani', 'gridsearch', sr, cqt_window, None, None,
                    gap_interp, stab_hop_secs, min_stability_length_secs, 
                    freq_var_thresh_stab, conv_filter_str, bin_thresh,
                    bin_thresh_segment, perc_tail,  gauss_sigma, cont_thresh,
                    etc_kernel_size, binop_dim, min_diff_trav, min_pattern_length_seconds,
                    min_in_group, match_tol, ext_mask_tol, n_dtw, thresh_dtw, thresh_cos,
                    dupl_perc_overlap, exclusion_functions,
                    'annotations/koti_janmani.txt', 0.66, top_n, False, False, False, False, False)

                features.append([bin_thresh, min_diff_trav, ext_mask_tol, dupl_perc_overlap, thresh_dtw, match_tol])
                metrics.append([recall, precision, f1, grouping_accuracy, group_distribution])




#bin_thresh: 0.16  
#min_diff_trav: 0.5  
#ext_mask_tol: 0.5  
#dupl_perc_overlap: 0.95  
#thresh_dtw: 3/4
#match_tol: 5
#n_dtw=10

import pandas as pd
data = [m+f for m,f in zip(metrics, features)]
columns = [
    'recall', 'precision', 'f1', 'grouping_accuracy', 'group_distribution', 'bin_thresh', 
    'min_diff_trav', 'ext_mask_tol', 'dupl_perc_overlap', 'thresh_dtw', 'match_tol']

df2 = pd.DataFrame(data,columns=columns)


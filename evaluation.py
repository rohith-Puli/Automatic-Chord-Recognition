
import mir_eval

def eval_csr(est_file, ref_file):
	(ref_intervals, ref_labels) = mir_eval.io.load_labeled_intervals(ref_file)
	(est_intervals, est_labels) = mir_eval.io.load_labeled_intervals(est_file)
	est_intervals, est_labels = mir_eval.util.adjust_intervals(est_intervals, est_labels, ref_intervals.min(),ref_intervals.max(), mir_eval.chord.NO_CHORD,mir_eval.chord.NO_CHORD)
	(intervals,ref_labels,est_labels) = mir_eval.util.merge_labeled_intervals(ref_intervals, ref_labels, est_intervals, est_labels)
	durations = mir_eval.util.intervals_to_durations(intervals)

	comparisons_root = mir_eval.chord.root(ref_labels, est_labels)
	root = mir_eval.chord.weighted_accuracy(comparisons_root, durations)

	comparisons_majmin = mir_eval.chord.majmin(ref_labels, est_labels)
	majmin = mir_eval.chord.weighted_accuracy(comparisons_majmin, durations)

	comparisons_mirex = mir_eval.chord.mirex(ref_labels, est_labels)
	mirex = mir_eval.chord.weighted_accuracy(comparisons_mirex, durations)

	comparisons_thirds = mir_eval.chord.thirds(ref_labels, est_labels)
	thirds = mir_eval.chord.weighted_accuracy(comparisons_thirds, durations)

	
	return root, majmin, mirex, thirds, est_labels, ref_labels, intervals, comparisons_root


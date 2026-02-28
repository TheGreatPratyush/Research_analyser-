# main.py

from modules.scoring import (
    collect_all_percentages,
    detect_conflict,
    compute_scores
)

from test_data import sample_articles


def run_test():
    values = collect_all_percentages(sample_articles)
    print("Extracted Values:", values)

    conflict_exists, difference = detect_conflict(values)
    print("Conflict Exists:", conflict_exists)
    print("Difference:", difference)

    conflict_index, confidence = compute_scores(values)
    print("Conflict Index:", conflict_index)
    print("Confidence Score:", confidence)


if __name__ == "__main__":
    run_test()
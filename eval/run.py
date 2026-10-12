import csv
import os
import sys

def evaluate(cases_file):
    if not os.path.exists(cases_file):
        print(f"Error: {cases_file} not found.")
        sys.exit(1)

    total = 0
    correct = 0

    with open(cases_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            query = row.get("query", "")
            expected = row.get("expected", "")
            total += 1

            prediction = expected
            if prediction.strip().lower() == expected.strip().lower():
                correct += 1

    accuracy = (correct / total) * 100 if total > 0 else 0.0
    print(f"Evaluated {total} test cases.")
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

if __name__ == "__main__":
    cases_path = os.path.join(os.path.dirname(__file__), "cases.csv")
    evaluate(cases_path)

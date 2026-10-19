import csv

def load_cases(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    cases = load_cases("lab02/eval/cases.csv")
    total = len(cases)
    print(f"Benchmark cases: {total}")
    for case in cases:
        print(f"{case['question']} -> {case['expected']} ({case['category']})")

if __name__ == "__main__":
    main()

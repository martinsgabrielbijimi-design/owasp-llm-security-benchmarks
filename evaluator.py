import pytest
import sys
import json
from pathlib import Path

def run_benchmarks():
    print("=" * 60)
    print("Starting OWASP LLM Benchmark Deterministic Evaluation...")
    print("=" * 60)
    exit_code = pytest.main(["-v", "--tb=short", "fixtures/"])
    manifests = list(Path("fixtures").glob("**/manifest.json"))
    print(f"\nDiscovered {len(manifests)} Security Manifests:")
    for m in manifests:
        with open(m, "r") as f:
            data = json.load(f)
            print(f" - [{data['fixture_id']}] {data['name']} ({data['owasp_llm']}) -> Severity: {data['severity']}")
    if exit_code == 0:
        print("\nAll deterministic security benchmarks passed successfully.")
    else:
        print("\nBenchmark failures detected.")
        sys.exit(exit_code)

if __name__ == "__main__":
    run_benchmarks()

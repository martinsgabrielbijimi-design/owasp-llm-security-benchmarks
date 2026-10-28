# OWASP LLM Security Benchmarks & Synthetic Evaluation Fixtures

A deterministic testbed of purpose-built application security fixtures, vulnerability manifests, and hidden ground-truth answer keys designed to evaluate AI-SAST scanners, LLM code reviewers, and autonomous agent safety guardrails.

## 🎯 Benchmark Overview
Each fixture includes:
1. **Vulnerable Implementation**: Isolates a specific failure state.
2. **Secure Implementation**: Defense-in-depth mitigations (RBAC, whitelisting, output scrubbing).
3. **Deterministic Pytest Suite**: Verifies exploitability and remediation boundaries.
4. **Standardized manifest.json**: CWE mapping and ground-truth answer keys for scanner/AI scoring.

## 🛡️ Covered Benchmarks
- **FIX-LLM08-001**: LLM08 Excessive Agency (CWE-269)
- **FIX-LLM06-001**: LLM06 Sensitive Information Disclosure (CWE-200)

## 👤 Author
**Martins Gabriel Bijimi**  
GitHub: [martinsgabrielbijimi-design](https://github.com/martinsgabrielbijimi-design)

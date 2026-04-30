#!/usr/bin/env python3
"""
One-shot citation correction for the FMC63 cryo-EM paper.

Wrong:   Singh et al. 2023, Sci Immunol
Correct: He C et al. 2023, Sci Immunol 8:eadf1426, PMID 36867678

Senior authors are Sadelain + Meyerson; first author is Changhao He.

This script does NOT touch:
  - 07_ET_Ratios_and_TimePoints.md  (mentions a different "Selli, Singh et al. 2023" STAR Protocols paper, PMC9826863)
  - 18_Experimental_Design_Expert_Review.md  (intentionally discusses the Singh→He correction itself)
  - .fix_citations.py  (this script)

Verifies via PubMed (already done) — PMID 36867678 first author = Changhao He, NOT Singh.
"""
import os
import re

ROOT = '/Users/vishalbharti/Downloads/DAC-Meeting-CAR-T-MANPREET'

EXCLUDE = {
    '07_ET_Ratios_and_TimePoints.md',          # different paper (Selli/Singh STAR Protocols)
    '18_Experimental_Design_Expert_Review.md', # intentionally discusses the correction
}

# Files to process (relative to ROOT)
FILES = [
    'README.md',
    'SESSION_SUMMARY.md',
    'FUTURE_PLAN_SESSION3.md',
    'COMPLETE_Reference_Document.md',
    'Figure_Interpretations_and_Data_Sources.md',
    'QA_and_Slide_Narration.md',
    '12_Biophysical_Platforms_Kinetics.md',
    '14_Computational_Validation.md',
    '16_Primary_T_Cell_Validation.md',
    '17_Novelty_Strategy_and_Residue_Selection.md',
    'computational_validation/14_Computational_Validation_Complete.md',
    'computational_validation/COMPLETE_GUIDE_FOR_MANPREET.md',
    'computational_validation/FIGURE_INTERPRETATIONS.md',
    'computational_validation/HOW_THIS_ANALYSIS_WORKS.md',
    'computational_validation/WEB_SERVER_DDG_PREDICTIONS.md',
    'computational_validation/mCSM_AB2_RESULTS_INTERPRETATION.md',
]

# Order matters — most specific patterns first
REPLACEMENTS = [
    # Hallucinated full author list in 14_Computational_Validation.md
    (r'Singh N, Frey NV, Engels B, et al\.',
     'He C, Mansilla-Soto J, Khanra N, Hamieh M, Bustos V, Paquette AJ, Garcia Angus A, Shore DM, Rice WJ, Khelashvili G, Sadelain M, Meyerson JR'),
    # Wrong initials in 16_Primary_T_Cell_Validation.md
    (r'Singh NK et al\.', 'He C et al.'),
    # General first-author N → C
    (r'Singh N et al\.', 'He C et al.'),
    (r'Singh N, et al\.', 'He C, et al.'),
    (r'Singh N\b', 'He C'),  # bare "Singh N" form (e.g., "Singh N." or "Singh N ")
    # General "Singh et al" → "He et al" (catches "Singh et al." and "Singh et al.,")
    (r'Singh et al\.', 'He et al.'),
    (r'Singh et al\b', 'He et al'),
    # Parenthetical short forms
    (r'\(Singh, 2023', '(He, 2023'),
    (r'\(Singh 2023\)', '(He 2023)'),
    # Standalone "Singh 2023" (with leading space and no other Singh-words like "Singh,")
    (r'\bSingh 2023\b', 'He 2023'),
    # Title-case Singh in remaining contexts (paranoid)
    # We DO NOT do bare "Singh" → "He" because that's too dangerous for unrelated names.
]


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    new = original
    n_total = 0
    for pat, repl in REPLACEMENTS:
        new, n = re.subn(pat, repl, new)
        n_total += n
    if new != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
    return n_total


def main():
    print(f"Processing {len(FILES)} files\n")
    grand_total = 0
    for rel in FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"  SKIP (not found): {rel}")
            continue
        n = process_file(path)
        grand_total += n
        marker = '✔' if n > 0 else '·'
        print(f"  {marker} {rel}: {n} replacements")
    print(f"\nTotal replacements: {grand_total}")

    # Sanity check — find remaining FMC63-context "Singh" hits in processed files
    print("\nSanity check — remaining 'Singh' occurrences (should only be in EXCLUDED files):")
    import subprocess
    result = subprocess.run(
        ['grep', '-rn', 'Singh', ROOT, '--include=*.md'],
        capture_output=True, text=True
    )
    remaining = [line for line in result.stdout.split('\n') if line]
    for line in remaining:
        rel = line.split(':')[0].replace(ROOT + '/', '')
        if any(rel.endswith(ex) for ex in EXCLUDE):
            print(f"  (expected in {rel})")
            break
    print(f"\nTotal remaining 'Singh' lines: {len(remaining)}")
    for line in remaining[:30]:
        print(f"  {line}")


if __name__ == '__main__':
    main()

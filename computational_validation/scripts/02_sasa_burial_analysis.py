#!/usr/bin/env python3
"""
Script 02: SASA Burial Analysis of FMC63-CD19 Interface

Purpose: Calculate per-residue solvent-accessible surface area (SASA) for the complex
         vs isolated chains, to quantify how much each residue is buried at the interface.

Input:  structures/7urv.pdb
Output: results/sasa_analysis.json, prints burial table

How to run:
    cd computational_validation/
    python3 scripts/02_sasa_burial_analysis.py

Dependencies: freesasa, BioPython
Install:      pip install freesasa biopython
"""
import freesasa
import json
import os
from Bio.PDB import PDBParser, PDBIO, Select

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDB_COMPLEX = os.path.join(BASEDIR, 'structures', '7urv.pdb')
RESULTS_DIR = os.path.join(BASEDIR, 'results')

class ChainSelect(Select):
    def __init__(self, chain_id):
        self.chain_id = chain_id
    def accept_chain(self, chain):
        return chain.id == self.chain_id

def extract_chains():
    """Extract individual chains from the complex PDB."""
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure('7URV', PDB_COMPLEX)
    io = PDBIO()
    chain_files = {}
    for chain_id in ['C', 'D']:
        outfile = PDB_COMPLEX.replace('.pdb', f'_chain{chain_id}.pdb')
        io.set_structure(struct)
        io.save(outfile, ChainSelect(chain_id))
        chain_files[chain_id] = outfile
    return chain_files

def calculate_sasa(pdb_path):
    """Calculate per-residue SASA using FreeSASA."""
    structure = freesasa.Structure(pdb_path)
    result = freesasa.calc(structure)
    return result.residueAreas()

def main():
    chain_files = extract_chains()

    areas_complex = calculate_sasa(PDB_COMPLEX)
    areas_d = calculate_sasa(chain_files['D'])
    areas_c = calculate_sasa(chain_files['C'])

    parser = PDBParser(QUIET=True)
    struct = parser.get_structure('7URV', PDB_COMPLEX)

    target_residues = [70, 214, 260, 261]

    print("=" * 75)
    print("INTERFACE BURIAL ANALYSIS (dSASA)")
    print("dSASA = SASA(isolated) - SASA(complex) = area buried upon binding")
    print("=" * 75)

    # FMC63 (Chain D)
    print(f"\n{'Residue':>12s} {'Complex':>10s} {'Isolated':>10s} {'dSASA':>8s} {'%Buried':>8s}  Notes")
    print("-" * 75)

    burial_data = []
    for resnum_str in sorted(areas_complex.get('D', {}).keys(), key=lambda x: int(x)):
        resnum = int(resnum_str)
        sasa_c = areas_complex['D'][resnum_str].total
        if resnum_str not in areas_d.get('D', {}):
            continue
        sasa_i = areas_d['D'][resnum_str].total
        dsasa = sasa_i - sasa_c
        pct = (dsasa / sasa_i * 100) if sasa_i > 0 else 0

        if dsasa > 5:
            try:
                resname = struct[0]['D'][(' ', resnum, ' ')].get_resname()
            except:
                resname = "???"
            mark = " *** TARGET" if resnum in target_residues else ""
            print(f"  {resname:>4s} {resnum:4d}  {sasa_c:8.1f}   {sasa_i:8.1f}  {dsasa:7.1f}   {pct:5.1f}%{mark}")
            burial_data.append({
                'resname': resname, 'resnum': resnum,
                'sasa_complex': round(sasa_c, 2), 'sasa_isolated': round(sasa_i, 2),
                'dsasa': round(dsasa, 2), 'pct_buried': round(pct, 1),
                'is_target': resnum in target_residues
            })

    total = sum(d['dsasa'] for d in burial_data)
    target_total = sum(d['dsasa'] for d in burial_data if d['is_target'])
    print(f"\nTotal FMC63 interface: {total:.1f} Å²")
    print(f"Target residues: {target_total:.1f} Å² ({target_total/total*100:.1f}%)")

    # CD19 (Chain C)
    cd19_burial = []
    for resnum_str in sorted(areas_complex.get('C', {}).keys(), key=lambda x: int(x)):
        resnum = int(resnum_str)
        sasa_c_val = areas_complex['C'][resnum_str].total
        if resnum_str not in areas_c.get('C', {}):
            continue
        sasa_i_val = areas_c['C'][resnum_str].total
        dsasa = sasa_i_val - sasa_c_val
        if dsasa > 5:
            try:
                resname = struct[0]['C'][(' ', resnum, ' ')].get_resname()
            except:
                resname = "???"
            cd19_burial.append({'resname': resname, 'resnum': resnum, 'dsasa': round(dsasa, 2)})

    # Save
    output = {'fmc63_burial': burial_data, 'cd19_burial': cd19_burial}
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, 'sasa_analysis.json'), 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to results/sasa_analysis.json")

if __name__ == '__main__':
    main()

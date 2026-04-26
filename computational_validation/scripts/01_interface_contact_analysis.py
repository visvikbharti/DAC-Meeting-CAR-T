#!/usr/bin/env python3
"""
Script 01: Interface Contact Analysis of FMC63-CD19 Complex (PDB 7URV)

Purpose: Identify all residue-residue contacts at the FMC63 (chain D) — CD19 (chain C)
         interface and map hydrogen bonds.

Input:  structures/7urv.pdb
Output: Prints contact table, H-bond inventory, and detailed target residue contacts

How to run:
    cd computational_validation/
    python3 scripts/01_interface_contact_analysis.py

Dependencies: BioPython (Bio.PDB), numpy
"""
from Bio.PDB import PDBParser, NeighborSearch
import numpy as np
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDB_FILE = os.path.join(BASEDIR, 'structures', '7urv.pdb')

def main():
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('7URV', PDB_FILE)
    model = structure[0]
    chain_c = model['C']  # CD19
    chain_d = model['D']  # FMC63 scFv

    # --- Chain information ---
    print("=" * 70)
    print("CHAIN INFORMATION — PDB 7URV")
    print("=" * 70)
    for chain in model:
        residues = [r for r in chain if r.id[0] == ' ']
        print(f"Chain {chain.id}: {len(residues)} residues "
              f"(range {residues[0].id[1]}-{residues[-1].id[1]})")

    # --- Interface contacts ---
    print("\n" + "=" * 70)
    print("INTERFACE CONTACTS (< 4.5 Å cutoff)")
    print("=" * 70)

    chain_c_atoms = list(chain_c.get_atoms())
    chain_d_atoms = list(chain_d.get_atoms())
    ns = NeighborSearch(chain_c_atoms)

    interface_d = {}
    interface_c = {}
    contact_distances = {}

    for atom_d in chain_d_atoms:
        close = ns.search(atom_d.get_vector().get_array(), 4.5)
        for atom_c in close:
            res_d = atom_d.get_parent()
            res_c = atom_c.get_parent()
            if res_d.id[0] != ' ' or res_c.id[0] != ' ':
                continue
            key_d = (res_d.get_resname(), res_d.id[1])
            key_c = (res_c.get_resname(), res_c.id[1])

            if key_d not in interface_d:
                interface_d[key_d] = set()
            interface_d[key_d].add(key_c)

            if key_c not in interface_c:
                interface_c[key_c] = set()
            interface_c[key_c].add(key_d)

            pair = (key_d, key_c)
            dist = np.linalg.norm(
                atom_d.get_vector().get_array() - atom_c.get_vector().get_array()
            )
            if pair not in contact_distances or dist < contact_distances[pair]:
                contact_distances[pair] = dist

    target_residues = [70, 214, 260, 261]

    print(f"\nFMC63 (Chain D) interface residues: {len(interface_d)}")
    print(f"{'Residue':>12s}  {'# CD19 Contacts':>15s}  Notes")
    print("-" * 50)
    for (name, num), contacts in sorted(interface_d.items(), key=lambda x: -len(x[1])):
        mark = " *** TARGET" if num in target_residues else ""
        print(f"  {name:>4s} {num:4d}       {len(contacts):2d}{mark}")

    print(f"\nCD19 (Chain C) interface residues: {len(interface_c)}")
    for (name, num), contacts in sorted(interface_c.items(), key=lambda x: -len(x[1])):
        print(f"  {name:>4s} {num:4d}       {len(contacts):2d}")

    # --- Detailed target residue contacts ---
    print("\n" + "=" * 70)
    print("DETAILED CONTACTS FOR TARGET RESIDUES")
    print("=" * 70)
    for resnum in target_residues:
        key_matches = [(k, v) for k, v in interface_d.items() if k[1] == resnum]
        if key_matches:
            (name, num), contacts = key_matches[0]
            print(f"\n{name} {num} (FMC63) → CD19:")
            for cname, cnum in sorted(contacts, key=lambda x: x[1]):
                d = contact_distances.get(((name, num), (cname, cnum)), 999)
                print(f"    → {cname} {cnum:4d}  min distance: {d:.2f} Å")

    # --- Hydrogen bonds ---
    print("\n" + "=" * 70)
    print("POTENTIAL HYDROGEN BONDS (N/O atoms, 2.0-3.5 Å)")
    print("=" * 70)
    hbond_count = 0
    for atom_d in chain_d_atoms:
        if atom_d.element not in ('N', 'O'):
            continue
        close = ns.search(atom_d.get_vector().get_array(), 3.5)
        for atom_c in close:
            if atom_c.element not in ('N', 'O'):
                continue
            res_d = atom_d.get_parent()
            res_c = atom_c.get_parent()
            if res_d.id[0] != ' ' or res_c.id[0] != ' ':
                continue
            dist = np.linalg.norm(
                atom_d.get_vector().get_array() - atom_c.get_vector().get_array()
            )
            if 2.0 < dist < 3.5:
                mark = " ***" if res_d.id[1] in target_residues else ""
                print(f"  {res_d.get_resname()}{res_d.id[1]:4d}.{atom_d.name:4s} — "
                      f"{res_c.get_resname()}{res_c.id[1]:4d}.{atom_c.name:4s}  "
                      f"dist={dist:.2f} Å{mark}")
                hbond_count += 1
    print(f"\nTotal potential H-bonds: {hbond_count}")

if __name__ == '__main__':
    main()

# Secret Sharing Schemes in Cryptography (Python)
Overview
This project implements **Shamir’s Secret Sharing Scheme** and **Additive Secret Sharing** in Python.

It demonstrates how a secret can be divided into multiple shares and reconstructed only when a minimum threshold is met.

## Features
- Shamir’s Secret Sharing (threshold scheme)
- Finite field arithmetic (mod prime)
- Lagrange interpolation for reconstruction
- Additive secret sharing implementation
- Security comparison of both schemes

## Example Output
Shamir Secret Sharing:
- Shares generated for n participants
- Secret successfully reconstructed using t shares
- Reconstruction fails with fewer than t shares

Additive Secret Sharing:
- Secret reconstructed using all shares

## How to Run

```bash
python3 shamir_lab.py
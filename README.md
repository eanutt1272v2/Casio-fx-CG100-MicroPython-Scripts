# Casio fx-CG100 MicroPython Scripts

A scientific and mathematical library of MicroPython scripts for the Casio fx-CG100 Graphing Calculator.

## Overview

This repository contains a library of standalone educational and utility scripts designed for GCSE and A-level mathematics, science, and visualisation (though some are extra!).

Most scripts are interactive:

- they ask for parameters with default values
- they print or draw a result
- they pause before exit so the final output stays visible

The codebase is organised semantically by topic so related scripts live together.

## Repository Structure

| Folder | Scripts | Theme | Example scripts |
|---|---:|---|---|
| `fractals_chaos/` | 8 | Fractals and chaotic systems | `mandelbrot_set.py`, `julia_set.py`, `burning_ship.py` |
| `number_theory/` | 16 | Primes, modular arithmetic, integer functions | `prime_sieve_eratosthenes.py`, `chinese_remainder.py` |
| `geometry_visual/` | 8 | Geometry calculators and curve visualization | `shapes.py`, `triangle_trig_solver.py`, `lissajous_curves.py` |
| `calculus_numerical/` | 7 | Calculus and numerical methods | `newton_raphson.py`, `numerical_integration.py` |
| `physics/` | 7 | Classical physics models | `projectile_motion.py`, `simple_harmonic_motion.py` |
| `probability_statistics/` | 4 | Random processes and distributions | `dice_roll_distribution.py`, `monte_carlo_pi.py` |
| `cellular_automata/` | 3 | Cellular and agent automata | `conway_gol.py`, `langton_ant.py` |
| `sequences_series/` | 3 | Integer sequences and series | `collatz_sequence.py`, `fibonacci_golden_ratio.py` |
| `cryptography/` | 2 | Classical ciphers | `caesar_cipher.py`, `cipher_vigenere.py` |
| `chemistry/` | 1 | Chemistry utility calculator | `chemistry_molar.py` |
| `signal_processing/` | 1 | Fourier/audio synthesis | `fourier_synth.py` |
| `algorithms_visual/` | 1 | Algorithm visualization | `sorting_visual.py` |

## Requirements

### On calculator

- Casio fx-CG100 with MicroPython support (ideally latest official OS)
- Copy the desired script(s) to the calculator storage

## Setup and Run on Physical Calculator (fx-CG100)

### 1. One-time setup

- Ensure your calculator firmware and Python/MicroPython app are installed, functioning correctly, and up to date.
- Connect the calculator to your computer over USB.
- Select the calculator file-transfer/storage mode so files are visible from your computer as a volume.

### 2. Pick a compatible script

- All scripts in this repository are compatible with the fx-CG100 calculator.
- Pick scripts by topic and expected runtime as fractals and dense simulations can take longer to render.
- For fastest on-device testing, start with default parameters and then increase complexity.

### 3. Transfer files

- Copy the selected `.py` file from this repository to calculator storage.
- Scripts in this repository are standalone, so you typically only need one file at a time.
- Keep a backup copy of your calculator storage before large file updates.

### 4. Run on calculator

- Open the Python app on the calculator.
- Browse to the transferred script.
- Run it and follow the on-screen input prompts.
- Most scripts pause before exit so final output remains visible.

### 5. Troubleshooting

- `Module not found`: The script likely uses a desktop-only package. Choose a `casioplot`-based script instead.
- Slow render or timeout: Reduce grid size, iteration count, or other heavy numeric parameters.
- Input/value errors: Re-run and provide values within the prompt ranges shown by the script.

### On desktop (for testing)

- Python 3.13+
- `casioplot` package

## Running Scripts

From the repository root:

```bash
python3 fractals_chaos/mandelbrot_set.py
python3 geometry_visual/shapes.py
python3 number_theory/prime_sieve_eratosthenes.py
```

If using a virtual environment:

```bash
./casio_env/bin/python geometry_visual/shapes.py
```

## Note

- These scripts are educational tools, not production scientific software.

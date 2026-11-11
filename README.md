# Bit-Detection

Can large language models tell when "random" data isn't random?

This project generates pseudo-random bit streams with controlled, subtle biases, encodes them as hex, and gives them to LLMs (ChatGPT, Gemini, Claude) to see whether they detect the irregularities. The full write-up is in [`bit_detection.pdf`](bit_detection.pdf).

**Authors:** Royce Nogales (roycen1@umbc.edu), Sina Roomi (sinar1@umbc.edu)

## Installation

Requirements: Python ≥ 3.13 and [uv](https://docs.astral.sh/uv/).

```bash
# Install uv (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up the project
git clone <repo-url> && cd bit-detection
uv sync
source .venv/bin/activate
uv pip install -e .
```

## Usage

```bash
bd
```

This runs `src/bit_detection/main.py`, which writes ten test files (`file0.txt`–`file9.txt`) of 2²⁰ bits each to `files/tests/`. Each file contains a single hex-encoded bit stream. The RNG is seeded (`seed(1)`), so output is reproducible.

To generate other sizes or output directories, edit `start()` in `main.py` and call `bit_create_tests(size, directory_name)`.

## Test Files

File 0 is an unbiased control. In every other file, the bits (or bytes) at the selected positions are forced to the target value with the given probability. All other bits are random.

| File | Biased positions | Target | Probability |
|------|------------------|--------|-------------|
| 0 | none (control) | — | — |
| 1 | every 3rd bit | 0 | 0.60 |
| 2 | every 3rd bit | 0 | 0.55 |
| 3 | every 2nd, 4th, 6th, 8th bit | 1 | 0.80 |
| 4 | every 3rd, 5th, 7th, 9th bit | 1 | 0.80 |
| 5 | every 2nd, 4th, 6th, 8th bit | 1 | 0.55 |
| 6 | every 3rd, 5th, 7th, 9th bit | 1 | 0.55 |
| 7 | every 3rd byte | all bits → 0 | 0.55 |
| 8 | every 2nd, 4th, 6th, 8th byte | alternating 0/1 | 0.55 |
| 9 | every 1st, 3rd, 5th, 7th byte | alternating 0/1 | 0.55 |

### Included datasets

| Directory | Stream size | Notes |
|-----------|-------------|-------|
| `files/test1/` | 2¹⁰ bits | |
| `files/test5/` | 2¹⁵ bits | `file1.txt` is a one-off: every 10th bit biased toward 0 at 0.51 |
| `files/tests/` | 2²⁰ bits | Default output of `bd` |

## Methodology

Each LLM received all ten files with one of two prompts.

**Open-ended detection**

> For each file, convert the hex to binary, then determine whether the data is random or not random. If it is not random, determine if there are any patterns/biases in the data in each file.

**Chi-squared test**

> For each file, convert the hex to binary, then perform a chi squared test. Only use the results of the chi squared tests to determine whether the data is random or not random.

Links to the model responses are in [`results/RESULTS.md`](results/RESULTS.md) and [`results/RESULTS_CHI.md`](results/RESULTS_CHI.md).

## Project Structure

```
bit-detection/
├── bit_detection.pdf          # Paper
├── files/                     # Generated test data
├── results/                   # Prompts and LLM responses
├── font/                      # Font used by the image generator
└── src/bit_detection/
    ├── main.py                # Entry point (`bd`); defines tests 0–9
    ├── bit_create.py          # Biased bit-stream generation
    └── imagine_gen.py         # Experimental image noise/steganography (unused)
```

## License

Released under the [MIT License](LICENSE).

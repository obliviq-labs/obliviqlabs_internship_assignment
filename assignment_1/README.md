# Assignment 1 — Debug a Robot Sensor Analysis Pipeline

## Theme

Python, debugging, sensor data, and engineering reasoning.

This assignment is designed for candidates who are comfortable with programming
and figuring things out, even if they have limited robotics experience.

## Scenario

You have been given a partially implemented program for analysing sensor readings
from a mobile robot. The program currently produces incorrect results and may fail
in some situations.

Your task is to understand the data, debug the program, and extend it with a small
useful feature.

## Dataset

The repository contains `data/move.data`, taken from the **UCI Pioneer-1 Mobile
Robot Data** dataset:

https://archive.ics.uci.edu/dataset/135/pioneer+1+mobile+robot+data

The file contains time-series observations from a Pioneer-1 mobile robot moving
in a straight line during different trials. Each row belongs to one trial and
contains the trial description, timestamp, sonar readings, wheel velocities,
robot velocity, stall sensors, and other measurements. Samples within a trial
were recorded approximately every 100 ms.

Distances and linear velocities are reported in millimetres and millimetres per
second. The original UCI dataset page and documentation are the source of truth
for the file format and sensor meanings.

## Your objective

Understand and repair the pipeline so that the following flow works correctly:

```text
load dataset
      ↓
parse sensor readings
      ↓
analyse robot motion
      ↓
generate visualisations
```

Do not assume that the current implementation or its outputs are correct.

### 1. Get the existing program working correctly

Inspect the code and data, identify problems, and make the program produce
trustworthy results. Preserve the command-line workflow described below.

### 2. Produce three plots

Generate clear plots for:

- Time versus forward sonar distance
- Time versus left and right wheel velocity
- Time versus robot translational velocity

The dataset contains multiple independent trials. Choose and document a sensible
way to present them—for example, plotting one selected trial or creating separate
outputs per trial. Axes, units, legends, and titles should be clear.

### 3. Detect possible obstacle interactions

Design a simple method that identifies moments when the robot may have encountered
an obstacle. There is not necessarily one correct solution. You may use one or
more signals such as sonar distance, stall sensors, or a sudden velocity change.

Your program should save the detected events to a machine-readable file such as
CSV and print a short summary to the terminal. Explain your method and justify
your thresholds or assumptions.

### 4. Add one analysis of your own

Add one useful analysis beyond the required plots and obstacle detector. Possible
directions include:

- Comparing left and right sonar measurements
- Identifying stationary periods
- Detecting turns or wheel imbalance
- Finding the nearest encountered obstacle
- Summarising individual trials

Choose something you find interesting and explain what it reveals.

### 5. Explain your work

Update this README, or add a clearly linked report, covering:

- Problems found
- Why they occurred
- How you fixed them
- Assumptions made
- Your obstacle-interaction method
- Your additional analysis and its result
- One thing you would improve with more time

## Setup

Python 3.10 or newer is recommended. No dedicated GPU is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the starter program

From the repository root, run:

```bash
python src/analyze.py
```

The final submission must remain reproducible with this command. You may use a
Jupyter notebook for exploration, but the notebook must not be required to obtain
the final results.

By default, the starter program reads `data/move.data`, selects one trial, prints
a short summary, and writes figures and analysis files under `outputs/`.

Useful command-line options:

```bash
python src/analyze.py --help
python src/analyze.py --trial MOVE-TRIALT148
python src/analyze.py --output-dir outputs
```

## Expected submission

Submit a Git repository or ZIP containing:

- Your corrected and extended source code
- All three required plots
- A CSV or similar file containing detected obstacle events
- Your additional analysis and its output
- Updated documentation explaining your reasoning
- A sensible Git commit history, if submitting a repository

Do not commit a virtual environment or generated cache files.

## Evaluation

We will evaluate:

- How systematically you understand and debug unfamiliar code
- Correctness of data handling and time-series reasoning
- Clarity and maintainability of your Python code
- Quality and readability of visualisations
- Reasoning behind obstacle-event detection
- Reproducibility from the command line
- Quality of your written explanation and assumptions

We care more about clear reasoning and a reliable solution than about sophisticated
machine learning. No machine-learning model is required.

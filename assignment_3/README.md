# Assignment 3 — Teach a Robot How to React to Sensors

## Theme

**Machine learning + data + experimentation**

## Background

A mobile robot has distance sensors around it. Based on these readings, it must decide how to move.

Your goal is to build a small machine-learning system that predicts the robot's movement from four sensor readings, evaluate it, and investigate when it fails. Prior robotics experience is not required. This assignment is designed to run on a normal CPU-based computer; no dedicated GPU is needed.

## Dataset

Use the supplied file:

```text
data/sensor_readings_4.data
```

It contains measurements recorded from a SCITOS G5 mobile robot while it followed a wall. Each row contains five comma-separated values and the file has no header row:

| Column | Meaning |
| --- | --- |
| 1 | Minimum front sensor distance (`front`) |
| 2 | Minimum left sensor distance (`left`) |
| 3 | Minimum right sensor distance (`right`) |
| 4 | Minimum back sensor distance (`back`) |
| 5 | Movement selected by the robot (`action`) |

The four possible actions are:

- `Move-Forward`
- `Slight-Right-Turn`
- `Sharp-Right-Turn`
- `Slight-Left-Turn`

The sensor readings are real-valued distances. The source does not specify a unit, so do not assume one in your analysis. For this assignment, treat each row as one supervised classification example.

### Dataset attribution

- **Dataset:** [Wall-Following Robot Navigation Data](https://archive.ics.uci.edu/dataset/194/wall+following+robot+navigation+data)
- **Creators:** Ananda Freire, Marcus Veloso, and Guilherme Barreto (2009)
- **Repository:** UCI Machine Learning Repository
- **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **DOI:** [10.24432/C57C8W](https://doi.org/10.24432/C57C8W)

## Your task

### Part 1 — Understand the data

Load and inspect the dataset. In your report, answer:

1. How many samples are present?
2. How many input features are present?
3. What are the possible robot actions?
4. Do the different actions occur equally often?
5. Are there missing, extreme, duplicated, or otherwise unusual sensor values?

Explain anything important you notice rather than only printing library output.

### Part 2 — Visualize the data

Create at least **two useful plots** that help you understand the robot's observations or decisions.

Choose the plots yourself. Possibilities include a class distribution, a sensor-value distribution, a comparison between two sensors, or sensor values grouped by action. Add a short explanation of what each plot reveals.

### Part 3 — Build a prediction model

Train a simple machine-learning model that predicts `action` from the four sensor readings.

You may use any method you think is appropriate. Examples include a decision tree, random forest, logistic regression, or k-nearest neighbours. A neural network is not required. Briefly explain why you selected your model and describe any preprocessing you applied.

### Part 4 — Evaluate the model

Use a train/test split so the model is evaluated on examples it did not train on. Report:

- Test accuracy
- Confusion matrix
- At least one observation about which actions are easy or difficult to predict

Use a fixed random seed where applicable so another person can reproduce your result. Take care to avoid accidental leakage between training and test data.

### Part 5 — Investigate failures

Find at least **five test examples** for which the model predicted the wrong action.

For each example, show:

- The four sensor readings
- The correct action
- The predicted action
- Your explanation of why the model may have been confused

There may not be one provably correct explanation. We are interested in the quality of your reasoning and the patterns you identify. You may use one of these observations to motivate the experiment in Part 6.

### Part 6 — Run one experiment of your own

Based on something you observed in the data or in the model's failures, form one small hypothesis and run an experiment to test it.

In your report, explain:

- What you observed and what you expected to happen
- What you changed and why that tests your hypothesis
- What happened, using an appropriate measurement or comparison
- What you concluded, including whether the result supported your hypothesis

Keep the experiment focused. We are interested in how you turn an observation into a test and reason about the result, not in an exhaustive model search.

## Bonus — Compare against explicit rules

Create a small hand-written rule-based controller and compare it with your machine-learning model on the same test data.

For example, a rule might inspect whether the front distance is below a chosen threshold before deciding to turn. Design your own rules, explain how you selected any thresholds, and discuss when explicit rules may be preferable to a learned controller—and when they may not be.

The bonus is optional. A careful core submission is more valuable than an unfinished bonus.

## Allowed tools

Recommended tools are:

- Python 3.10 or newer
- NumPy
- pandas
- Matplotlib or Seaborn
- scikit-learn

Other lightweight, CPU-compatible tools are allowed. Do not use paid services or GPU-only libraries.

## Setup

Create and activate a virtual environment, then install the suggested packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

A typical way to load the file is shown below. This is only a loading example, not a solution:

```python
import pandas as pd

columns = ["front", "left", "right", "back", "action"]
data = pd.read_csv("data/sensor_readings_4.data", names=columns)
```

## What to submit

Submit a GitHub repository or a ZIP file containing:

```text
your_submission/
├── README.md                 # How to run your work and a short result summary
├── requirements.txt         # Or an equivalent environment file
├── src/                     # Python scripts, if used
├── notebook.ipynb           # Optional; a notebook is also acceptable
├── report.md or report.pdf  # Analysis, plots, results, failures, and experiment
└── outputs/                 # Generated plots or other relevant outputs
```

Your work should run from a fresh environment using the instructions you provide. Do not commit a virtual environment, cached packages, or large unrelated files.

## What we will look for

- Correct, readable, and reproducible code
- Thoughtful exploration rather than a large number of plots
- A sensible modeling and evaluation process
- Careful analysis of wrong predictions
- A clear hypothesis and a focused experiment that tests it
- Clear written communication
- Independent engineering judgment

The highest score does not necessarily go to the most complex model. A simple model with well-reasoned experiments and strong failure analysis is an excellent submission.

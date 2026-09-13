# Assignment 2 — Build a Tiny Physics Simulator

## Theme

**Math, physics intuition, Python, debugging, and learning something unfamiliar**

## Objective

A ball was observed moving through a simple 2D environment. Its measured trajectory is provided in `data/ball_trajectory.csv`.

Build a small physics simulator that approximately reproduces the observed motion. Do not use a physics engine or machine-learning model.

The goal is not to produce a perfect fit. We want to understand how you approach an unfamiliar technical problem, translate equations into code, compare a model with observations, and reason about mismatch.

This assignment is designed to run on a normal CPU-only computer.

## Dataset

The CSV contains 400 observations sampled at approximately 50 Hz:

| Column | Meaning | Unit |
|---|---|---|
| `time` | Time since recording began | seconds |
| `x` | Measured horizontal position | metres |
| `y` | Measured vertical position | metres |

The ground is approximately at `y = 0`. The values represent measurements, so expect a small amount of noise. A measured point may occasionally lie slightly below zero even though the physical ball cannot pass through the ground.

## Background

Ignoring air resistance, a simple discrete-time model of a projectile is:

```text
v_y(t + dt) = v_y(t) - g * dt
x(t + dt)   = x(t) + v_x(t) * dt
y(t + dt)   = y(t) + v_y(t) * dt
```

where:

- `x`, `y` are position;
- `v_x`, `v_y` are horizontal and vertical velocity;
- `g` is gravitational acceleration; and
- `dt` is the simulation time step.

You may change the order of the velocity and position updates if you believe another numerical integration scheme is more suitable. Explain your choice briefly.

### Coefficient of restitution

When the ball reaches the ground while travelling downward, make it bounce by reversing and reducing its vertical velocity:

```text
v_y_after = -e * v_y_before
```

`e` is the coefficient of restitution:

- `e = 0`: no bounce;
- `e = 1`: perfectly elastic bounce with no vertical impact-energy loss;
- `0 < e < 1`: the ball bounces but loses energy at impact.

In code, a basic collision condition might begin with `y <= 0`. Your implementation should also prevent the simulated ball from continuing below the ground.

## Required work

### Part 1 — Load and inspect the data

- Load `data/ball_trajectory.csv`.
- Check its columns, units, sample count, and sampling interval.
- Plot or otherwise inspect the measured motion before choosing parameters.

### Part 2 — Build the simulator

Implement a 2D ball simulator using Python and NumPy. It must include:

- initial position;
- initial horizontal and vertical velocity;
- gravity;
- a configurable time step; and
- a sequence of simulated `time`, `x`, and `y` values.

Do not use MuJoCo, Isaac Sim, PyBullet, Box2D, or another physics engine.

### Part 3 — Add ground collision and bouncing

- Detect contact with the ground.
- Prevent persistent ground penetration.
- Apply the coefficient-of-restitution rule to downward impact velocity.
- Ensure that successive bounces lose energy when `e < 1`.

### Part 4 — Compare simulation with observations

Create clear plots comparing the measured and simulated trajectories. Include at least:

1. vertical position `y` versus time; and
2. the 2D path `y` versus `x`.

Use labels, units, legends, and a readable figure size. You may add other plots or numerical error measures if they help your analysis.

### Part 5 — Choose a reasonable bounce parameter

Try different values of `e` between 0 and 1 and identify a value that produces reasonably similar bounce behaviour. Manual trial and error is acceptable. Explain how you chose your final value.

### Part 6 — Explain the mismatch

Your simulation will probably not reproduce every measured point. Give at least three plausible reasons for the difference between the recorded and simulated trajectories. Support your explanation with evidence from your plots or experiments where possible.

Examples of factors worth thinking about include measurement uncertainty, initial-condition estimates, time discretization, omitted forces, and the simplicity of the collision model. These are prompts for investigation, not a required answer list.

## Allowed tools

- Python 3
- NumPy
- Matplotlib
- pandas (optional)
- Jupyter Notebook (optional)

No dedicated GPU is needed. Do not use a physics engine, machine-learning model, or parameter-fitting library that solves the whole task for you.

## Submission

Submit a Git repository or ZIP archive containing:

- your runnable Python script(s) or notebook;
- a short `README.md` with run instructions;
- the comparison plot(s), either saved as images or generated when the code runs;
- your chosen parameter values, including `e`; and
- a brief explanation of your approach, observations, and at least three mismatch causes.

A reviewer should be able to install the small set of dependencies and reproduce your result with a clearly documented command or notebook workflow.

## What we evaluate

- correctness and clarity of the physics implementation;
- handling of collision edge cases and numerical issues;
- quality of the observed-versus-simulated comparison;
- reasoning behind parameter choices;
- debugging and investigation process;
- code readability and reproducibility; and
- clarity and honesty of the written explanation.

We care more about thoughtful reasoning and a reliable, understandable solution than about achieving an artificially tiny error.

## Notes

- Do not search for or assume hidden generating parameters.
- Reasonable engineering assumptions are welcome—state them clearly.
- Keep the solution focused; a user interface is not required.
- If something in the data surprises you, investigate it and explain what you found.

# Obliviq Labs — Internship Technical Assignment

Welcome to the **Obliviq Labs Internship Technical Assignment**.

If you are here, you are probably interested in working on hard problems around robotics, simulation, Physical AI, machine learning, or engineering systems.

You are **not expected to already know all of these areas**.

What we care about much more is whether you can:

* learn unfamiliar concepts quickly;
* debug problems systematically;
* build things independently;
* work through problems that do not have a perfect tutorial;
* reason clearly about your engineering decisions;
* write understandable Python code; and
* explain what worked, what failed, and what you learned.

---

## About Obliviq Labs

**Obliviq Labs** is an early-stage robotics and Physical AI company working toward infrastructure that helps robots learn and improve through simulation.

At a high level, we are interested in the complete **Real2Sim2Real** loop:

```text
Real-world observations
        ↓
Understanding the environment
        ↓
Building useful simulations / digital twins
        ↓
Generating robot experience and data
        ↓
Training robot policies
        ↓
Evaluating failures
        ↓
Improving the system
        ↓
Real-world deployment
```

Our long-term goal is to make it easier to go from:

```text
robot + task definition
        ↓
simulation
        ↓
training data
        ↓
robot policy
        ↓
validated behaviour
```

without every robotics team having to manually build the entire pipeline from scratch.

These assignments do **not** expect you to already know how to build this system.

Instead, each assignment tests some of the fundamental abilities that are useful when working toward problems like these.

---

# Choose ONE Assignment

There are three assignments in this repository.

You should complete **only one**.

Choose the assignment that genuinely interests you the most or best matches the kind of problems you would like to work on.

Completing multiple assignments does **not** give you an advantage.

---

## Assignment 1 — Debug a Robot Sensor Analysis Pipeline

**Best suited for:** people who enjoy programming, debugging, understanding unfamiliar code, and working with data.

You will work with real sensor data collected from a mobile robot.

Your job is to understand an existing partially implemented codebase, identify problems, fix them, analyse robot behaviour, and add a small feature of your own.

```text
assignment_1/
```

This track primarily tests:

* Python fundamentals
* debugging
* code reading
* data handling
* engineering reasoning
* independent investigation

Prior robotics knowledge is **not required**.

---

## Assignment 2 — Build a Tiny Physics Simulator

**Best suited for:** people interested in physics, mathematics, simulation, robotics, mechanical systems, or numerical programming.

You will receive the measured trajectory of a bouncing ball.

Your task is to build a small physics simulator that approximately reproduces the observed motion and investigate why simulation and observation may differ.

```text
assignment_2/
```

This track primarily tests:

* basic physics intuition
* translating equations into code
* numerical reasoning
* experimentation
* debugging
* learning unfamiliar concepts

Prior simulation-engine experience is **not required**.

You do not need MuJoCo, Isaac Sim, PyBullet, or any other physics engine.

---

## Assignment 3 — Teach a Robot How to React to Sensors

**Best suited for:** people interested in machine learning, data science, AI, robotics, or experimentation.

You will work with sensor readings recorded from a real mobile robot and build a lightweight machine-learning model that predicts how the robot should move.

```text
assignment_3/
```

This track primarily tests:

* data understanding
* basic machine learning
* experimentation
* model evaluation
* failure analysis
* engineering judgement

You do not need deep-learning or robotics experience.

---

# Compute Requirements

All assignments are intentionally designed to run on a **normal CPU-based laptop or desktop**.

A dedicated GPU is **not required**.

You should not need:

* CUDA
* high-end GPUs
* cloud GPU instances
* Isaac Sim
* large neural networks
* VLA models
* expensive paid services

A typical computer with Python and approximately 8 GB RAM should be sufficient.

---

# Using AI Tools

You are allowed to use:

* ChatGPT
* Claude
* GitHub Copilot
* documentation
* Google/Search
* Stack Overflow
* tutorials
* any other reasonable learning resource

We are not testing whether you can work without modern tools.

We are testing whether you can **use those tools while still understanding what you build**.

You should therefore be prepared to explain any part of your submission during a follow-up technical discussion.

If you cannot explain why your own code works, that will significantly affect the evaluation.

---

# Submission Deadline

You have **7 days from the day you receive this assignment** to submit your work.

You do not need to use the entire seven days.

### Execution speed is part of the signal we evaluate.

At an early-stage company, being able to understand a problem, learn what is necessary, make decisions, and produce a working result quickly is valuable.

For that reason, **a strong submission completed substantially before the deadline will be viewed positively during the final evaluation**.

However:

> **Do not sacrifice quality simply to submit early.**

A rushed submission with weak reasoning will not score better than a thoughtful and technically solid submission.

The strongest signal is:

```text
good engineering
      +
clear reasoning
      +
independent execution
      +
fast iteration
```

If you can produce high-quality work quickly, we want to see that.

---

# What You Should Submit

Your submission should contain:

```text
your_submission/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── your code
│
├── outputs/
│   └── plots / results
│
└── report.md or equivalent
```

Exact structure may vary depending on the assignment.

The individual assignment README contains the detailed requirements.

---

# Private Repository Requirement

**Do not publish your solution in a public GitHub repository.**

These assignments are used for evaluating multiple candidates, so publicly available solutions reduce the usefulness of the evaluation process.

Create a **private GitHub repository** for your solution.

Please:

1. Create a new private GitHub repository.
2. Push your complete solution to it.
3. Keep a sensible Git commit history where possible.
4. Give access to the GitHub account:

```text
obliviq-labs
```

5. Send the private repository link with your submission email.

Do not commit:

```text
.venv/
__pycache__/
large unrelated files
downloaded package caches
```

If you are unable to use a private GitHub repository, you may submit a ZIP archive instead.

---

# Video Explanation — Required

Along with your code, submit a **short face-camera video explaining your solution**.

This is required.

Recommended duration:

**3–6 minutes**

Your face should be visible for at least part of the recording.

Screen sharing is encouraged while explaining the implementation.

You do not need professional editing or presentation slides.

A simple screen recording is enough.

Please explain:

### 1. What you built

Briefly describe the problem and your approach.

### 2. Show the solution running

Run your program or show the important outputs.

### 3. Explain one important technical decision

For example:

```text
Why did you choose this algorithm?

Why did you handle the data this way?

Why did you implement the physics like this?

How did you decide a threshold?
```

### 4. Explain one problem you encountered

Tell us:

```text
What went wrong?

How did you investigate it?

How did you fix it?
```

### 5. What would you improve next?

Explain what you would do differently or improve if you continued working on the problem.

---

## Why We Require the Video

The goal is not to evaluate presentation skills or English fluency.

We want to understand **how you think about your own work**.

Clear technical understanding matters much more than polished speaking.

You should be able to explain your solution in your own words.

---

# Submission Email

Send your final submission to:

**[saurabh@obliviqlabs.com](mailto:saurabh@obliviqlabs.com)**

Use the subject:

```text
Obliviq Labs Internship Assignment — <Your Name> — Assignment <1/2/3>
```

Example:

```text
Obliviq Labs Internship Assignment — Rahul Sharma — Assignment 2
```

Include:

```text
Name:
Chosen assignment:
Private GitHub repository:
Video explanation link:
```

You may upload the video as:

* an unlisted YouTube video;
* Google Drive link;
* Loom recording; or
* another accessible private/unlisted link.

Make sure we have permission to view both the repository and the video before submitting.

---

# How Your Work Will Be Evaluated

We are not primarily looking for the most complicated solution.

Across all three tracks, we care about:

| Area                             | Importance |
| -------------------------------- | ---------: |
| Problem understanding            |       High |
| Debugging and problem solving    |  Very High |
| Implementation correctness       |       High |
| Engineering reasoning            |  Very High |
| Experimentation / investigation  |       High |
| Ability to learn independently   |  Very High |
| Code quality and reproducibility |     Medium |
| Communication and explanation    |     Medium |
| Execution speed / initiative     |       High |

A simple solution that you deeply understand is often stronger than a sophisticated solution assembled without understanding.

---

# What We Are Really Looking For

You may encounter something in the assignment that you have never seen before.

That is intentional.

At Obliviq Labs, many problems we work on do not come with:

```text
step-by-step tutorial
+
perfect documentation
+
known solution
```

The ability we care about is:

```text
"I don't know how to do this yet."
               ↓
        investigate
               ↓
          experiment
               ↓
            fail
               ↓
           debug
               ↓
          understand
               ↓
             build
```

If that process sounds enjoyable rather than frustrating, you are probably the kind of person we would like to work with.

---

## Final Checklist

Before sending your submission, verify that:

* [ ] You completed **one** assignment.
* [ ] Your solution runs on CPU.
* [ ] Your repository is **private**.
* [ ] `obliviq-labs` has access to the repository.
* [ ] Your README explains how to run the project.
* [ ] Your required outputs are included.
* [ ] You can reproduce the result from a fresh environment.
* [ ] Your face-camera explanation video is accessible.
* [ ] You understand the code you submitted.
* [ ] Your submission email contains all requested links and information.

---

Good luck.

We are much more interested in **how you approach the problem** than whether you already know everything required to solve it.

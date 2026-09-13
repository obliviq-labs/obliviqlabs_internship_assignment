"""Plotting functions for the robot sensor analysis."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def _finish_figure(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def plot_forward_sonar(data: pd.DataFrame, output_path: Path) -> None:
    plt.figure(figsize=(10, 4))
    plt.plot(data["time_s"], data["sonar_0_mm"], color="tab:blue")
    plt.xlabel("Time (s)")
    plt.ylabel("Forward sonar distance (mm)")
    plt.title("Forward sonar distance over time")
    plt.grid(alpha=0.25)
    _finish_figure(output_path)


def plot_wheel_velocities(data: pd.DataFrame, output_path: Path) -> None:
    plt.figure(figsize=(10, 4))
    plt.plot(
        data["time_s"],
        data["left_wheel_velocity_mm_s"],
        label="Left wheel",
    )
    plt.plot(
        data["time_s"],
        data["right_wheel_velocity_mm_s"],
        label="Right wheel",
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Wheel velocity (mm/s)")
    plt.title("Wheel velocities over time")
    plt.legend()
    plt.grid(alpha=0.25)
    _finish_figure(output_path)


def plot_translational_velocity(data: pd.DataFrame, output_path: Path) -> None:
    plt.figure(figsize=(10, 4))
    plt.plot(
        data["translational_velocity_mm_s"],
        data["time_s"],
        color="tab:green",
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Translational velocity (mm/s)")
    plt.title("Robot translational velocity over time")
    plt.grid(alpha=0.25)
    _finish_figure(output_path)


def create_required_plots(data: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_forward_sonar(data, output_dir / "forward_sonar.png")
    plot_wheel_velocities(data, output_dir / "wheel_velocities.png")
    plot_translational_velocity(
        data, output_dir / "translational_velocity.png"
    )

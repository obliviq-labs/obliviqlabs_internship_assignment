"""Command-line entry point for the Pioneer-1 sensor analysis."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from load_data import load_robot_data
from visualize import create_required_plots


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "move.data"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs"


def detect_obstacle_interactions(data: pd.DataFrame) -> pd.DataFrame:
    """Return rows that may represent an obstacle interaction."""
    return data.iloc[0:0].copy()


def choose_trial(data: pd.DataFrame, requested_trial: str | None) -> pd.DataFrame:
    if requested_trial is None:
        requested_trial = data["trial_id"].iloc[0]

    trial = data[data["trial_id"] == requested_trial].copy()
    if trial.empty:
        available = ", ".join(data["trial_id"].drop_duplicates().head(8))
        raise ValueError(
            f"Unknown trial '{requested_trial}'. Some available trials: {available}"
        )

    return trial.sort_values("time_s", ascending=False).reset_index(drop=True)


def print_summary(data: pd.DataFrame, trial: pd.DataFrame) -> None:
    print(f"Loaded {len(data):,} observations from {data['trial_id'].nunique()} trials")
    print(f"Selected trial: {trial['trial_id'].iloc[0]}")
    print(f"Description: {trial['description'].iloc[0]}")
    print(f"Samples: {len(trial)}")
    print(
        "Forward-sonar range: "
        f"{trial['sonar_3_mm'].min():.1f} to {trial['sonar_3_mm'].max():.1f} mm"
    )
    print(
        "Mean translational velocity: "
        f"{trial['translational_velocity_mm_s'].mean():.1f} mm/s"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyse the UCI Pioneer-1 mobile robot movement data."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA_PATH,
        help="Path to move.data",
    )
    parser.add_argument(
        "--trial",
        type=str,
        default=None,
        help="Trial ID to analyse (defaults to the first trial in the file)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for plots and CSV outputs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_robot_data(args.data)
    trial = choose_trial(data, args.trial)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    print_summary(data, trial)
    create_required_plots(trial, args.output_dir)

    events = detect_obstacle_interactions(trial)
    events.to_csv(args.output_dir / "obstacle_events.csv", index=False)

    print(f"Possible obstacle interactions: {len(events)}")
    print(f"Outputs written to: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()

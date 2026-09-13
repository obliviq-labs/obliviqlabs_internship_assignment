"""Utilities for loading Pioneer-1 mobile robot sensor data."""

from pathlib import Path

import pandas as pd


COLUMNS = [
    "trial_id",
    "description",
    "time_s",
    "battery_v",
    "sonar_0_mm",
    "sonar_1_mm",
    "sonar_2_mm",
    "sonar_3_mm",
    "sonar_4_mm",
    "sonar_5_mm",
    "sonar_6_mm",
    "heading_deg",
    "left_wheel_velocity_mm_s",
    "right_wheel_velocity_mm_s",
    "translational_velocity_mm_s",
    "rotational_velocity_mm_s",
    "right_stall",
    "left_stall",
    "robot_status",
    "gripper_state",
    "gripper_front_beam",
    "gripper_rear_beam",
    "gripper_bumper",
    "vis_a_area_px",
    "vis_a_x_px",
    "vis_a_y_px",
    "vis_a_height_px",
    "vis_a_width_px",
    "vis_a_distance_mm",
    "vis_b_area_px",
    "vis_b_x_px",
    "vis_b_y_px",
    "vis_b_height_px",
    "vis_b_width_px",
    "vis_b_distance_mm",
    "vis_c_area_px",
    "vis_c_x_px",
    "vis_c_y_px",
    "vis_c_height_px",
    "vis_c_width_px",
    "vis_c_distance_mm",
]


def load_robot_data(path: str | Path) -> pd.DataFrame:
    """Load a Pioneer-1 movement data file into a DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    data = pd.read_csv(path, names=COLUMNS, header=None, dtype=str)

    value_columns = COLUMNS[2:]
    data[value_columns] = data[value_columns].apply(
        pd.to_numeric, errors="coerce"
    )

    sonar_columns = [f"sonar_{index}_mm" for index in range(7)]
    data[sonar_columns] = data[sonar_columns].mask(data[sonar_columns] >= 5000, 0)

    return data

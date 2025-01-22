import os
import pandas as pd


def load_gnss_data(base_folder):
    required_columns = ["Lat_GNSS", "Long_GNSS", "Height_GNSS"]

    gnss_data = []

    for trial in sorted(os.listdir(base_folder)):
        trial_path = os.path.join(base_folder, trial)

        if os.path.isdir(trial_path) and trial.startswith("trial"):
            gnss_file_name = "GNSS.csv"
            gnss_file_path = os.path.join(trial_path, gnss_file_name)

            if os.path.exists(gnss_file_path):
                gnss_df = pd.read_csv(gnss_file_path)

                if all(col in gnss_df.columns for col in required_columns):
                    gnss_df = gnss_df[required_columns]  # Select only the required columns
                    gnss_df['Trial'] = trial  # Add a column to identify the trial
                    gnss_data.append(gnss_df)
                else:
                    print(f"Warning: File {gnss_file_name} in {trial} missing required columns.")

    concatenated_gnss_data = pd.concat(gnss_data, ignore_index=True) if gnss_data else None

    return concatenated_gnss_data

def load_data_imu(base_folder, data_type):
    required_columns = [
        "PacketCounter", "SampleTimeFine", "Euler_X", "Euler_Y", "Euler_Z",
        "Acc_X", "Acc_Y", "Acc_Z", "Gyr_X", "Gyr_Y", "Gyr_Z"
    ]
    if data_type not in ['imu', 'imu_radial', 'car']:
        raise ValueError("data_type must be either 'imu', 'imu_radial', or 'car'")

    if data_type in ['imu', 'imu_radial']:
        file_suffix = "" if data_type == "imu" else "_radial"

        data = {f'IMU{i}{file_suffix}': [] for i in range(1, 5)}

        for trial in sorted(os.listdir(base_folder)):
            trial_path = os.path.join(base_folder, trial)

            if os.path.isdir(trial_path) and trial.startswith("trial"):
                for imu_num in range(1, 5):
                    file_name = f"IMU{imu_num}{file_suffix}.csv"
                    file_path = os.path.join(trial_path, file_name)

                    if os.path.exists(file_path):
                        df = pd.read_csv(file_path,skiprows=1)

                        if all(col in df.columns for col in required_columns):
                            df = df[required_columns]  # Select only the required columns
                            # Add a column to identify the trial and IMU
                            df['Trial'] = trial
                            df['IMU'] = f'IMU{imu_num}{file_suffix}'

                            data[f'IMU{imu_num}{file_suffix}'].append(df)
                        else:
                            print(f"Warning: File {file_name} in {trial} missing required columns.")

        concatenated_data = {key: pd.concat(value, ignore_index=True) if value else None
                             for key, value in data.items()}

        return concatenated_data

    elif data_type == 'car':
        car_data = []

        for trial in sorted(os.listdir(base_folder)):
            trial_path = os.path.join(base_folder, trial)

            if os.path.isdir(trial_path) and trial.startswith("trial"):
                car_file_name = "CAR.csv"
                car_file_path = os.path.join(trial_path, car_file_name)

                if os.path.exists(car_file_path):
                    car_df = pd.read_csv(car_file_path,skiprows=1)
                    car_df['Trial'] = trial  # Add a column to identify the trial
                    car_data.append(car_df)

        concatenated_car_data = pd.concat(car_data, ignore_index=True) if car_data else None

        return concatenated_car_data

base_folder = "datasets"
try:
    data_gnss = load_gnss_data(base_folder)
    if data_gnss is not None:
        print(f"GNSS: Loaded {len(data_gnss)} rows with required columns.")
    else:
        print("GNSS: No data found.")
except Exception as e:
    print(e)


data_type='car' #choose data type (imu,imu_radial,car)

try:
    data_imu = load_data_imu(base_folder, data_type)

    if data_type in ['imu', 'imu_radial']:
        for imu, df in data_imu.items():
            if df is not None:
                print(f"{imu}: Loaded {len(df)} rows with required columns.")
            else:
                print(f"{imu}: No data found or missing required columns.")
    elif data_type == 'car':
        if data_imu is not None:
            print(f"CAR: Loaded {len(data_imu)} rows.")
        else:
            print("CAR: No data found.")
except ValueError as e:
    print(e)

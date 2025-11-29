# WID

Here, you can find the dataset and code of the paper <span style="font-family:Arial; font-size:18px;">WID : Wheel Inertial Dataset</span>

## Abstract

<p style="font-family:Verdana; font-size:14px;">
A wheel-mounted inertial sensor mitigates inertial drift more effectively than an inertial sensor mounted on the vehicle chassis. Although their usage is increasing, there is no publicly available dataset for wheel-mounted inertial sensors. To fill this gap, this work presents the wheel-mounted inertial (WMI) dataset. WMI was recorded using two platforms: an omni-directional robot equipped with 5 IMUs, and a passenger car equipped with 9 IMUs. Each platform features IMUs mounted on every wheel. In total  64.04 minutes of recordings for each IMU (490 minutes for all IMUs) were made with associated ground truth trajectory. This versatile dataset will help develop model-based and data-driven approaches with wheel mounted inertial sensors.
</p>

## Sensors Used
**Car**
- Xsens DOTs - a low-cost IMU sensors. Eight used in each experiment to produce the raw data.<br/>
- GNSS-RTK - an accurate positioning solution connected to the MRU-P.

**Mobile Robot**
- STMicroelectronics ASM330LHBG (6-DoF IMU) — one on each wheel, measuring linear acceleration and angular velocity.
- InvenSense MPU9250 (9-DoF IMU) — mounted inside the chassis, combining accelerometer, gyroscope, and magnetometer.
- GNSS-RTK - provides high-accuracy ground-truth positioning (±0.06 m accuracy with NTRIP corrections).
  
## Platforms
- Car - a private Skoda Roomster <br/>
<img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/a27946ca-5b5c-4735-980a-f435ac983ba6" />


- Mobile Robot <br/>
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/3cc76a64-88f1-483a-aceb-3d7ae2bdcc57" />

## Update 

Data and code will be available soon.

If you find the paper, dataset, or code helpful in your research, please cite our paper:

```bibtex
@article{Wheel-Mounted Inertial Datasets,
    author = {Dusan, Nemec and Gal, Versano and Vojtech, Simak and Michal, Gregor and Itai, Savin and Juraj,
Kekelak and Itzik, Klein},
journal = {Scientific Data}, 
year = 2026, 
title = {Wheel-Mounted Inertial Datasets},    
}


# WID

Here, you can find the dataset and code of the paper <span style="font-family:Arial; font-size:18px;">WID : Wheel Inertial Dataset</span>

## Abstract

<p style="font-family:Verdana; font-size:14px;">
A wheel-mounted inertial sensor mitigates inertial drift more effectively than an inertial sensor mounted on the vehicle chassis.
Although their usage is increasing, there is no publicly available dataset for wheel-mounted inertial sensors.
To fill this gap, this work presents the wheeled-mounted inertial (WMI) dataset. WMI was recorded using two platforms: an omni-directional robot equipped with 5 IMUs, and a passenger car equipped with 9 IMUs.
Each platform features IMUs mounted on every wheel. In total 106 minutes of recordings for each IMU (740 minutes for all IMUs) were made with associated ground truth trajectory. 
This versatile dataset will help develop model-based and data-driven approaches with wheel mounted inertial sensors.
</p>

## Sensors Used
Xsens DOTs - a low-cost IMU sensors. Eight used in each experiment to produce the raw data.<br/>
GNSS-RTK - an accurate positioning solution connected to the MRU-P that is licensed with the TerraStar-C Pro system.


## Platforms
Car - a private Skoda Roomster <br/>
![image](https://github.com/user-attachments/assets/02c63ccd-79db-4340-b54f-677d6c060259)

## Update 

Data and code will be available soon.

If you find the paper, dataset, or code helpful in your research, please cite our paper:

```bibtex@article{yampolsky2024multiple, title={Multiple and Gyro-Free Inertial Datasets}, author={Yampolsky, Zeev and Stolero, Yair and Pri-Hadash, Nitsan and Solodar, Dan and Massas, Shira}, journal={Scientific Data}, volume={11}, number={1}, pages={1080}, year={2024}, publisher={Nature Publishing Group UK London} }

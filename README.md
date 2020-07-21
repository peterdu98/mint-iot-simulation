# IoT Simulation for Mint Growth - Python
This repository is for implementing the IoT simulation for measuring the growth of mint by different environmental conditions such as temperature and humidity. Technologies used for implementation include Python, Azure Cloud (IoT Hub and Streaming Analytics Jobs) and Power BI. Also, this repository is used for Azure & Cloud Fundamentals (tech stream) in the Microsoft Student Accelerator (MSA) Project - Australia 2020.

## Description
In this project, there is an IoT simuluator for measuring the growth of mint via generated data of different environemental conditions such as temperature and humidity. The range of randomly generated data depends on different growth state of a particular plan. The following image shows the ideal environment rewarded system for a particular plant.

![Ideal environment and rewarded system for mint](https://github.com/peterdu98/mint-iot-simulation/blob/master/images/mint_growth.png)

Note that the information to sketch the image above is listed out in the *Refereces* section below. With the use of Azure Cloud as well as PowerBI, we can set up the simulated IoT devices for testing and draw the analytic report for streaming data from different devices. The project used only 1 device for testing, but the code can be customised to adapt the demand on sending messages from multiple devices.

## Knowledge path
- [x] Introduction to Azure IoT [MSLearn](https://docs.microsoft.com/en-us/learn/paths/introduction-to-azure-iot/)
- [x] Create and analytics reports with Power BI [MSLearn](https://docs.microsoft.com/en-us/learn/paths/create-use-analytics-reports-power-bi/)
- [x] Send telemetrty from device to an IoT Hub using Python [MSLearn](https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python#code-try-2)

## Tasks
- [x] Find resources about the growth of mint and sketch the plan
- [x] Implementation for generating random humidity and temperature values automatically
- [x] Set up devices in Azure IoT Hub and Streaming Analytics Jobs
- [x] Implementation for generating and sending messages to IoT Hub automatically
- [x] Testing connection between local machine and Azure server
- [x] Perform analytics for streaming dataset in PowerBI

## PowerBI Report
* [MintGrowthReport](https://app.powerbi.com/groups/me/reports/a2da6a35-9f50-4be7-ad75-0b5e4837fc84?ctid=df7f7579-3e9c-4a7e-b844-420280f53859) - In order to view the report, you need to register an account in PowerBI website.


## Requirements and Guidelines
* Python version: 3.7.3
* Cloning the project
```
	git clone https://github.com/peterdu98/mint-iot-simulation.git
```
* Set up dependencies
```
	pip install -r requirements.txt
```
* To sucessfully run the code, you need to set up Azure IoT Hub and customise the `.env` file with your connection string and the device's id.
* To run Stream Analytics Job, you need to set up Stream Analytics Job and run the following query
```
	SELECT
	    CAST(deviceId AS nvarchar(max)) AS PartitionKey,
	    CAST(iothub.EnqueuedTime AS datetime) AS RowKey,
	    CAST(plant_id AS bigint) AS PlantID,
	    CAST(temperature AS float) AS Temperature,
	    CAST(humidity AS float) AS Humidity,
	    CAST(growth_state AS nvarchar(max)) AS State,
	    CAST(reward AS float) AS Reward
	INTO
    	[Your alias storage]
	FROM
    	[Your alias IoT Hub]
```


## References
1. [Mint growing - NSW Gov](https://www.dpi.nsw.gov.au/agriculture/horticulture/vegetables/commodity-growing-guides/mint-growing)
2. [How to Grow Mint Indoors - WikiHow](https://www.wikihow.com/Grow-Mint-Indoors)
3. [Success With Mints](https://www.richters.com/show.cgi?page=MagazineRack/Articles/mint.html)
4. [azure-iot-samples-python - Github](https://github.com/Azure-Samples/azure-iot-samples-python)
import os
import time
import threading
from dotenv import load_dotenv
from azure.iot.device import Message

from generator import Humidity, Temperature
import listener

# Get variables from dotenv
load_dotenv()
DEVICE_ID = os.getenv("DEVICE_ID")

# Define the default value
LIMIT_GROWING_DAYS = 40			# The maximum number of days before harvesting
LIMIT_GROWING_REWARD = 40.0 	# The maximum number of rewarding scores before harvesting
MESSAGE = '{{ "deviceId": "{deviceId}", "plant_id": {plant_id}, "temperature": {temperature}, "humidity": {humidity}, "growth_state": "{state}", "reward": {reward} }}'

GROWTH_STATE = {
	"bRoot": "bRoot",			# Root begins
	"dRoot": "dRoot", 			# Root develops
	"growing": "growing", 		# Start growing
}

HUMIDITY_STATUS = {
	"Perfect": 0.0,				# Within the ideal condition
	"Normal": 5.0,				# 5% lower or higher than the ideal condition
	"Not well": 10.0 			# 10% lower or higher than the ideal condition
}

TEMPERATURE_STATUS = {
	"Perfect": 0.0, 			# Within the ideal condition
	"Normal": 3.0, 				# 3 degrees Celsius lower or higher than the ideal condition
	"Not well": 4.0 			# 5 degrees Celsius lower or higher than the ideal condition
}

def generate_daily_msg(temperature, humidity, days):
	# Set up objects based on the current number of grown days
	if days <= 3:
		temperature.set_init_value(20.0)
		humidity.set_init_value(85.0)

		temperature.set_range(22.0, 25.0)
		humidity.set_range(90.0, 100.0)

		growth_state = GROWTH_STATE["bRoot"]
	elif days <= 13:
		temperature.set_init_value(16.0)
		humidity.set_init_value(65.0)

		temperature.set_range(18.0, 22.0)
		humidity.set_range(70.0, 75.0)
		
		growth_state = GROWTH_STATE["dRoot"]
	else:
		temperature.set_init_value(13.0)
		humidity.set_init_value(65.0)

		temperature.set_range(15.0, 22.0)
		humidity.set_range(70.0, 75.0)

		growth_state = GROWTH_STATE["growing"]	

	# Generate condition information
	temp_info = temperature.generate_info()
	humi_info = humidity.generate_info()

	return temp_info, humi_info, growth_state

def start_planting():

	try:
		client = listener.iothub_client_init()
		print ("IoT Hub device sending periodic messages, press Ctrl-C to exit")

		# Start a thread to listen
		device_method_thread = threading.Thread(target=listener.device_method, args=(client,))
		device_method_thread.daemon = True
		device_method_thread.start()

		# Intialise variables
		temperature = Temperature(20.0, TEMPERATURE_STATUS)
		humidity = Humidity(85.0, HUMIDITY_STATUS)
		plant_id = 1
		days = 1
		curr_reward = 0

		# Start sending message
		while True:
			# Build the message with simulated telmetry values
			temp_info, humi_info, growth_state = generate_daily_msg(temperature, humidity, days)
			temp = temp_info["temperature"]
			humi = humi_info["humidity"]
			reward = temp_info["status"] + humi_info["status"]
			msg_txt_formatted = MESSAGE.format(deviceId= DEVICE_ID, plant_id=plant_id, temperature=temp, humidity=humi, state=growth_state, reward=reward)
			message = Message(msg_txt_formatted)
			
			# Go to a new day
			curr_reward += reward
			days += 1

			# Plant a new mint after harvesting the old one
			if days > LIMIT_GROWING_DAYS or curr_reward >= LIMIT_GROWING_REWARD:
				days = 1
				plant_id += 1
				curr_reward = 0

			# Send message
			print("Sending message: {}".format(message))
			client.send_message(message)
			print("Message sent")

			time.sleep(listener.INTERVAL)

	except KeyboardInterrupt:
		print("Stopped planting")

if __name__ == "__main__":
	print("IoT Mint Growth")
	print("Press Ctrl-C to exit.")
	start_planting()
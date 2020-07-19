from dotenv import load_dotenv
import os
from azure.iot.device import IoTHubDeviceClient, MethodResponse

# Get variables from dotenv
load_dotenv()
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
INTERVAL = 1

def iothub_client_init():
	# Create an IoT Hub client
	client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
	return client

def device_method(device_client):
	global INTERVAL

	while True:
		method_request = device_client.receive_method_request()

		if method_request.name == "SetTelemetryInterval":
			try:
				INTERVAL = int(method_request.payload)
			except ValueError:
				response_payload = { "Response": "Invalid parameter" }
				response_status = 400
			else:
				response_payload = { "Response": "Executed direct method {}".format(method_request.name) }
				response_status = 200
		else:
			response_payload = { "Response": "Direct method {} not defined".format(method_request.name) }
			response_status = 404

		print(response_payload)

		method_response = MethodResponse(method_request.request_id, response_status, payload=response_payload)
		device_client.send_method_response(method_response)
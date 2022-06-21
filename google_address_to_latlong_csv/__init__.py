import csv
import requests
import json

class AddressToLatLong:
	def __init__(self, input_csv_file: str = 'input_file.csv', output_csv_file: str = 'output_file.csv', google_api_key: str = '') -> None:
		self.INPUT_CSV_FILE = input_csv_file
		self.OUTPUT_CSV_FILE = output_csv_file
		self.GOOGLE_API_KEY = google_api_key

	def run(self):
		with open(self.INPUT_CSV_FILE, encoding='latin-1') as r, \
				open(self.OUTPUT_CSV_FILE, 'w', newline='', encoding="utf-8") as o:
			reader = csv.DictReader(r)
			writer = csv.DictWriter(
				o, fieldnames=reader.fieldnames +
								[
									"Google Address", "Place Id", "Google Lat", "Google Lng", "Location Type"
								])
			writer.writeheader()
			for count, line in enumerate(reader):
				print(count + 1, ":: ", line)
				written = False
				response_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json",{"address":line['Address'],"key": self.GOOGLE_API_KEY})
				
				query_results = response_json.json()["results"]

				if not query_results:
					line['Google Address'] = "Address Not Found"
					continue

				query_result = query_results[0]
				
				line['Google Address'] = query_result['formatted_address']
				line["Place Id"] = query_result['place_id']
				line['Google Lat'] = query_result['geometry']['location']['lat']
				line['Google Lng'] = query_result['geometry']['location']['lng']
				line['Location Type'] = query_result['geometry']['location_type']
						
				if not written:
					writer.writerow(line)
				o.flush()

if __name__ == '__main__':
	AddressToLatLong()
	print("Your Records Updated")
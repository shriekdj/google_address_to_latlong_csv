import csv
import requests
import json

GOOGLE_API_KEY = 'YOUR_API_KEY'
INPUT_CSV_FILE = 'input_file.csv'
OUTPUT_CSV_FILE = 'output_file.csv'

def search_with_areas():
	with open(INPUT_CSV_FILE, encoding='latin-1') as r, \
			open(OUTPUT_CSV_FILE, 'w', newline='', encoding="utf-8") as o:
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
			response_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json",{"address":line['Address'],"key":GOOGLE_API_KEY})
			
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
	search_with_areas()
	print("Your Records Updated")
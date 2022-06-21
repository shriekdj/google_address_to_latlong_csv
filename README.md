# google_address_to_latlong_csv

## What it does

This is a Python 3 Package which gets the list of data of addresses from an csv file and gives an output as csv with additional fields of latitude and longitude of the address provided by google GeoCoding API.

## Requirements

- Python 3 Installed
- Have Google API Key of `Google GeoCoding API` You can get it from Google Cloud Console


## Same Package for venv, pipenv and poetry

## Sample Input CSV File

```csv
ID,Address
1,"Nehru Nagar, Pimpri, Pune, Opp Sheetal Hotel, Pune, 411018"
2,"Rahatani Main Road, Rahatani, Pune, Near Baliraj Garden, Pune, 411017"
3,"Chinchwad East, Pune, Near Thermax Chowk, Pune, 411019"
4,"Shop No 7/61/2, Tapavan Road, Pimpri Gaon-Pimpri, Pune, Near Tapavan, Pune, 411018"
5,"Chinchwad, Pune, Near Post Office Chaphekar Chowk, Pune, 411033"
6,"Pune, Maharashtra, India, Pune, 411038"
7,"New Sanghvi Rd, Sangavi, Pune, Near Famous Chowk, Pune, 411027"
8,"Moshi, Pune, Nageshwar Nagar, Pune, 412105"
9,"Near Chintamani Chowk, Pune, 411035"
10,"Nigdi, Pune, Next Om Swadish Bhel, Pune, 411044"
```

## How to use the Package

Just Install with `pip install google-address-to-latlong-csv`

And in your Python Program run Given Below Commands

```python
from google_address_to_latlong_csv import AddressToLatLong

app = AddressToLatLong(input_csv_file="input.csv", output_csv_file="output.csv", google_api_key="google_api_key")

app.run()
```

the variable name `app` is not mandatory you can give any name to variable

If Any Issues occured raise `GitHub Issue on` [issues](https://github.com/shriekdj/google_address_to_latlong_csv) or Contact Me via mail me.

My Name Is **Shrikant Dhayje**.
My GitHub Username Is **[shriekdj](https://github.com/shriekdj)**.
My Official Email Id Is [shrikantdhayaje@gmail.com](mailto:shrikantdhayaje@gmail.com)

I Will Try to Give Response Within 24 Hours.

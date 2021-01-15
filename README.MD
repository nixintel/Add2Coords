## Add2Coords

Add2Coords is a simple Python tool for generating latitude and longitude data for any given location.

The script reads place names from a CSV file and uses Nominatim to search the OpenStreetMap database. Place names are resolved and Lat/Long coordinates obtained and written to a CSV output file.

See the attached ```example.csv``` for the CSV format.

The same data can also be used to generate an optional KML file by using the ```-k``` option.

### Nominatim Fair Usage

The data is collected from Nominatim. This is a free service and no API key is required, however queries are limited to 1 per second and large bulk queries are not permitted. See terms and conditions here:
https://operations.osmfoundation.org/policies/nominatim/

For heavier usage the script can be adapted to use a Google Maps API key, or the entire OpenStreetMap DB (98GB) can be downloaded and run on your local machine.

See here for alternatives to Nominatim in the GeoPy docs: https://geopy.readthedocs.io/en/stable/#module-geopy.geocoders



### Installation & Usage

Installation:
```
git clone https://github.com/nixintel/Add2Coords

cd Add2Coords

pip install -r requirements.txt
```

This has been test on Python 3.7. 

```
usage: coords.py [-h] -i INPUT -o OUTPUT [-k KML]

Takes location names and creates CSV with latitude and longitude. Optional KML
output.

optional arguments:
  -h, --help            Show this help message and exit
  -i INPUT, --input INPUT
                        Specify input CSV file containing raw location names.
  -o OUTPUT, --output OUTPUT
                        Specify filename for CSV file containing full address
                        and lat/long
  -k KML, --kml KML     Filename for KML file (optional)
```

### Example

```python coords.py -i example.csv -o coordinates.csv -k coordinates.kml ```


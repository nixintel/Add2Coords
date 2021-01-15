import csv
from geopy.geocoders import Nominatim
import simplekml
import pandas as pd
import argparse


def read_csv(file):
    """Reads addresses from input CSV"""
    locations_list = []

    locations_file = csv.reader(open(file, 'r'))

    for row in locations_file:
        locations_list.append(row)

    return locations_list


def get_latlong(address):
    """Takes address string, returns lat/long values"""
    geolocator = Nominatim(user_agent='Add2Coords')

    coords = []

    for a in address:

       try:
        print('Querying Nominatim for ' + str(a))
        location = geolocator.geocode(a, timeout=10)
        lat = location.latitude
        long = location.longitude

        coords.append([location, lat, long])

       except AttributeError:
           print('Issue with a query. Location ' + str(a) + ' could not be found. Check place name is valid.')
           continue
       else:
         df = pd.DataFrame(coords)

    print('Geocode lat/long lookups completed.')
    return df


def make_kml(csv_file, kml_filename):
    """Takes lat, long and address string from csv, converts to KML"""

    kml = simplekml.Kml()

    for row in csv_file:
        kml.newpoint(name=row[0], coords=[(row[2], row[1])])

    kml_file = kml.save(kml_filename)
    print('KML data saved as ' + str(kml_filename))

    return kml_file


def main():

    # Set arguments

    parser = argparse.ArgumentParser(description='Takes location names and creates CSV with latitude and longitude.'
                                                 ' Optional KML output.')

    parser.add_argument('-i', '--input', help='Specify input CSV file containing raw location names.', required=True)

    parser.add_argument('-o', '--output', help='Specify filename for CSV file containing full address and lat/long', required=True)
    parser.add_argument('-k', '--kml', help='Filename for KML file (optional)')

    args = parser.parse_args()

    input_csv = args.input
    output_csv = args.output
    kml_output = args.kml

    # Read input CSV

    locations = read_csv(input_csv)

    # Convert DataFrame to CSV

    df = get_latlong(locations)
    df.to_csv(str(output_csv), index=False, encoding='utf-8', header=False)
    print('Saving data to ' + str(output_csv))

    # Create KML file from CSV

    if args.kml:
        coords_csv = csv.reader(open(output_csv, 'r'))
        make_kml(coords_csv, kml_output)


main()







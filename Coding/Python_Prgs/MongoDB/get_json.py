import json
from urllib.request import urlopen

# -------------- URL's and their File names -------------------

# National Vulnerabilities Database URL
nvd = "https://csrc.nist.gov/schema/nvd/feed/1.0/cvss-v2.0.json"
nvd_file = "National_Vulnerabilities_Database.json"

# Uk Police Senior Officers
ukp = "https://data.police.uk/api/forces/leicestershire/people"
ukp_file = "UK_Police_Senior_Officers.json"

# Uk Police List of forces
ukp_lof = "https://data.police.uk/api/forces"
ukplof_file = "UK_Police_List_of_Forces.json"

# Metaweather URL
mw = "https://www.metaweather.com/api/location/44418/"
mw_file = "Weather.json"


# --------------------------------------------------------------


# -------------- Fetching the Data -----------------------------

# Opening the Url and fetching the data in json format

print("Connecting to URL.......")

with urlopen(mw) as f:
    source = f.read()

print("Fetching Data Completed!!!")

# -------------------------------------------------------------

# Converting the fetched json string into json object
data = json.loads(source)

print("Conversion Completed!!!")


# ------------- Writing into File -----------------------------

print("Writing into the File.......")

# Dumping the json data into the respective file
with open(mw_file, "w") as f:
    json.dump(data, f, indent=2)

print("Completed Successfully..........")

# -------------------------------------------------------------
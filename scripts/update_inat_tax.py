import requests
import time
import json
import os.path
import pandas as pd

# read in existing database
obs = pd.read_csv('_data/inat-observations-425614-with-updates.csv')

unique_taxa = obs['taxon_id'].dropna().unique()

if os.path.isfile('_data/inat_taxonomy.json'):

  with open('_data/inat_taxonomy.json', 'r') as j:
    all_taxa = json.loads(j.read())

  all_taxa_ids = [x['id'] for x in all_taxa]

else:

  all_taxa = []
  
  all_taxa_ids = []

new_taxa = list(set(unique_taxa).difference(all_taxa_ids))

# Set the base URL for the iNaturalist API v1
base_url = 'https://api.inaturalist.org/v1/taxa'

# 30 taxa per request
for i in range(0,len(new_taxa)):
  
  response = requests.get(base_url, params={'id': new_taxa[i], 'per_page': 1})

  data = response.json()
  if 'results' not in data:
    print(f"Warning: unexpected response for taxon {new_taxa[i]}: status={response.status_code}, keys={list(data.keys())}")
    continue

  all_taxa.extend(data['results'])
  
  # Wait for 1 second before the next request
  time.sleep(1)

with open('_data/inat_taxonomy.json', 'w') as f:
    json.dump(all_taxa, f)

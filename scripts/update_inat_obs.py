import requests
import time
from io import StringIO
import pandas as pd

# find dates corresponding to latest updates and observations in existing dataset
df = pd.read_csv('_data/inat-observations-425614-with-updates.csv')

df_latest = pd.to_datetime(df['updated_at'], format='mixed').max().isoformat()

## get new observations

# Set the base URL for the iNaturalist API
base_url = 'https://inaturalist.org/observations/rmcminds'

# Define the parameters for the request
params = {
    'updated_since': df_latest,
    'per_page': 200,
    'page': 1
}

new_observations = pd.DataFrame()
del_observations = []

while True:
  # Make the request
  response = requests.get(base_url + '.csv', params=params)

  # Parse the response csv
  new_csv = pd.read_csv(StringIO(response.text))
  
  # Append the new obs
  new_observations = pd.concat([new_observations, new_csv])
  
  # Append deleted obs if there are any
  headers = requests.head(base_url + '.json', params=params).headers
  if 'X-Deleted-Observations' in headers.keys():
    del_observations.extend([int(i) for i in headers['X-Deleted-Observations'].split(',')])

  # If this is the last page, break out of the loop
  if len(new_csv.index) < params['per_page']:
      break

  # Otherwise, increment the page counter
  params['page'] += 1
  
  # Wait for 1 second before the next request
  time.sleep(1)


# add observations to database
new_df = df
if len(new_observations.index) > 0:

  new_observations['private_latitude'] = None
  new_observations['private_longitude'] = None
  new_observations['private_place_guess'] = None

  new_df = pd.concat([new_df, new_observations[df.columns.intersection(list(new_observations.columns))]]).drop_duplicates(subset='id', keep='last')

# remove observations from database
if len(del_observations) > 0:

  new_df = new_df[~new_df['id'].isin(del_observations)]

# save updated database
new_df.to_csv('_data/inat-observations-425614-with-updates.csv', index=False)


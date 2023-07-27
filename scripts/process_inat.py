import pandas as pd
import json

number_keep = 20

obs = pd.read_csv('_data/inat-observations-345649-with-updates.csv')

obs = obs.sort_values(by=['time_observed_at'], ascending=False)

# load taxonomy data
with open('_data/inat_taxonomy.json', 'r') as j:
  taxa = json.loads(j.read())

# make a simple dictionary relating each taxon id with a list of itself and its ancestors
taxa_dict = {}
for taxon in taxa:
  taxa_dict[taxon['id']] = taxon['ancestor_ids']

# simplify dataset by removing exact taxon duplicates
obs_unique = obs.drop_duplicates(subset='taxon_id',keep='last').reset_index()

# check if unique taxa are actually first-timers, or if they are higher taxa for an earlier observation
attempted = 0
saved = 0
final_obs = pd.DataFrame()
while True:

  # pull all self- and ancestral- ids for each unique taxon observed before the one being tested
  all_before = [taxa_dict[query] for query in obs_unique.truncate(before=attempted+1)['taxon_id']]
  
  # collapse nested list into a simple list
  all_before = [x for sl in all_before for x in sl]
  
  # if observation being tested is a taxon never before seen, add it to the output and increment the number of output records
  if obs_unique['taxon_id'][attempted] not in all_before:
  
    final_obs = pd.concat([final_obs, obs_unique.truncate(before=attempted, after=attempted)])
    
    saved += 1
    
  # increment observation being tested
  attempted += 1

  # if number of output records is the number we want, stop testing for more
  if saved == number_keep:
  
    break

final_obs.to_csv('_data/most_recent_new_taxa.csv', index=False)

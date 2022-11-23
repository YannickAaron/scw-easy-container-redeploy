
import os
import sys
import requests

# extracting all the input from environments
organization_id = os.environ['INPUT_ORGANIZATION_ID']
project_id = os.environ['INPUT_PROJECT_ID']
api_version = os.environ['INPUT_API_VERSION']
region = os.environ['INPUT_REGION']
container_name = os.environ['INPUT_CONTAINER_NAME']
api_secret_key = os.environ['INPUT_API_SECRET_KEY']

#make sure that all required inputs are provided
if api_version == '' or region == '' or container_name == '' or api_secret_key == '':
  print('Error: Missing required inputs')
  sys.exit(1)

getparams = {}
baseurl = f"https://api.scaleway.com/containers/{api_version}/regions/{region}/containers"

if organization_id != '':
  getparams['organizationId'] = organization_id

if project_id != '':
  getparams['projectId'] = project_id

headers = {
  'X-Auth-Token': api_secret_key
}

response = requests.get(baseurl, params=getparams, headers=headers)

if response.status_code != 200:
  print('Error: Failed to get containers: there was an error with the request')
  sys.exit(1)

containers = response.json()['containers']

container_id = ''
for container in containers:
  if container['name'] == container_name:
    container_id = container['id']
    break

if container_id == '':
  print(f'Error: Failed to get container_id: container with the name {container_name} not found')
  sys.exit(1)

print(f'Redeploying Container ID: {container_id}')

response = requests.post(f"{baseurl}/{container_id}/deploy", headers=headers, data='{}')

if response.status_code != 200:
  print('Error: Failed to redeploy container: there was an error with the request')
  sys.exit(1)

print('Redeployed container successfully')
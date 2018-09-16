
from google.cloud import storage
import sys

# Explicitly use service account credentials by specifying the private key
# file.
storage_client = storage.Client.from_service_account_json('pennapps-fit.json')

# Make an authenticated API request
##buckets = list(storage_client.list_buckets())
##print(buckets)

bucketname = sys.argv[1]
filename = sys.argv[2]


bucket = storage_client.get_bucket(bucketname)

destination_blob_name = filename
source_file_name = filename

blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)
blob.make_public()

print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))

import duolingo
from huggingface_hub import HfApi
import json
import datetime
import huggingface_hub
import dotenv
import os
import sys
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=False, help="name of the user")
ap.add_argument("-f", "--huggingface-token", required=False, help="huggingface token")
ap.add_argument("-j", "--jwt", required=False, help="duolingo jwt token")
args = vars(ap.parse_args())

if args["username"] is None:
    dotenv.load_dotenv("..")

    JWT_TOKEN = os.getenv("JWT_TOKEN")
    HF_TOKEN = os.getenv("HF_TOKEN")
    USERNAME = os.getenv("USERNAME")
else:
    JWT_TOKEN = args["jwt"]
    HF_TOKEN = args["huggingface_token"]
    USERNAME = args["username"]

lingo  = duolingo.Duolingo(username=USERNAME, jwt=JWT_TOKEN)
result = lingo.get_user_info()

today = datetime.date.today().isoformat()
json_filename = f'{today}_profile_auth.json'
with open(json_filename, 'w') as outfile:
    json.dump(result, outfile)

huggingface_hub.login(HF_TOKEN)

api = HfApi()
api.upload_file(
    path_or_fileobj=json_filename,
    path_in_repo=json_filename,
    repo_id="osbm/duolingo_progress",
    repo_type="dataset",
)
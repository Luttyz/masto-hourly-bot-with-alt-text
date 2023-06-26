import json
import requests
import shutil 
from mastodon import Mastodon

retries = 0

# set the API's used URL
url = "https://api.tinyfox.dev/img?animal=capy"

r = requests.get(url, stream = True)

# This part definitely wasn't copy pasted and I definitely do understand what it does yes yes

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open("capybara.jpg",'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded')
else:
    print('Image couldn\'t be downloaded')

# Send through Mastodon server (used in example : my own server)
mastodon = Mastodon(
    access_token = 'dummy-access-token-GO-GET-YOUR-OWN',
    api_base_url = 'https://instance.example'
)
# if needed : the masto.ml instance (my own) is bot-friendly, as long as asked before creating the account and posted in unlisted, and botsin.space was specifically made for bots

# Upload image and get media ID
media = mastodon.media_post('capybara.jpg', description=alt_text, mime_type="image/jpeg")

# Post status with media ID and alt text
mastodon.status_post('Here\'s an image of a #Capybara! #HourlyAnimals', media_ids=[media])

# andrewschmidt

*** To copy dir from local to remote
- sudo scp -i PersonalWebsiteKey.pem -r <local dir> ubuntu@<Public DNS ipv4>:/home/ubuntu/personal-website/<rest of path>

*** To copy files from local to remote
- sudo scp -i PersonalWebsiteKey.pem <local files> ubuntu@<Public DNS ipv4>:/home/ubuntu/personal-website/<rest of path>

*** To apply changes
- sudo ssh -i PersonalWebsiteKey.pem ubuntu@<Public DNS ipv4>
- git pull
- source env/bin/activate
- pip install -e .
- npm install .
- node_modules/.bin/webpack
- pkill -f gunicorn
- pgrep -af gunicorn
- gunicorn -b localhost:8000 -w 2 -D andrewschmidt:app
- exit ssh
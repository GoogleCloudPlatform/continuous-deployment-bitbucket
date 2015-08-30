# Sample of how to deploy from Travis CI and run an end-to-end test

This repo demonstrates how to deploy to Google Cloud from a 
Travis file and run an end to end test ( in e2e_test.py) against 
a staging environment.

Please see the associated blog post for details.

See the `managed_vms` example for a similar repo and Travis deployment
using Managed VMs.

## Prerequisites

* Download [Google Cloud SDK](https://cloud.google.com/sdk/)
* Install [Travis CI client](http://blog.travis-ci.com/2013-01-14-new-client/)

## Steps to deploy to your own App Engine project
* Enable your repo or fork of this repo on Travis CI
* Delete existing credentials
`rm credentials.tar.gz.enc`
* Enable the Books API
* Download a Public API Key and add it to api_key.py (see sample)
* Download a Service Account JSON file, copy it into this direcotry as  'cont-deployment.json'
* Remove the openssl line from the .travis file
* `tar -czf credentials.tar.gz api_key.py cont-deployment.json'
* `travis login`
* Encrypt the file with travis, using --add adds the SSL command back 
to the .travis file 
   `travis encrypt-file credentials.tar.gz --add`
* Add the encrypted archive and the changes to the .travis file to your repo
  `git add credentials.tar.gz`
  `git add .travis.yml`
  `git commit -m "Add credentials and Travis changes`
* Push to your repo and read the Travis console to verify the build succeeds
  `git push origin master`


## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)


## Licensing

* See LICENSE

Copyright (C) 2015 Google Inc.

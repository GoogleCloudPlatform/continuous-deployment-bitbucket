[![Build Status](https://travis-ci.org/GoogleCloudPlatform/continuous-deployment-demo.svg)](https://travis-ci.org/GoogleCloudPlatform/continuous-deployment-demo)

# Sample of how to deploy from Travis CI and run an end-to-end test

This repo demonstrates how to deploy to Google Cloud from a 
Travis file and run an end to end test ( in e2e_test.py) against 
a staging environment.

See the [managed_vms](https://github.com/googlecloudplatform/continuous-deployment-demo/tree/managed_vms) branch for a similar repo and Travis deployment using Managed VMs.

# Travis Continual Deployment Provider

Travis has a  [builtin Travis deploy provider](http://docs.travis-ci.com/user/deployment/) that can simplify your .travis.yml.

The main difference is that you no longer need to explicitly download the 
Cloud SDK and run the deploy command, although you still need to 
specify a service account credential.

To see an example, look at the following branches:

* App Engine [appengine_travis_deploy](https://github.com/GoogleCloudPlatform/continuous-deployment-demo/tree/appengine_travis_deploy)
* Managed VMS [managed_vms_travis_deploy](https://github.com/GoogleCloudPlatform/continuous-deployment-demo/tree/managed_vms_travis_deploy)

## Prerequisites

* Download [Google Cloud SDK](https://cloud.google.com/sdk/)
* Install [Travis CI client](http://blog.travis-ci.com/2013-01-14-new-client/)

## Steps to deploy to your own App Engine project

You can watch a screencast that walks through these steps with this repo here.

https://www.youtube.com/watch?v=7U4jjRw_AJk&feature=youtu.be

Note that the Books API Key is a specific requirement of this app, but is not generally
necessary to deploy from Travis. The service account credential is always necessary, 
in order to authenticate the gcloud command line tool.

* Enable your repo or fork of this repo on Travis CI
* Delete existing credentials
`rm credentials.tar.gz.enc`
* Enable the Books API
* Enable the App Engine Admin API
* Download a Public API Key and add it to api_key.py (see sample)
* Download a Service Account JSON file, copy it into this direcotry as  'client-secret.json'
* Remove the openssl line from the .travis file
* `tar -czf credentials.tar.gz api_key.py client-secret.json'
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

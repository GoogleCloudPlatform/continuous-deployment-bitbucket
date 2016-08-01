# Sample of how to deploy from Bitbucket Pipelines and run an end-to-end test

This repo demonstrates how to deploy to Google Cloud from  Bitbucket Pipelines
and run an end to end test (in e2e_test.py) against a staging environment.

## Prerequisites

* Download [Google Cloud SDK](https://cloud.google.com/sdk/)

## Steps to deploy to your own App Engine project

Note that the Books API Key is a specific requirement of this app,
but is not generally necessary to deploy from Bitbucket Pipelines.
The service account credential is always necessary, 
in order to authenticate the gcloud command line tool.

* Enable your repo or fork of this repo on Bitbucket Pipelines
* Delete existing credentials
`rm credentials.tar.gz.enc`
* Enable the Books API
* Enable the App Engine Admin API
* Download a Public API Key and add it to
`api_key.py` (see sample)
* Download a Service Account JSON file,
copy it into this direcotry as 
`client-secret.json`
* `tar -czf credentials.tar.gz api_key.py client-secret.json`

## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Licensing

* See [LICENSE](LICENSE)

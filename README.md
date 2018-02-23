# JupyterLab on Heroku + Amazon S3

This application runs a JupyterLab instance on Heroku, backed by Amazon S3.

Deploy to Heroku
----------------

You can deploy this application to Heroku with this simple button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


Environment Variables
---------------------

The following environment variables are expected to be set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `S3_BUCKET_NAME`

Optional:

- `PASSWORD`
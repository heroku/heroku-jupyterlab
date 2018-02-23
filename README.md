# JupyterLab on Heroku + Amazon S3

This application runs a JupyterLab instance on Heroku, backed by Amazon S3.


Environment Variables
---------------------

The following environment variables are expected to be set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `S3_BUCKET_NAME`

Optional:

- `PASSWORD`
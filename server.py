import os

from s3monkey import S3FS
from notebook import notebookapp as app
# from jupyterlab import labapp as app


PORT = os.environ.get('PORT', '8080')
S3_DATA_DIR = '/app/data'


# Launch Jupyter Notebook.
args = [
    '--no-browser', '-y', '--ip=*', '--port', PORT,
    '--config=config.py'
     '--NotebookApp.token=\'\'', # '--NotebookApp.password=\'\''
     # '--NotebookApp.contents_manager_class=S3ContentsManager'
    # '--notebook-dir={}'.format(S3_DATA_DIR), # '--generate-config'
]
print(' '.join(args))
print(app)
# exit()


# with S3FS('kr-test-jupyter', S3_DATA_DIR, other_dirs=['/dev/fd', '/Volumes'], create=True) as fs:
print(app.launch_new_instance(argv=args))

import requests
import tarfile

def get_zip_file_by_url(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

def untar_file(tar_file, untar_directory):
    with tarfile.open(tar_file, 'r') as data_tgz:
        data_tgz.extractall(path=untar_directory)






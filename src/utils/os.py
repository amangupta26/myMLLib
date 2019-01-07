import requests

def get_zip_file_by_url(url, path):
    print("0000")
    r = requests.get(url, stream=True)
    print("1111")
    with open(path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            print("222")
            fd.write(chunk)




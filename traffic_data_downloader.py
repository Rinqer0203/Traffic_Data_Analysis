'''
トラフィックデータをダウンロードするスクリプト
'''
import os
import requests
import zipfile

# ダウンロードするトラフィックデータのURL
URLS = [
    "https://www.takakura.com/Kyoto_data/new_data201704/2015/201501.zip",
    "https://www.takakura.com/Kyoto_data/new_data201704/2015/201502.zip"
]
DEST_FOLDER = "./data"


def download_file(url, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    filename = dest_folder + '/' + url.split('/')[-1]

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        downloaded_size = 0
        chunk_size = 8192

        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                downloaded_size += len(chunk)
                progress = downloaded_size / total_size * 100
                print(f"\r{filename}: {progress:.2f}%", end='')

    print(f"\nDownloaded {filename}")
    return filename


def extract_zip(file_path, dest_folder):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    print(f"Extracted {file_path} to {dest_folder}")
    os.remove(file_path)
    print(f"Removed {file_path}")


if __name__ == "__main__":
    for url in URLS:
        zip_file = download_file(url, DEST_FOLDER)
        extract_zip(zip_file, DEST_FOLDER)

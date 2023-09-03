import os
from tqdm import tqdm
import tarfile
from urllib.request import urlretrieve

DATA_DIR = 'data/tpugraphs/'

filenames = [f'npz_tile_xla_{split}.tar' for split in ('train', 'test', 'valid')]

for source in ('xla', 'nlp'):
    for search in ('default', 'random'):
      for split in ('train', 'valid', 'test'):
        filenames.append(f'npz_layout_{source}_{search}_{split}.tar')

# Create the directory if it doesn't exist.
os.makedirs(DATA_DIR, exist_ok=True)

# Download the files from http://download.tensorflow.org/data/tpu_graphs/v0/{filename}.
# If the file already exists, skip the download.
for file in tqdm(filenames):
    url = f'http://download.tensorflow.org/data/tpu_graphs/v0/{file}'
    local_path = DATA_DIR + file
    if not os.path.exists(local_path):
        urlretrieve(url, local_path)
        # Extract the tar file.
        tarfile.open(local_path).extractall(DATA_DIR)

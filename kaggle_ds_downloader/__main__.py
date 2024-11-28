
import os
from kaggle.api.kaggle_api_extended import KaggleApi


def main(
    dataset_id: str = "dataset-name",
    destination: str = "./data"
):
    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset_id,
        path=destination,
        unzip=True
    )



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='What this program is going to do.'
    )
    parser.add_argument(
        '--dataset_id', '-DID', type=str, default='./image/lake_michigan.jpg', help=''
    )
    parser.add_argument(
        '--destination', '-DP', type=str, default='./kaggle_data', help='kaggle_data'
    )
    args = parser.parse_args()

    main(
        args.dataset_id,
        args.destination
    )
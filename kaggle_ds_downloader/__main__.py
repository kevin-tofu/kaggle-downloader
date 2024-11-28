

from kaggle.api.kaggle_api_extended import KaggleApi


def main(
    dataset_id: str = "dataset-name",
    destination: str = "./data"  # ダウンロード先ディレクトリ
):
    # Kaggle APIの初期化
    api = KaggleApi()
    api.authenticate()

    # データセットのダウンロード
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
import os

import logging
import click
from sklearn.datasets import load_wine

logger = logging.getLogger("Download")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    X, y = load_wine(return_X_y=True, as_frame=True)

    os.makedirs(output_dir, exist_ok=True)
    logger.info(f"Data Downloaded to OUTPUT_DIR: {output_dir}")
    X.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == '__main__':
    download()
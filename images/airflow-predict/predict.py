import logging
import os
import pandas as pd

import click
logger = logging.getLogger("Predict")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


@click.command("predict")
@click.argument("input-dir")
@click.argument("output-dir")
def predict(input_dir: str, output_dir):
    logging.info(f"Data trying to read from {os.path.join(input_dir, 'data.csv')}")
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    # do real predict instead
    data["predict"] = 1

    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Writing into {output_dir}")
    data.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == '__main__':
    predict()
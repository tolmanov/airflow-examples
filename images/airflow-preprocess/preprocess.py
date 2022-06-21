import logging
import os
import pandas as pd
import click

logger = logging.getLogger("Predict")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

@click.command("preprocess")
@click.argument("input-dir")
@click.argument("output-dir")
def preprocess(input_dir: str, output_dir):
    logger.info(f"Reading data from {input_dir}/data.csv")
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    # do something instead
    data["features"] = 0

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == '__main__':
    preprocess()
import papermill as pm
import datetime
from pathlib import Path
import yaml
import os
from typing import Dict
import argparse


def load_config(path: str = None) -> Dict:
    if not path:
        path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "parameters.yaml")
        )
    with open(path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise FileNotFoundError(exc)
    return config


def main(specs: Dict, params: Dict) -> None:
    try:
        output = "outputs/{0}".format(datetime.datetime.now().strftime("%Y-%m-%d"))
        Path(output).mkdir(parents=True, exist_ok=True)
        for book in specs["Notebooks"]:
            pm.execute_notebook(
                book,
                "{0}/{1}_{2}.ipynb".format(
                    output,
                    book.split("/")[-1].split(".")[0],
                    datetime.datetime.now().strftime("%Y%m%d%H%M"),
                ),
                parameters=params,
            )
    except Exception as e:
        raise (e)


parser = argparse.ArgumentParser(description="Notebook as pipeline")
parser.add_argument("--spec", "-s", required=False, help="Run time Configs")
parser.add_argument(
    "--parameters", "-p", required=False, help="parameters yaml location"
)
args = parser.parse_args()

if __name__ == "__main__":
    specs = load_config(args.spec)
    config = load_config(args.parameters)
    main(specs,config)

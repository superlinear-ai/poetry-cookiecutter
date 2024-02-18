"""This module contains the training logic."""
import json
import os
import subprocess
import typer
import wandb

def retrieve_data():
    """Retrieve data from Data Version Control.

    This function retrieves the data from DVC and moves it to the input directory.
    It is advisable not to keep this unless you are using DVC.

    This function moves the contents of the data/ folder using the * wildcard to move all subfolders and files.
    """
    # Data Version Control
    commands = [
        "dvc pull",
        "cp -rv data/* /opt/ml/input/data/",
        "rm -rf data",
        "ls -hR /opt/ml/input/data/",
    ]

    for cmd in commands:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check if the command was executed successfully
        if process.returncode != 0:
            print(f"Error executing '{cmd}': {stderr.decode()}")
        else:
            print(f"Output of '{cmd}': {stdout.decode()}")
    
    return None

    
def train(
    hosts: list = typer.Option(
        json.loads(os.environ["SM_HOSTS"]), 
        help="Sagemaker specific environment variables"
    ),
    current_host: str = typer.Option(
        os.environ["SM_CURRENT_HOST"], 
        help="Sagemaker specific environment variables"
    ),
    model_dir: str = typer.Option(
        os.environ["SM_MODEL_DIR"], 
        help="Sagemaker specific environment variables"
    ),
    data_dir: str = typer.Option(
        "/opt/ml/input/data/", 
        help="Sagemaker specific environment variables"
    ),
    num_gpus: int = typer.Option(
        int(os.environ["SM_NUM_GPUS"]), 
        help="Sagemaker specific environment variables"
    )
    ):
    """Train the model."""
    
    # Retrieve the Dataset
    _ = retrieve_data()

    # Training logic
    # ...
    # ...
    # ...

    pass

if __name__ == "__main__":
    wandb.init(
        id=os.environ["WANDB_RUN_ID"], 
        resume="allow", 
        name=os.environ["GITHUB_SHA"]
    )
    typer.run(train)

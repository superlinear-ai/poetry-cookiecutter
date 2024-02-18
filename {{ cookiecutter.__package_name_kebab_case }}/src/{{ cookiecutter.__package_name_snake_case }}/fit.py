"""{{ cookiecutter.package_name }} Sagemaker Training Launch Script."""
import boto3
import sagemaker
import wandb
from sagemaker.estimator import Estimator

from {{ cookiecutter.__package_name_snake_case }}.settings import Settings

# Github Actions CI/CD Passthrough
settings = Settings()

# Sagemaker Variables
SESSION = sagemaker.Session(boto3.Session(region_name="us-east-1"))
TRAINING_INSTANCE = "ml.g4dn.xlarge"

# W&B Variables
run_id = wandb.util.generate_id()  # type: ignore
wandb.init(
    id=run_id,
    project=settings.github_repo_name,
    entity="{{cookiecutter.variable_name | lower | replace(' ', '_') | replace('-', '_')}}",
    name=settings.short_sha,
    tags=["debugging", "wandb", "sagemaker"],
)
wandb_run_url = wandb.run.get_url()  # type: ignore

# Hyperparameters
hyperparameters = {
    "epochs": 20,
    "momentum": 0.5,
}

# Environment Variables
environment = {
    "WANDB_RUN_ID": run_id,
    "WANDB_API_KEY": settings.wandb_api_key,
    "WANDB_PROJECT": settings.github_repo_name,
    "WANDB_RUN_GROUP": settings.short_sha,
    "GITHUB_SHA": settings.short_sha,
}

# Define Estimator
estimator = Estimator(
    image_uri=settings.ecr_repo_name,
    role=settings.iam_role,
    entry_point="src/{{ cookiecutter.__package_name_snake_case }}/train/train.py",
    instance_type=TRAINING_INSTANCE,
    instance_count=1,
    environment=environment,
    hyperparameters=hyperparameters,  # type: ignore
    base_job_name=settings.output_s3_uri,
    output_path=settings.output_s3_uri,
    code_location=settings.output_s3_uri,
    sagemaker_session=SESSION,
    source_dir="./",
    dependencies=["src/{{ cookiecutter.__package_name_snake_case }}/train/requirements.txt"],
)

estimator.fit(job_name=f"{settings.short_sha}", wait=False, logs="Training")
wandb.run.finish(quiet=True)  # type: ignore

# Create a CML Runner Comment
message = (
    f":crystal_ball: Hi! Sagemaker training launch detected. :rocket: \n\n"
    f"You can view the details of this run in the table by clicking on the link below.\n\n"
    f"| Item | Value |\n"
    f"| --- | --- |\n"
    f"| Job Name | {settings.short_sha} |\n"
    f"| Training Instance | {TRAINING_INSTANCE} |\n"
    f"| W&B :sparkles: Job URL | [Here]({wandb_run_url}) |\n"
    f"| S3 Artifacts | [Here]({settings.s3_http_url}) |\n"
    f"| Training Logs | [Here]({settings.cloudwatch_logs}) |\n"
    "If this training job was not to your liking, please close this PR and start another.\n\n"
)

# Convert the tuple to a string
message_str = "".join(message)

# Write the comment to the PR
with open("details.txt", "w") as f:
    f.write(message_str)

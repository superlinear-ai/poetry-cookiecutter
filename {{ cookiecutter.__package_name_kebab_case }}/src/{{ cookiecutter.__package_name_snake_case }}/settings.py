"""This module contains the settings for SageMaker."""
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """A class that represents the settings for the SageMaker Script.

    Attributes:
                github_ref_name (str): The name of the GitHub reference (branch or tag) being used.
                github_sha (str): The SHA of the GitHub commit being used.
                github_repository (str): The URL of the GitHub repository.
                github_actor (str): The username of the GitHub actor (user or bot) triggering the pipeline.
                output_s3_uri (str): The S3 URI for the output of the pipeline.
                ecr_account_id (str): The ID of the AWS account where the ECR repository is located.

    Methods:
    check_s3_uri(cls, v): A validator method that checks if the provided URI is a valid S3 URI.

    Config:
    env_file (str): The name of the environment file to load configuration from.
    """

    # Github Actions environment variables
    github_ref_name: str = os.environ.get("GITHUB_REF_NAME")
    github_sha: str = os.environ.get("EVENT_SHA")
    github_repository: str = os.environ.get("GITHUB_REPOSITORY")
    github_repo_name = github_repository.split("/")[-1]
    github_actor: str = os.environ.get("GITHUB_ACTOR")
    short_sha: str = github_sha[:7]
    ecr_account_id: str = os.environ.get("ECR_ACCOUNT_ID")

    # AWS Environment Variables
    output_s3_uri: str = f"s3://{{cookiecutter.__organization_name_kebab_case}}-sagemaker/fits/{github_repo_name}/{github_ref_name}/"
    s3_http_url: str = f"https://{{cookiecutter.__organization_name_kebab_case}}-sagemaker.s3.amazonaws.com/fits/{github_repo_name}/{github_ref_name}/{short_sha}/"
    ecr_repo_name: str = f"{ecr_account_id}.dkr.ecr.us-east-1.amazonaws.com/{{cookiecutter.__organization_name_kebab_case}}-sagemaker-container:{github_repo_name}"
    iam_role: str = os.environ.get("SAGEMAKER_IAM_ROLE")
    cloudwatch_logs: str = rf"https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/\$252Faws\$252Fsagemaker\$252FTrainingJobs\$3FlogStreamNameFilter\$3D{short_sha}"

    # W&B Environment Variables
    wandb_api_key: str = os.environ.get("WANDB_API_KEY")

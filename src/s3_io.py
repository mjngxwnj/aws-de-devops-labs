import os
from pathlib import Path
from aws_client import AWSClients

#configuration
BUCKET_NAME = "huynhthuan-bucket-test"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOCAL_INPUT_FILE_PATH = PROJECT_ROOT / "data" / "input" / "test.txt"
LOCAL_OUTPUT_FILE_PATH = PROJECT_ROOT / "data" / "output" / "test.txt"
S3_KEY = "test.txt"


#function to upload file
def upload_to_S3(local_input_file_path: Path, bucket_name: str, s3_key: str, client):
    """
    Upload a local file to S3.

    Args:
        local_input_file_path (Path): Path to the local file
        bucket_name (str): Target S3 bucket
        s3_key (str): Key in S3 bucket
        s3_client: boto3 S3 client
    """

    if not local_input_file_path.exists():
        print(f"[ERROR] Local file {local_input_file_path} does not exist")
        return

    try:
        client.upload_file(str(local_input_file_path), bucket_name, s3_key)
        print(f"[INFO] Uploaded to s3://{bucket_name}/{s3_key}")
    except client.exceptions.NoSuchBucket:
        print(f"[ERROR] Bucket {bucket_name} does not exist")
    except Exception as e:
        print(f"[ERROR] Failed to upload file: {e}")


#function to download file
def download_from_s3(bucket_name: str, s3_key: str, local_output_file_path: Path, client):
    """
    Download a file from S3 bucket to local path.

    Args:
        bucket_name (str): Target S3 bucket
        s3_key (str): Key in S3 bucket
        local_output_file_path (Path): Path to the local file
        s3_client: boto3 S3 client
    """

    try:
        client.download_file(bucket_name, s3_key, str(local_output_file_path))
        print(f"[INFO] Downloaded s3://{bucket_name}/{s3_key} to {local_output_file_path}")
    except client.exceptions.NoSuchKey:
        print(f"[ERROR] S3 object '{s3_key}' does not exist in bucket '{bucket_name}'")
    except Exception as e:
        print(f"[ERROR] Failed to download file: {e}")


if __name__ == "__main__":
    #initialize AWS client manager
    aws = AWSClients()

    #get S3 client with default region
    s3_client = aws.get_client("s3")

    upload_to_S3(LOCAL_INPUT_FILE_PATH, BUCKET_NAME, S3_KEY, s3_client)
    download_from_s3(BUCKET_NAME, S3_KEY, LOCAL_OUTPUT_FILE_PATH, s3_client)

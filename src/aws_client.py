import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


#load env
load_dotenv()

#get variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")


class AWSClients:
    """
    Class to manage AWS clients (S3, Lambda, DynamoDB, ...).
    Supports credentials from .env or IAM role.
    Cache clients to reuse them.
    """

    def __init__(self):
        """
        Initialize a single AWS session for the class.
        """

        self._default_region_name = os.getenv("AWS_DEFAULT_REGION", "ap-southeast-1")
        self._access_key  = os.getenv("AWS_ACCESS_KEY_ID")
        self._secret_key  = os.getenv("AWS_SECRET_ACCESS_KEY")

        try:
            session_args = {}

            if self._access_key and self._secret_key:
                session_args["aws_access_key_id"] = self._access_key
                session_args["aws_secret_access_key"] = self._secret_key

            else:
                print("[WARNING] AWS credentials not found in environment variables")

            self._session = boto3.Session(**session_args)

        except Exception as e:
            print(f"[ERROR] Error processing AWS credentials: {e}")
            self._session = None

        self._clients = {}


    def get_client(self, service_name: str, region_name: str = None):
        """
        Get an AWS client for a specific service.

        Args:
            service_name: Name of the AWS service (S3, Lambda, DynamoDB, ...)
            region_name: Optional region to override default. If none, use default region.
        """

        if self._session is None:
            print("[ERROR] No valid boto3 session variable.")
            return None

        region = region_name or self._default_region_name

        cache_key = f"{service_name}-{region}"

        if cache_key in self._clients:
            return self._clients[cache_key]

        try:
            client = self._session.client(service_name, region_name = region)
            self._clients[cache_key] = client
            return client

        except Exception as e:
            print(f"[ERROR] Failed to create AWS client for {service_name} in region {region}: {e}")
            return None







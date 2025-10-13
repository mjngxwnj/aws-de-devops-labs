variable "aws_region" {
  description = "AWS region for the resources"
  type        = string
  default     = "ap-southeast-1"
}

variable "state_bucket_name" {
  description = "Name of the S3 bucket for Terraform state (huynhthuan + S3name)"
  type        = string
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for state locking (huynhthuan + dynamodbname)"
  type        = string
}

variable "project" {
  description = "The project name to use for unique resource naming"
  type        = string
}

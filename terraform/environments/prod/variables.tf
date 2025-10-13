variable "aws_region" {
  description = "Region to deploy resources"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket name for services"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

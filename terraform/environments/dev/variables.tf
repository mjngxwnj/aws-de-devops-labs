variable "aws_region" {
  description = "Region to deploy resources"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket name for services"
  type        = string
}

variable "tags" {
  description = "A map of tags to apply to resources"
  type        = map(string)
}

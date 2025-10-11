#AWS provider
provider "aws" {
  region = var.aws_region
}

#S3 bucket for Terraforms state
resource "aws_s3_bucket" "terraform_state" {
  bucket = var.state_bucket_name

  #versioning to keep a history of state files
  versioning {
    enabled = true
  }
}

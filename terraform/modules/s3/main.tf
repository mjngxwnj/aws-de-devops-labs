provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "huynhthuan_bucket" {
  bucket = var.bucket_name
  acl    = var.acl

  versioning {
    enabled = var.versioning
  }

  tags = var.tags
}

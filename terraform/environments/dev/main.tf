terraform {
  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}

module "dev-s3-database" {
  source      = "../../modules/s3"
  bucket_name = var.s3_bucket_name
  tags        = var.tags
}

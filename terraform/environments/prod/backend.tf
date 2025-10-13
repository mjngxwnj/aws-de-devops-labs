terraform {
  backend "s3" {
    bucket = "huynhthuan-tfstate"
    key    = "production/terraform.tfstate"
    region = "ap-southeast-1"
    dynamodb_table = "huynhthuan-locks"
    encrypt = true
  }
}

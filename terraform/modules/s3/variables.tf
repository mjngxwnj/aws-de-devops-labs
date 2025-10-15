#Require root module provide
variable "bucket_name" {
  description = "Name of the S3 bucket for data storage"
  type    = string
}

variable "tags" {
  description = "A map of tags to assign to the bucket"
  type    = map(string)
}


#Optional, has default value
variable "acl" {
  description = "Access control list for the bucket"
  type    = string
  default = "private"
}

variable "versioning" {
  description = "Enable versioning for the bucket"
  type    = bool
  default = true
}

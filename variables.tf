variable "aws_access_key_id" {
  description = "AWS acces key id"
}

variable "aws_secret_access_key" {
  description = "AWS secret access key"
}

variable "aws_region" {
  description = "AWS region"
}

variable "environment" {
  default     = "dev"
  description = "The environment in which the project is running."
  type        = string
}


variable "ami" {
    type = string
    default = "ami-0aa7d40eeae50c9a9"
}

variable "instance_type" {
    type = string
    default = "t2.micro"
}
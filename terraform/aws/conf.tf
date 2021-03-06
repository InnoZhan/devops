terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
  profile = "default"
}

resource "aws_instance" "my_app" {
  ami = "ami-0b9064170e32bde34"
  instance_type = "t2.micro"

  tags = {
    Name = "Python applications"
  }
}

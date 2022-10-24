terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}


provider "aws" {
  profile = "default"
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-03d5c68bab01f3496"
  instance_type = "t2.micro"
  key_name = "IaC-V"
  tags = {
    Name = "Terraform Ansible Python"
  }
}

resource "aws_key_pair" "keySSH" {
  key_name = "IaC-V"
  public_key = file("IaC-V.pub")
  
}

output "public_IP" {
  value = aws_instance.app_server.public_ip
}
resource "aws_dynamodb_table" "signups" {
  name           = "signups"
  billing_mode   = "PROVISIONED"
  read_capacity  = 10
  write_capacity = 10
  hash_key       = "user_id"

  attribute {
    name = "user_id"
    type = "S"
  }

}


resource "aws_dynamodb_table" "sessions" {
  name           = "sessions"
  billing_mode   = "PROVISIONED"
  read_capacity  = 3
  write_capacity = 3
  hash_key       = "session_id"

  attribute {
    name = "session_id"
    type = "S"
  }

}


resource "aws_instance" "fake_social" {
  ami           = var.ami
  instance_type = var.instance_type
  security_groups = [aws_security_group.allow_all_ob.name]
  tags = {
    Name = "fake_social"
  }

}


resource "aws_security_group" "allow_all_ob" {
  name        = "allow_all_ob"
  description = "Allow all OB traffic"

  #Allow all ob traffic
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  #Allow ssh from my ip
  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  

  tags = {
    Name = "allow_all_ob"
  }
}
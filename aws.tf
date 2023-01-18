resource "aws_dynamodb_table" "signups" {
  name           = "signups"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "user_id"

  attribute {
    name = "user_id"
    type = "S"
  }

}


resource "aws_dynamodb_table" "sessions" {
  name           = "sessions"
  billing_mode   = "PROVISIONED"
  read_capacity  = 30
  write_capacity = 30
  hash_key       = "session_id"

  attribute {
    name = "session_id"
    type = "S"
  }

}
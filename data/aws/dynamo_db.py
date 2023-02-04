import boto3
from boto3.dynamodb.conditions import Attr

class DynamoDB:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')


    def get_table(self, table_name):
        table = self.dynamodb.Table(table_name)
        return table
    
    
    def insert_into_table(self, table, obj):
        table.put_item(Item=obj)
        print("Object loaded to dynamo table.")


    def dump_table(self, table):
        results = []
        last_evaluated_key = None
        while True:
            if last_evaluated_key:
                response = table.scan(
                    ExclusiveStartKey=last_evaluated_key,
                    FilterExpression=Attr('session_eligible').eq(True)
                )
            else: 
                response = table.scan(
                    FilterExpression=Attr('session_eligible').eq(True)
                )
            last_evaluated_key = response.get('LastEvaluatedKey')
            
            results.extend(response['Items'])
            
            if not last_evaluated_key:
                break

        return results

    def update_session_eligible(self, user_id, table):

        table.update_item(
             Key={'user_id': user_id},
             UpdateExpression='SET session_eligible = :s',
             ExpressionAttributeValues={
                ':s': False
             }
        )
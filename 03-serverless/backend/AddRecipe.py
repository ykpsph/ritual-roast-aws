import json
import uuid
import boto3
from datetime import datetime

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb",  region_name="eu-west-2")
table = dynamodb.Table("recipes")  # <-- Replace "Recipes" with your table name

def lambda_handler(event, context):
    try:
        if "body" in event and isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event

        recipe_id = str(uuid.uuid4())

        item = {
            "id": recipe_id,
            "name": body.get("name"),
            "email": body.get("email"),
            "recipe_name": body.get("recipe_name"),
            "description_main": body.get("description_main"),
            "ingredients": body.get("ingredients"),
            "created_at": datetime.utcnow().isoformat()
        }
        
        # Insert into DynamoDB
        table.put_item(Item=item)

        return {
            "statusCode": 200,
             "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                'Content-Type': 'application/json'
            },
            "body": json.dumps({
                "message": "Recipe added successfully",
                "recipe_id": recipe_id
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

import boto3
import json

dynamodb = boto3.resource("dynamodb", region_name="eu-west-2")
table = dynamodb.Table("recipes")

def lambda_handler(event, context):
    try:
        response = table.scan()  
        items = response.get("Items", [])
        recipes = []
        for row in items:
            recipe = {
                "name": row.get("name"),
                "recipe": row.get("recipe_name"),
                "ingredients": row.get("ingredients"),
                "description": {
                    "main": row.get("description_main"),
                    "nutrition": row.get("description_nutrition")
                }
            }
            recipes.append(recipe)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(recipes)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

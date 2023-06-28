import json


def get_streak_data(event, context):
    body = {
        "message": "Get Streak data API Invoked",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def delete_streak_data(event, context):
    body = {
        "message": "Delete Streak data API Invoked",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def update_streak_data(event, context):
    body = {
        "message": "Update Streak data API Invoked",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

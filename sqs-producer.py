import boto3
import json

sqs_client = boto3.client("sqs", region_name="us-east-1")

queue_name = 'cinema-queue'

def get_queue():
    queue = sqs_client.get_queue_url(QueueName=queue_name)
    return queue["QueueUrl"]

def send_message():
    queue = get_queue()

    message = {"1": "Alto filmao hoje"}

    response = sqs_client.send_message(
        QueueUrl=queue,
        MessageBody=json.dumps(message)
    )

    print(response)

if __name__ == '__main__':
    send_message()

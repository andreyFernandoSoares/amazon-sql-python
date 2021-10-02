import boto3

sqs = boto3.resource('sqs')

queue_name = 'cinema-queue'

def get_queue():
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    return queue

def receive_messages():
    queue = get_queue()

    messages = queue.receive_messages(
        MessageAttributeNames=['All'],
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )

    for msg in messages:
        print(msg.body)

if __name__ == '__main__':
    receive_messages()

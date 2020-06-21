import argparse, sys, logging
from transformers import pipeline
import boto3

# supress warning message from pipeline
logging.disable(sys.maxsize)

def main(question, context, item_id):

    nlp = pipeline("question-answering")
    answer = nlp(question=question, context=context)

    # get the table name
    ssm_client = boto3.client("ssm")
    table_name = ssm_client.get_parameter(Name="TABLE_NAME")["Parameter"]["Value"]

    # store answer in DynamoDB
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)
    resp = table.put_item(
        Item={
            "item_id": item_id,
            "context": context,
            "question": question,
            "score": str(answer["score"]),
            "answer": answer["answer"],
        }
    )

    print(answer)
    print(resp)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("context", type=str)
    parser.add_argument("question", type=str)
    parser.add_argument("item_id", type=str)
    args = parser.parse_args()
    main(args.context, args.question, args.item_id)

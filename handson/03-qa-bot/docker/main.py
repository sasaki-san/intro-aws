import argparse, sys, logging
from transformers import pipeline
from decimal import Decimal
import boto3

# supress warning message from pipeline
logging.disable(sys.maxsize)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("context", type=str)
    parser.add_argument("question", type=str)
    parser.add_argument("item_id", type=str)
    args = parser.parse_args()

    nlp = pipeline("question-answering")
    answer = nlp(question=args.question, context=args.context)

    # get the table name
    ssm_client = boto3.client("ssm")
    table_name = ssm_client.get_parameter(Name="TABLE_NAME")["Parameter"]["Value"]

    # store answer in DynamoDB
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)
    resp = table.put_item(
        Item={
            "item_id": args.item_id,
            "context": args.context,
            "question": args.question,
            "score": Decimal(answer["score"]),
            "start": int(answer["start"]),
            "end": int(answer["end"]),
            "answer": answer["answer"],
        }
    )

    print(answer)
    print(resp)

if __name__ == "__main__":
    main()

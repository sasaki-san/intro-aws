import argparse, sys, logging
from transformers import pipeline

# supress warning message from pipeline
logging.disable(sys.maxsize)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("context", type=str)
    parser.add_argument("question", type=str)
    args = parser.parse_args()

    nlp = pipeline("question-answering")
    print(nlp(question=args.question, context=args.context))

if __name__ == "__main__":
    main()

"""
🧠 smart_data_labeler.py — Classifies and tags raw input using basic NLP and keyword matching.
"""
import argparse
import json

def label_data(input_text):
    tags = []
    if any(word in input_text.lower() for word in ["bug", "error", "issue"]):
        tags.append("technical_problem")
    if any(word in input_text.lower() for word in ["feature", "request"]):
        tags.append("feature_request")
    if "thank you" in input_text.lower():
        tags.append("positive_feedback")
    return tags

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', required=True, help='Text to label')
    args = parser.parse_args()
    result = label_data(args.text)
    print(json.dumps({"tags": result}, indent=2))

if __name__ == '__main__':
    main()

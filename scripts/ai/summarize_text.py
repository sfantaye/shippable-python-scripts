# scripts/ai/summarize_text.py

import openai
import argparse
import json

# Set OpenAI API Key (you'll need to set your key here)
openai.api_key = 'your-api-key-here'

def summarize_text(input_text):
    """
    Summarizes the given input text using OpenAI's GPT-3 model.
    
    Args:
        input_text (str): Text that needs to be summarized.
    
    Returns:
        str: Summarized version of the input text.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{input_text}",
        max_tokens=150,
        temperature=0.7,
    )
    summary = response.choices[0].text.strip()
    return summary

def save_summary(input_text, output_file):
    """
    Summarizes the input text and saves the result to an output file.
    
    Args:
        input_text (str): Text to summarize.
        output_file (str): Path to the file where the summary will be saved.
    """
    summary = summarize_text(input_text)
    with open(output_file, 'w') as file:
        file.write(summary)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Summarize text using OpenAI GPT')
    parser.add_argument('--input', required=True, help='Text to summarize')
    parser.add_argument('--output', required=True, help='Path to output summary')
    
    args = parser.parse_args()
    
    save_summary(args.input, args.output)
    print(f"Summary saved to {args.output}")


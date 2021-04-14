import boto3
import json
import urllib
import os
from spellchecker import SpellChecker

spell = SpellChecker()

ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
REGION_NAME = "us-west-2"

# Amazon Textract client
textract = boto3.client('textract', aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY,
                        region_name=REGION_NAME)


def read_file(f):
    with open(f) as json_file:
        data = json.load(json_file)
    return (data['urls'])


def download_file(url):
    file_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, file_name)
    return file_name


def check_spelling(word):
    misspelled = spell.unknown([word])
    if len(misspelled) > 0:
        return spell.correction(word)
    else:
        return (word)


def run_textract(im):
    documentText = ""
    found_words = []
    with open(im, 'rb') as document:
        imageBytes = bytearray(document.read())
    response = textract.detect_document_text(Document={'Bytes': imageBytes})
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            documentText = documentText + item["Text"]
            phrase = item["Text"].split()
            for p in phrase:
                found_words.append(p)
    return found_words


def spellCheck(words):
    corrected_text = []
    for fw in words:
        corr = check_spelling(fw)
        if check_spelling(fw) != 'none':
            corrected_text.append(corr)
    return (corrected_text)


if __name__ == '__main__':
    urls = read_file("images.json")
    for url in urls:
        im = download_file(url)
        words = run_textract(im)
        corrected = spellCheck(words)
        print(corrected)

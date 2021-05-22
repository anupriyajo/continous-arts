# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import json
import urllib
import os

import boto3
from spellchecker import SpellChecker

spell = SpellChecker()

ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
REGION_NAME = "us-west-2"

# Amazon Textract client
textract = boto3.client(
    "textract",
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION_NAME,
)


def read_file(path):
    with open(path) as json_file:
        data = json.load(json_file)

    return data["urls"]


def download_file(file_url):
    file_name = file_url.split("/")[-1]
    urllib.request.urlretrieve(file_url, file_name)

    return file_name


def check_spelling(word):
    misspelled = spell.unknown([word])

    return spell.correction(word) if misspelled else word


def run_textract(image):
    document_text = ""
    found_words = []

    with open(image, "rb") as document:
        image_bytes = bytearray(document.read())

    response = textract.detect_document_text(Document={"Bytes": image_bytes})

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            document_text = document_text + item["Text"]
            found_words += item["Text"].split()

    return found_words


def spell_check(words):
    corrected_text = []

    for word in words:
        corr = check_spelling(word)

        if check_spelling(word) != "none":
            corrected_text.append(corr)

    return corrected_text


if __name__ == "__main__":
    urls = read_file("images.json")

    for url in urls:
        im = download_file(url)
        all_words = run_textract(im)
        corrected = spell_check(all_words)
        print(corrected)

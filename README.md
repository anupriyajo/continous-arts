# Continous-Arts


This is a simple project demoing the use of a [CI](https://en.wikipedia.org/wiki/Continuous_integration) tool and a machine learning program.

### The program
- Given a list of image URLs: `images.json`.
- The images are downloaded concurrently into a folder `output`.
- The images passed through [tesseract](https://github.com/tesseract-ocr/tesseract) to perform optical character recognition.
- The results are collected in a file `extracted.json`.
- The finished artifact can be downloaded as a zip from the GitHub Actions [page](https://github.com/anupriyajo/continous-arts/actions).

### Running locally
- Python 3.7+ is installed
- [tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html) is installed
- Run `python3 main.py` to obtain the output in a dir: `output`
- Customize the urls in the `images.json` to affect the images being downloaded.

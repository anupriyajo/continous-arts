# Continuous-Arts Example


This is a simple project demoing the use of a [CI](https://en.wikipedia.org/wiki/Continuous_integration) tool and a machine learning program.

### The program
- Given a list of image URLs: `images.json`.
- The images are downloaded.
- The images passed through aws textract to perform optical character recognition.
- The results are printed on the console.

### Running locally
- Python 3.7+ is installed
- Create a virtual env
- Run `pip install -r requirements.txt` to install the dependencies
- Run `python3 main.py` to obtain the output in the console
- Customize the urls in the `images.json` to affect the images being downloaded

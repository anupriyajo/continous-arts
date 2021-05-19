# Continuous-Arts Example


This is an example repo to demonstrate the use of a [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) toolkit based on a machine learning program, as described in James Coupe's article [A Continuous Integration Toolkit for Artists](https://thoughtworksarts.io/blog/continuous-integration-toolkit-for-artists/).

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

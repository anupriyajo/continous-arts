# Continuous-Arts Example

This is an example to demonstrate the use of a [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) toolkit based on a machine learning program, as described in James Coupe's article [A Continuous Integration Toolkit for Artists](https://thoughtworksarts.io/blog/continuous-integration-toolkit-for-artists/).

This is a Python program which is to be run using the links provided in the `images.json`. This uses Amazon [Textract](https://aws.amazon.com/textract/) to perform [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) on the downloaded images and outputs the recognized text in the console.

This is primarily intended to be run in a [CI](https://en.wikipedia.org/wiki/Continuous_integration) pipeline, but can also be executed locally
to check and verify the results.

### Running locally

A Linux or MacOS is assumed.

- Make sure [Python](https://www.python.org/downloads/) 3.7+ is installed
- Create a directory `~/.virtualenvs`
- Create a virtual environment called `arts` for example. Run `python3 -m venv ~/.virtualenvs/arts` to create it
- Switch to it by running `source ~/.virtualenvs/arts/bin/activate`
- Set 2 environment variables to be able to use AWS Textract: (see [this](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds) to make a key pair)
  - `AWS_ACCESS_ID`: The ID of the access key
  - `AWS_SECRET_KEY`: The secret of the key
- Run `pip install -r requirements.txt` to install the dependencies
- Run `python3 main.py` to obtain the output in the console
- Customize the urls in the `images.json` to affect the images being downloaded

### Seeing the CI Runs
This project uses GitHub [Actions](https://github.com/features/actions) as the CI and it used pre-configured AWS credentials to connect to AWS and perform the OCR.

The status of the last pipeline runs can be viewed [here](https://github.com/thoughtworksarts/continuous-arts/actions)

To execute the runs on your own, you can fork this repo and you would get your own copy of the pipeline and can set your own AWS variables and should be triggered via pushing more commit to your repo.

# Google Scholar to JSON cloud function

Bit of code designed to run as a Google Cloud Function. It will grab a scholar profile and 
pull out the citation statistics which will be returned as JSON.

## Usage

Deploy as a Google Cloud Function (the target should be parse_scholar), you can get the data by going to the url and 
including a user argument with the Google Scholar ID to grab.

```text
https://<URL_TO_FUNCTION>/?user=<USER_ID>
```

## Testing Locally

Create a virtual environment and install the requirements from ```requirements.dev.txt```.

```shell
# Execute in same folder as code
python -m venv venv
souce venv/bin/activate
pip install -r requirements.dev.txt
```

This will install all dependencies and the function framework, you can now run the function locally using :

```shell
functions-framework --target parse_scholar --debug
```

You can now check if it works by pointing your browser to e.g.
[http://localhost:8080/?user=4niBmJUAAAAJ](http://localhost:8080/?user=4niBmJUAAAAJ) .


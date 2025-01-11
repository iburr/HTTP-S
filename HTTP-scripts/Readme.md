# Curated Python Scripts for HTTP POST and GET Requests

## Overview
This repository contains a collection of Python scripts designed for handling HTTP POST and GET requests. These scripts are ideal for web interaction, API interaction, and automation of tasks. They are modular, reusable, and optimized for efficient data handling.
** Made for Educational purposes. **

## Features
- **HTTP Request Automation**: Easily send POST and GET requests with customizable payloads, headers, and parameters.
- **Logging**: Logs request and response details for debugging and monitoring purposes.
- **Modular Design**: Each script is modular and can be reused or extended for various use cases.
- **Library Support**: Leverages Python’s `requests` Library, I found it easier to test and use compared to pythons `urlib` library cut down a lot unnecessary syntax.
- *Optional*: For a more Verbose set of information you can use NC (netcat) to listen in on the connection of the GET/POST requests of your http/https connections, Utilizing Burp or Caido helps as well ***Also depending on your use case with the scripts.

## Refrences/Research to help curate this list
    - https://pentesterlab.com/
    - https://stackoverflow.com/
    - https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
    - https://en.wikipedia.org/wiki/Method_overriding
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE
    - https://requests.readthedocs.io/en/latest/

## Using the scripts
- Scripts are to be used for legal and safe purposes only:
    - Scripts have only been tested in safe enviorments like Pentesterlab, TryHackMe, HTB, and Vulnhub, and personal Virtual Enviorments.
- Using
    - Uncomment any of the following scripts that you need to for a GET or POST Requests
    - Make sure to edit URL variables value before excution so there is no confliction with the website url you are attempting to run tests on. 

## Requirements
- Python 3.8+
- Libraries:
  - `requests`
  - (Add any other libraries used)

Install the required libraries using:
```bash
You can use pip install or uv install depending how you like to manage your depedencies/packages.
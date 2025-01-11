#!/usr/bin/env python3
import urllib.request

'''Orginally tried giving urlib a shot for simple get requests but decided to stick to requests, you may use this an optional
    on differences between urlib and requests libraries'''

# Define the base URL and parameters
base_url = "http://ptl-ac422e9c-29ada5f4.libcurl.so/pentesterlab"
parameters = "?key=please"

# Combine the URL and parameters
url = base_url + parameters

# Send the GET request
response = urllib.request.urlopen(url)

# Display the HTTP status code
print(f"HTTP Status Code: {response.getcode()}")

# Display the headers
print("\nResponse Headers:")
for key, value in response.getheaders():
    print(f"{key}: {value}")

# Read and decode the response body
print("\nResponse Body:")
contents = response.read()
print(contents.decode('utf-8'))  # Decoding the body for readability

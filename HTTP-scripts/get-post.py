#!/usr/bin/env python3

'''The following scripts were last used for the platform pentesterlab, you may need to make adjustments to the follwing
    header and url variables. '''

import requests

'''Use script below for cookies'''

# url = "http://ptl-f96c67ae-86627b39.libcurl.so/pentesterlab"
# cookies = {"key": "please"}

# response = requests.get(url, cookies=cookies)
# print(response.text)

'''Use script below for content-type'''

# url = "http://ptl-f63495f8-9159094c.libcurl.so/pentesterlab"
# headers = {
#     "Content-type" : "key/please"
# }


# response = requests.get(url, headers=headers)
# print(response.text)


# response_dir = "\n".join(dir(response))  # Join attributes with a newline
# print(f"The response dir:\n{response_dir}")

# print("\nThe response dir:")
# response_dir = dir(response)
# for i, item in enumerate(response_dir, start=1):
#     print(f"{i}. {item}")

'''Use for the Accept-language'''

# url = "https://ptl-a081e6fd-42b79525.libcurl.so/pentesterlab"
# headers = {
#     "Accept-language" : "key-please"
# }

# response = requests.get(url, headers=headers)
# print(response.text)

'''Use for HTTP-Overide methods with custom headers, may need to change custom header depending on use.
   Also useful for other http methods like X-Forwarded-For, X-Forwarded-Host. Just edit the headers method if needed.'''

url = "http://scanme.nmap.org/"
headers = {"X-HTTP-Method-Override": "PUT"}
# Can use content type optionally if you want, just enter the following alongside in the header
# "Content-type: example"

response = requests.get(url, headers=headers)
print(f"Response:\n{response.text}")


# You will need to install (if your sys does not have it) the json library
'''POST request with JSON and Escape sequence'''

# url = "example.com"
# json_data = {
#     "key": "example\""
# }

# response = requests.post(url, json=json_data)
# print(f"Repsonse:\n{response.text}")

'''POST Request with YAML content'''

# def yaml_post(url, yaml_data, headers):
#     response = requests.post(url, data=yaml_data, headers=headers)
#     print(response.status_code, response.text)

# # Example usage
# yaml_post()

'''POST Requests with multiple params'''
# Structured the same way for GET requests just change the requests from post to get 
# def post_multi(url, params):
#     response = requests.post(url, data=params)
#     print(response.status_code, response.text)

# # Example usage
# post_multi("example.com", {
#     "Key": ["example", "example"]
# })

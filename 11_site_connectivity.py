# Project 11
# Site Connectivity Checker

import urllib.request as urllib

def main(url):
    print("Checking...")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("Response code:", response.getcode())
    # if response code is 200, then it means that its successfully connected

print("Site Connectivity Checker Program")
input_url = input("Enter the url: ")

main(input_url)

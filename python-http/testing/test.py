import requests
import time

import structlog
from utils import logging as logger

def main():
    time.sleep(5)       # Sleep for 5 seconds before starting
    urls = [
        "http://service-b:8081/health",
        "http://service-b:8081/call-echo?msg=hello",
        "http://service-b:8081/call-echo?msg=hello",
        "http://service-b:8081/call-echo?msg=error",
        "http://service-b:8081/call-echo?msg=hello",
    ]
    
    for url in urls:
        response = requests.get(url)

if __name__ == "__main__":
    main()

if __name__ == "__test__":
    main()
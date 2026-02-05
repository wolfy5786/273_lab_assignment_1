from flask import Flask, request, jsonify

import requests
from requests.exceptions import Timeout, RequestException
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import time

from utils import logging as logger
import structlog


logger.configure_logging()
log = structlog.get_logger()

app = Flask(__name__)

SERVICE_A = "http://service-a:8080"


#==========================Retry logic=============================
def create_session():
    retry = Retry(
        total=3,                 # total retry attempts
        connect=3,               #  total connection attempts
        read=3,                  # number of retry attempts if no responce is heard 
        status=3,                 # max retries for status codes below
        backoff_factor=0.2,       # delay before next rery 0.2s, 0.4s, 0.8s
        status_forcelist=[500, 502, 503, 504],  #allowed retry on these responce code 5xx are server errors
        allowed_methods=["GET"],    #allow retry on which methods
        raise_on_status=False,      #setting true will result in rasing exception upon receiving error responce code
    )

    adapter = HTTPAdapter(max_retries=retry)

    session = requests.Session()    #creates connection alive
    session.mount("http://", adapter)   
    session.mount("https://", adapter)
    return session


http = create_session()




@app.get("/health")
def health():
    """health endpoint return status ok if running"""
    log.info("service b, endpoint = /health status = ok")
    return jsonify(status="ok")

@app.get("/call-echo")
def call_echo():
    """api end point call-echo, accepted param => ?msg, return json output"""
    #-------------------------start clock--------------------------------------
    start = time.time()
    #-------------------------fetch params-------------------------------------
    msg = request.args.get("msg", "")
    try:
        r = http.get(f"{SERVICE_A}/echo", params={"msg": msg}, timeout=(0.5, 1.0))
        r.raise_for_status()    # check for HTTP error
        data = r.json()         # convert to json format
        #--------------------------------------log result------------------------------------------
        log.info(f'service=B endpoint=/call-echo status=ok latency_ms={int((time.time()-start)*1000)}')
        return jsonify(service_b="ok", service_a=data)
    except Timeout:
         #------------------------------log Timeout--------------------------------------
        log.ecxception(f'service=B endpoint=/call-echo status= Timeout_exception, error="{str(re)}" latency_ms={int((time.time()-start)*1000)}')
        return jsonify(
            service_b="ok",
            service_a="unavailable",
            error="service A timeout")  ,    503
    except RequestException as re:
        #------------------------------log exception--------------------------------------
        log.exception(f'service=B endpoint=/call-echo status=request_exception, error="{str(re)}" latency_ms={int((time.time()-start)*1000)}')
        return jsonify(
            service_b="bad request",
            service_a="available",
            error=str(re))   ,   503
    except Exception as e:
        #------------------------------log exception--------------------------------------
        log.exception(f'service=B endpoint=/call-echo status=exception raised, error="{str(e)}" latency_ms={int((time.time()-start)*1000)}')
        return jsonify(
            service_b="working",
            service_a="not available",
            error=str(e))   ,   503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

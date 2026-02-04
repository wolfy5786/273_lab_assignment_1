from flask import Flask, request, jsonify
import time
import requests
import utils.logging as logger
import structlog

logger.configure_logging()
log = structlog.get_logger()

app = Flask(__name__)

SERVICE_A = "http://127.0.0.1:8080"

@app.get("/health")
def health():
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
        r = requests.get(f"{SERVICE_A}/echo", params={"msg": msg}, timeout=(0.5, 1.0))
        r.raise_for_status()    # check for HTTP error
        data = r.json()         # convert to json format
        #--------------------------------------log result------------------------------------------
        log.info(f'service=B endpoint=/call-echo status=ok latency_ms={int((time.time()-start)*1000)}')
        return jsonify(service_b="ok", service_a=data)
    except Exception as e:
        #------------------------------log exception--------------------------------------
        log.exception(f'service=B endpoint=/call-echo status=error error="{str(e)}" latency_ms={int((time.time()-start)*1000)}')
        return jsonify(service_b="ok", service_a="unavailable", error=str(e)), 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)

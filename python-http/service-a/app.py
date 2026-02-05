from flask import Flask, request, jsonify, abort
import time
import structlog
from utils import logging as logger
import random

app = Flask(__name__)

logger.configure_logging()
log = structlog.get_logger()




@app.get("/health")
def health():
    log.info("service = A endpoint = /health status = ok")
    return jsonify(status="ok")

@app.get("/echo")
def echo():
    """endpoint echo, params : ?msg msg==error for 400 error"""
    #=============================start the clock===================================
    start = time.time()
    #=============================fetch the params==================================
    msg = request.args.get("msg", "")
    
    resp = {"echo": msg}
    #============================intentionally adding delay randomly======================
    if msg=="error":
        abort(400, description="Bad request (intentional)")

    r = random.random()
    if r < 0.4:
        log.info("service A, method = /echo, intentionally causing timeout")
        time.sleep(2.0)   

    #============================log responce==============================================
    log.info(f'service=A endpoint=/echo status=ok latency_ms={int((time.time()-start)*1000)}')
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

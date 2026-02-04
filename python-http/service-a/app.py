from flask import Flask, request, jsonify
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
    #=============================start the clock===================================
    start = time.time()
    #=============================fetch the params==================================
    msg = request.args.get("msg", "")
    
    resp = {"echo": msg}
    #============================intentionally adding delay randomly======================
    r = random.random()
    if r < 0.4:
        log.info("intentionally causing timeout")
        time.sleep(2.0)   
    elif r < 0.6:
        log.info("intentionally causing causing delay")
        time.sleep(0.7) 
    #============================log responce==============================================
    log.info(f'service=A endpoint=/echo status=ok latency_ms={int((time.time()-start)*1000)}')
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

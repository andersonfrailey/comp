from flask import Blueprint, request, make_response
from celery.result import AsyncResult
from celery import chord

import redis
import json
import msgpack
import os

# import celery tasks here using the template:
# from api.celery_app.{project_name}_tasks import (
#     {project_name}_postprocess,
#     {project_name}_task)
from api.celery_app.compbaseball_tasks import (
    compbaseball_postprocess,
    compbaseball_task)

from api.celery_app.taxbrain_tasks import (
    taxbrain_postprocess,
    taxbrain_task)


bp = Blueprint('endpoints', __name__)

queue_name = "celery"
client = redis.StrictRedis.from_url(os.environ.get("CELERY_BROKER_URL",
                                                   "redis://redis:6379/0"))


def aggr_endpoint(compute_task, postprocess_task):
    print('aggregating endpoint')
    data = request.get_data()
    inputs = msgpack.loads(data, encoding='utf8',
                           use_list=True)
    print('inputs', inputs)
    result = (chord(compute_task.signature(kwargs=i, serializer='msgpack')
              for i in inputs))(postprocess_task.signature(
                serializer='msgpack'))
    length = client.llen(queue_name) + 1
    data = {'job_id': str(result), 'qlength': length}
    return json.dumps(data)


# template for app endpoints:
# @bp.route("/{project_name}", methods=['POST'])
# def {project_name}_endpoint():
#     return aggr_endpoint({project_name}_task, {project_name}_postprocess)


@bp.route("/compbaseball", methods=['POST'])
def compbaseball_endpoint():
    return aggr_endpoint(compbaseball_task, compbaseball_postprocess)


@bp.route("/taxbrain", methods=['POST'])
def taxbrain_endpoint():
    return aggr_endpoint(taxbrain_task, taxbrain_postprocess)


@bp.route("/get_job", methods=['GET'])
def results():
    job_id = request.args.get('job_id', '')
    async_result = AsyncResult(job_id)
    if async_result.ready() and async_result.successful():
        return json.dumps(async_result.result)
    elif async_result.failed():
        print('traceback', async_result.traceback)
        return async_result.traceback
    else:
        resp = make_response('not ready', 202)
        return resp


@bp.route("/query_job", methods=['GET'])
def query_results():
    job_id = request.args.get('job_id', '')
    async_result = AsyncResult(job_id)
    print('async_result', async_result.state)
    if async_result.ready() and async_result.successful():
        return 'YES'
    elif async_result.failed():
        return 'FAIL'
    else:
        return 'NO'

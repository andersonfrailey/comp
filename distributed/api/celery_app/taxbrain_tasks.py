import time

from api.celery_app import celery_app

@celery_app.task(name='taxbrain_tasks.taxbrain_task', soft_time_limit=300)
def taxbrain_task(start_year, data_source, use_full_sample, user_mods):
    start = time.time()

    #######################################
    # code snippet
    import taxcalc
    def run(start_year, data_source, use_full_sample, user_mods):
        return taxcalc.tbi.run_tbi_model(start_year, data_source,
                                         use_full_sample, user_mods)
    #######################################

    result = run(start_year, data_source, use_full_sample, user_mods)

    finish = time.time()
    elapsed = finish - start
    if "meta" in result:
        result["meta"]["task_times"] = [elapsed]
    else:
        result["meta"] = {"task_times": [elapsed]}
    print("finished result")
    return result

@celery_app.task(name='taxbrain_tasks.taxbrain_postprocess', soft_time_limit=10)
def taxbrain_postprocess(ans):
    # do nothing by default
    return ans[0]
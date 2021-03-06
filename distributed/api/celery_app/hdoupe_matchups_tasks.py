import time

from api.celery_app import celery_app


@celery_app.task(name="hdoupe_matchups_tasks.inputs_get", soft_time_limit=10)
def inputs_get(**kwargs):
    start = time.time()

    #######################################
    # code snippet
    import matchups

    def package_defaults(**meta_parameters):
        return matchups.get_inputs(use_full_data=meta_parameters["use_full_data"])

    #######################################

    return package_defaults(**kwargs)


@celery_app.task(name="hdoupe_matchups_tasks.inputs_parse", soft_time_limit=10)
def inputs_parse(**kwargs):
    start = time.time()

    #######################################
    # code snippet
    import matchups

    def parse_user_inputs(params, jsonparams, errors_warnings, **meta_parameters):
        # parse the params, jsonparams, and errors_warnings further
        use_full_data = meta_parameters["use_full_data"]
        params, jsonparams, errors_warnings = matchups.parse_inputs(
            params, jsonparams, errors_warnings, use_full_data == use_full_data
        )
        return params, jsonparams, errors_warnings

    #######################################

    return parse_user_inputs(**kwargs)


@celery_app.task(name="hdoupe_matchups_tasks.sim", soft_time_limit=60)
def sim(**kwargs):
    start = time.time()

    #######################################
    # code snippet
    import matchups

    def run(**kwargs):
        result = matchups.get_matchup(kwargs["use_full_data"], kwargs["user_mods"])
        return result

    #######################################

    result = run(**kwargs)

    finish = time.time()
    result["meta"]["task_times"] = [finish - start]
    print("finished result")
    return result

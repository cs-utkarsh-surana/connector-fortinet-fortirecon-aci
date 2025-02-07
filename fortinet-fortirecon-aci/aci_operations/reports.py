"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


def get_reports(config: dict, params: dict) -> dict:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/reports"
    method = "GET"

    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))

    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_reports_with_iocs(config: dict, params: dict) -> dict:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/reports"+"/{0}".format(params.pop("id"))
    method = "GET"

    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))

    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
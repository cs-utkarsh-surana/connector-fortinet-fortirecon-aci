"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


def get_iocs(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)

    if params.get('report_id'):
        params["report_id"] = str(params.get('report_id')).strip('[]')
    endpoint = "/aci/{org_id}/iocs"

    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

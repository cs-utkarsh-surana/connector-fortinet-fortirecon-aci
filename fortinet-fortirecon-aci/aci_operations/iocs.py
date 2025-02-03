"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


def get_iocs(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    get_all_records = params.pop('get_all_records', None)
    if params.get('report_id'):
        params["report_id"] = str(params.get('report_id')).strip('[]')
    endpoint = "/aci/{org_id}/iocs"
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    if get_all_records:
        params.pop('page', "")
        params['size'] = 500
        response = MK.make_request(endpoint=endpoint, method="GET", params=params)
        iocs = response.get('hits', [])
        while response.get('hits'):
            params['page'] = int(params.get('page', 1)) + 1
            response = MK.make_request(endpoint=endpoint, method="GET", params=params)
            iocs.extend(response.get('hits', []))
        response['hits'] = iocs
        return response
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

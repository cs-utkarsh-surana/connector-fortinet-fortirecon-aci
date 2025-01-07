"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


def get_leaked_cards(config: dict, params: dict) -> dict:

    MK = MakeRestApiCall(config=config)
    if params.get('bin'):
        params["bin"] = str(params.get('bin')).strip('[]')
    endpoint = "/aci/{org_id}/leaked_cards"
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall


def get_vendor_watchlist(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/vendors_watchlist'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

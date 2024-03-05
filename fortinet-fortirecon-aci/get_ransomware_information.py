"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall

URL = {
    "Fetch Active Ransomware": "active",
    "Fetch Organizations Affected by Ransomware": "organization_watchlist",
    "Fetch Ransomware Summary": "summary",
    "Fetch Ransomware Trend Statistics": "trends",
    "Fetch Vendors Affected By Ransomware": "vendor_watchlist",
    "Fetch Ransomware Victim Targets": "victims"
}

MAPPING = {
    "Potential Ransomware Victims": "potential_ransomeware_victims",
    "Ransomware Victims": "ransomeware_victims"
}


def get_ransomware_information(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware' + '/{url}'.format(url=URL.get(params.get('type_of_info')))
    if params.get('category'):
        params['category'] = MAPPING.get(params.get('category'))
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

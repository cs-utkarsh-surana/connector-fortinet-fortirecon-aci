""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from .make_rest_api_call import MakeRestApiCall

URL = {
    "Attack Surface Exposure": "asm_exposure",
    "Darknet Exposure": "darknet_exposure",
    "Incidents": "incidents"
}


def get_vendor_details_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/vendors'+'/{id}'.format(id=params.pop('id'))+'/{url}'.format(url=URL.get(params.get('type_of_info'))) if params.get('type_of_info') else ""
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

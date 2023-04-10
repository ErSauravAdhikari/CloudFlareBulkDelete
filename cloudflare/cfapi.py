import http.client
import json
from typing import List
from .exceptions import ZONEIDNOTFOUND, DNSRECORDNOTFOUND, APIKEYERROR, UnknownException

def list_records(zoneid: str, apikey: str) -> List[dict]:
    conn = http.client.HTTPSConnection("api.cloudflare.com")
    payload = ""
    headers = {
        'Authorization': f"Bearer {apikey}"
        }

    conn.request("GET", f"/client/v4/zones/{zoneid}/dns_records", payload, headers)

    res = conn.getresponse()

    # Making sure that there are no erros
    # Errors can happen when ZoneID does not match
    if res.status != 200:
        # Unauthorized
        if res.status == 401:
            raise APIKEYERROR

        # Cloudflare sends 404 when there is invalid zoneid
        if res.status == 404:
            # Parsing error message
            err = json.loads(res.read().decode("utf-8"))
            if err["errors"][0]["code"] == 7003:
                raise ZONEIDNOTFOUND
            
            raise UnknownException

    else:
        data = res.read()
        records = json.loads(data.decode("utf-8"))
        return records["result"]


def delete_record(zoneid: str, dnsid: str, apikey: str):
    conn = http.client.HTTPSConnection("api.cloudflare.com")

    payload = ""

    headers = {
        'Authorization': f"Bearer {apikey}"
        }

    conn.request("DELETE", f"/client/v4/zones/{zoneid}/dns_records/{dnsid}", payload, headers)

    res = conn.getresponse()

    # Making sure that there are no erros
    # Errors can happen when ZoneID does not match and DNSID does not match
    if res.status != 200:
        # Unauthorized
        if res.status == 401:
            raise APIKEYERROR

        # Cloudflare sends 404 when there is invalid zoneid or dnsrecord id
        if res.status == 404:
            # Parsing error message
            err = json.loads(res.read().decode("utf-8"))
            if err["errors"][0]["code"] == 7003:
                raise ZONEIDNOTFOUND
            
            elif err["errors"][0]["code"] == 81044:
                raise DNSRECORDNOTFOUND

            raise UnknownException
    
    return

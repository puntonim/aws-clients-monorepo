import json
from decimal import Decimal
from typing import Collection, Optional, Union
from uuid import UUID


class ApiGatewayEventV2Factory:
    @staticmethod
    def make_for_read_version():
        data = {
            "version": "2.0",
            "routeKey": "GET /version",
            "rawPath": "/version",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-6230747b-27c4de4547db4307403594d7",
                "x-forwarded-for": "52.46.162.106",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "i35w8x7vw1",
                "domainName": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "domainPrefix": "i35w8x7vw1",
                "http": {
                    "method": "GET",
                    "path": "/version",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "52.46.162.106",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "PBcjThLMSQ0EJVA=",
                "routeKey": "GET /version",
                "stage": "$default",
                "time": "15/Mar/2022:11:11:55 +0000",
                "timeEpoch": 1647342715339,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_health():
        data = {
            "version": "2.0",
            "routeKey": "GET /health",
            "rawPath": "/health",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-6230747b-27c4de4547db4307403594d7",
                "x-forwarded-for": "52.46.162.106",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "i35w8x7vw1",
                "domainName": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "domainPrefix": "i35w8x7vw1",
                "http": {
                    "method": "GET",
                    "path": "/health",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "52.46.162.106",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "PBcjThLMSQ0EJVA=",
                "routeKey": "GET /health",
                "stage": "$default",
                "time": "15/Mar/2022:11:11:55 +0000",
                "timeEpoch": 1647342715339,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_settings():
        data = {
            "version": "2.0",
            "routeKey": "GET /settings",
            "rawPath": "/settings",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "0",
                "host": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-6230747b-27c4de4547db4307403594d7",
                "x-forwarded-for": "52.46.162.106",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "i35w8x7vw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "domainPrefix": "i35w8x7vw1",
                "http": {
                    "method": "GET",
                    "path": "/settings",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "52.46.162.106",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "PBcjThLMSQ0EJVA=",
                "routeKey": "GET /settings",
                "stage": "$default",
                "time": "15/Mar/2022:11:11:55 +0000",
                "timeEpoch": 1647342715339,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_openapi_view():
        data = {
            "version": "2.0",
            "routeKey": "GET /openapi",
            "rawPath": "/openapi",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-6230747b-27c4de4547db4307403594d7",
                "x-forwarded-for": "52.46.162.106",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "i35w8x7vw1",
                "domainName": "i35w8x7vw1.execute-api.ap-southeast-1.amazonaws.com",
                "domainPrefix": "i35w8x7vw1",
                "http": {
                    "method": "GET",
                    "path": "/openapi",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "52.46.162.106",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "PBcjThLMSQ0EJVA=",
                "routeKey": "GET /openapi",
                "stage": "$default",
                "time": "15/Mar/2022:11:11:55 +0000",
                "timeEpoch": 1647342715339,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_read_rulebook():
        data = {
            "version": "2.0",
            "routeKey": "GET /rulebook",
            "rawPath": "/rulebook",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-638de618-00fd50855702f3865fe73553",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": "/rulebook",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "crDjzgBQoAMEMcw=",
                "routeKey": "GET /rulebook",
                "stage": "$default",
                "time": "05/Dec/2022:12:37:44 +0000",
                "timeEpoch": 1670243864170,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_read_attributes():
        data = {
            "version": "2.0",
            "routeKey": "GET /rulebook/attribute",
            "rawPath": "/rulebook/attribute",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-638de632-01f1381a32279257653b45e6",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": "/rulebook/attribute",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "crDn6i1hIAMEYfg=",
                "routeKey": "GET /rulebook/attribute",
                "stage": "$default",
                "time": "05/Dec/2022:12:38:10 +0000",
                "timeEpoch": 1670243890472,
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_read_operators(attribute: str):
        data = {
            "version": "2.0",
            "routeKey": "GET /rulebook/attribute/{attribute}/operator",
            "rawPath": f"/rulebook/attribute/{attribute}/operator",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-638de639-112ab57b20cb4b6a2e7d4635",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": f"/rulebook/attribute/{attribute}/operator",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "crDpFho5IAMEMBw=",
                "routeKey": "GET /rulebook/attribute/{attribute}/operator",
                "stage": "$default",
                "time": "05/Dec/2022:12:38:17 +0000",
                "timeEpoch": 1670243897994,
            },
            "pathParameters": {"attribute": f"{attribute}"},
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_validate_ruleset(
        body_list: Optional[list] = None,
        body_json: Optional[str] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "PUT /rulebook/validate-ruleset",
            "rawPath": "/rulebook/validate-ruleset",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "160",
                "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-638de676-03827d3c0ca6a87313dc2ea8",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "PUT",
                    "path": "/rulebook/validate-ruleset",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "crDykgngIAMEJ8Q=",
                "routeKey": "PUT /rulebook/validate-ruleset",
                "stage": "$default",
                "time": "05/Dec/2022:12:39:18 +0000",
                "timeEpoch": 1670243958635,
            },
            # "body": json.dumps(body_list),
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_list is not None:
            body = json.dumps(body_list)
        elif body_json is not None:
            body = body_json
        if body is not None:
            data["body"] = body
        return data

    @staticmethod
    def make_for_read_all_odd_definitions(next_page_token: Optional[str] = None):
        data = {
            "version": "2.0",
            "routeKey": "GET /odd-definition",
            "rawPath": "/odd-definition",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637ddca4-4cad5ea74c90fa874c489c83",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": "/odd-definition",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cC9pthbbIAMEcFA=",
                "routeKey": "GET /odd-definition",
                "stage": "$default",
                "time": "23/Nov/2022:08:41:08 +0000",
                "timeEpoch": 1669192868350,
            },
            "isBase64Encoded": False,
        }
        if next_page_token:
            data["rawQueryString"] = f"next-page-token={next_page_token}"
            data["queryStringParameters"] = {"next-page-token": next_page_token}

        return data

    @staticmethod
    def make_for_read_one_odd_definition(uuid: Union[str, UUID]):
        data = {
            "version": "2.0",
            "routeKey": "GET /odd-definition/{uuid}",
            "rawPath": f"/odd-definition/{uuid}",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637dccd3-6ad9ae4d1a98c7ff4fefd556",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": f"/odd-definition/{uuid}",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cCzxEiLyIAMEVlw=",
                "routeKey": "GET /odd-definition/{uuid}",
                "stage": "$default",
                "time": "23/Nov/2022:07:33:39 +0000",
                "timeEpoch": 1669188819493,
            },
            "pathParameters": {
                "uuid": str(uuid),
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_create_odd_definition(
        body_dict: Optional[dict] = None,
        body_json: Optional[str] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "POST /odd-definition",
            "rawPath": "/odd-definition",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "67",
                # "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637dcd53-40fc13695e4f32fb35a45659",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "POST",
                    "path": "/odd-definition",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cC0FHgCmIAMEJBg=",
                "routeKey": "POST /odd-definition",
                "stage": "$default",
                "time": "23/Nov/2022:07:35:47 +0000",
                "timeEpoch": 1669188947757,
            },
            # "body": body,
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_dict is not None:
            body = json.dumps(body_dict)
        elif body_json is not None:
            body = body_json
        if body is not None:
            data["body"] = body
        return data

    @staticmethod
    def make_for_update_odd_definition(
        uuid: Union[str, UUID],
        body_dict: Optional[dict] = None,
        body_json: Optional[str] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "PUT /odd-definition/{uuid}",
            "rawPath": f"/odd-definition/{uuid}",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "76",
                "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-6383156c-0bc6dbc86d3addb9394c1b92",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "PUT",
                    "path": f"/odd-definition/{uuid}",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "cQBJBjNxIAMEcWA=",
                "routeKey": "PUT /odd-definition/{uuid}",
                "stage": "$default",
                "time": "27/Nov/2022:07:44:44 +0000",
                "timeEpoch": 1669535084736,
            },
            "pathParameters": {"uuid": uuid},
            # "body": body,
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_dict is not None:
            body = json.dumps(body_dict)
        elif body_json is not None:
            body = body_json
        if body is not None:
            data["body"] = body
        return data

    @staticmethod
    def make_for_read_all_rules_for_odd_definition(
        uuid: Union[str, UUID], next_page_token: Optional[str] = None
    ):
        data = {
            "version": "2.0",
            "routeKey": "GET /odd-definition/{uuid}/ruleset",
            "rawPath": f"/odd-definition/{uuid}/ruleset",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-63888fde-0b4fc6e2787b3630140bcecb",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": f"/odd-definition/{uuid}/ruleset",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "cdtq3iy6IAMEVlA=",
                "routeKey": "GET /odd-definition/{uuid}/ruleset",
                "stage": "$default",
                "time": "01/Dec/2022:11:28:30 +0000",
                "timeEpoch": 1669894110930,
            },
            "pathParameters": {
                "uuid": str(uuid),
            },
            "isBase64Encoded": False,
        }
        if next_page_token:
            data["rawQueryString"] = f"next-page-token={next_page_token}"
            data["queryStringParameters"] = {"next-page-token": next_page_token}
        return data

    @staticmethod
    def make_for_create_rules_for_odd_definition(
        uuid: Union[str, UUID],
        body_dict: Optional[dict] = None,
        body_json: Optional[str] = None,
        rules_data: Optional[Collection[dict]] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "PUT /odd-definition/{uuid}/ruleset",
            "rawPath": f"/odd-definition/{uuid}/ruleset",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "167",
                "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-6388d575-46fed8de4ee5b4d012a7793a",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "PUT",
                    "path": f"/odd-definition/{uuid}/ruleset",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "ceZKZhm0oAMEbgw=",
                "routeKey": "PUT /odd-definition/{uuid}/ruleset",
                "stage": "$default",
                "time": "01/Dec/2022:16:25:25 +0000",
                "timeEpoch": 1669911925513,
            },
            "pathParameters": {"uuid": str(uuid)},
            # "body": body,
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_dict is not None:
            body = json.dumps(body_dict)
        elif body_json is not None:
            body = body_json
        elif rules_data:
            rules = []
            for rule_item in rules_data:
                rule = {}
                if "attribute" in rule_item:
                    rule["attribute"] = getattr(
                        rule_item.get("attribute"), "value", rule_item.get("attribute")
                    )
                if "operator_id" in rule_item:
                    rule["operatorId"] = getattr(
                        rule_item.get("operator_id"),
                        "value",
                        rule_item.get("operator_id"),
                    )
                if "value" in rule_item:
                    value = rule_item["value"]
                    if isinstance(value, Decimal):
                        value = str(value)
                    rule["value"] = value
                rules.append(rule)
            body = json.dumps(rules)
        if body is not None:
            data["body"] = body
        return data

    @staticmethod
    def make_for_read_all_annotation_overrides(next_page_token: Optional[str] = None):
        data = {
            "version": "2.0",
            "routeKey": "GET /annotation-override",
            "rawPath": "/annotation-override",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637ddca4-4cad5ea74c90fa874c489c83",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": "/annotation-override",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cC9pthbbIAMEcFA=",
                "routeKey": "GET /annotation-override",
                "stage": "$default",
                "time": "23/Nov/2022:08:41:08 +0000",
                "timeEpoch": 1669192868350,
            },
            "isBase64Encoded": False,
        }
        if next_page_token:
            data["rawQueryString"] = f"next-page-token={next_page_token}"
            data["queryStringParameters"] = {"next-page-token": next_page_token}

        return data

    @staticmethod
    def make_for_read_one_annotation_override(uuid: Union[str, UUID]):
        data = {
            "version": "2.0",
            "routeKey": "GET /annotation-override/{uuid}",
            "rawPath": f"/annotation-override/{uuid}",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "0",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637dccd3-6ad9ae4d1a98c7ff4fefd556",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "GET",
                    "path": f"/annotation-override/{uuid}",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cCzxEiLyIAMEVlw=",
                "routeKey": "GET /annotation-override/{uuid}",
                "stage": "$default",
                "time": "23/Nov/2022:07:33:39 +0000",
                "timeEpoch": 1669188819493,
            },
            "pathParameters": {
                "uuid": str(uuid),
            },
            "isBase64Encoded": False,
        }
        return data

    @staticmethod
    def make_for_create_annotation_override(
        body_dict: Optional[dict] = None,
        body_json: Optional[str] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "POST /annotation-override",
            "rawPath": "/annotation-override",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "67",
                # "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-637dcd53-40fc13695e4f32fb35a45659",
                "x-forwarded-for": "69.210.74.152",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "POST",
                    "path": "/annotation-override",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "69.210.74.152",
                    "userAgent": "curl/7.64.1",
                },
                "requestId": "cC0FHgCmIAMEJBg=",
                "routeKey": "POST /annotation-override",
                "stage": "$default",
                "time": "23/Nov/2022:07:35:47 +0000",
                "timeEpoch": 1669188947757,
            },
            # "body": body,
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_dict is not None:
            body = json.dumps(body_dict)
        elif body_json is not None:
            body = body_json
        if body is not None:
            data["body"] = body
        return data

    @staticmethod
    def make_for_update_annotation_override(
        uuid: Union[str, UUID],
        body_dict: Optional[dict] = None,
        body_json: Optional[str] = None,
        do_skip_json_content_type_header=False,
        content_type_header: Optional[str] = "application/json",
    ):
        data = {
            "version": "2.0",
            "routeKey": "PUT /annotation-override/{uuid}",
            "rawPath": f"/annotation-override/{uuid}",
            "rawQueryString": "",
            "headers": {
                "accept": "text/plain",
                "authorization": "Bearer ...",
                "content-length": "76",
                "content-type": "application/json",
                "host": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "user-agent": "curl/7.71.1",
                "x-amzn-trace-id": "Root=1-6383156c-0bc6dbc86d3addb9394c1b92",
                "x-forwarded-for": "151.55.93.219",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "289485838881",
                "apiId": "4b3cuvdgw1",
                "authorizer": {
                    "lambda": {
                        "scope": "read:maps write:maps write:branches openid profile email write:locations offline_access read:map-deployments write:map-deployments"
                    }
                },
                "domainName": "4b3cuvdgw1.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4b3cuvdgw1",
                "http": {
                    "method": "PUT",
                    "path": f"/annotation-override/{uuid}",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "151.55.93.219",
                    "userAgent": "curl/7.71.1",
                },
                "requestId": "cQBJBjNxIAMEcWA=",
                "routeKey": "PUT /annotation-override/{uuid}",
                "stage": "$default",
                "time": "27/Nov/2022:07:44:44 +0000",
                "timeEpoch": 1669535084736,
            },
            "pathParameters": {"uuid": uuid},
            # "body": body,
            "isBase64Encoded": False,
        }
        if not do_skip_json_content_type_header:
            data["headers"]["content-type"] = content_type_header
        body = None
        if body_dict is not None:
            body = json.dumps(body_dict)
        elif body_json is not None:
            body = body_json
        if body is not None:
            data["body"] = body
        return data

#!/usr/bin/env python
import web
from random import randint
import json
from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    "/securityConcerns", "SecurityConcerns",
    "/connectivityStatus", "ConnectivityStatus",
    "/alerts", "Alerts",
    "/users/(.*)", "User"
)
app = web.application(urls, globals())


class SecurityConcerns:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "securityConcerns",
            "data": [
                {
                    "id": "non-compliant",
                    "label": "Non Compliant",
                    "count": randint(100, 500)
                },
                {
                    "id": "no-passcode",
                    "label": "No Passcode",
                    "count": randint(100, 500)
                },
                {
                    "id": "no-encryption",
                    "label": "Non encrypted",
                    "count": randint(100, 500)
                },
                {
                    "id": "unmonitored",
                    "label": "Unmonitored",
                    "count": randint(100, 500)
                }
            ]
        }
        i = web.input();
        return json.dumps(response)

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        return True


class ConnectivityStatus:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "connectivityStatus",
            "data": [
                {
                    "id": "active",
                    "label": "Active",
                    "count": randint(100, 500)
                },
                {
                    "id": "blocked",
                    "label": "Blocked",
                    "count": randint(100, 500)
                },
                {
                    "id": "inactive",
                    "label": "Inactive",
                    "count": randint(100, 500)
                }
            ]
        }
        return json.dumps(response)

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        return True


class Alerts:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "alerts",
            "data": [
                {
                    "id": "critical",
                    "label": "Critical",
                    "count": randint(100, 500)
                },
                {
                    "id": "high",
                    "label": "High",
                    "count": randint(100, 500)
                },
                {
                    "id": "medium",
                    "label": "Medium",
                    "count": randint(100, 500)
                },
                {
                    "id": "Normal",
                    "label": "Normal",
                    "count": randint(100, 500)
                }
            ]
        }
        return json.dumps(response)

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        return True


class User:
    def GET(self, user):
        return user


if __name__ == "__main__":
    app.run()

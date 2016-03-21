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
    "/platforms", "Platforms",
    "/ownerships", "Ownerships",
    "/userGroups", "UserGroups",
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
        post_data = web.data()
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


class Alert:
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


class Platforms:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "platforms",
            "data": [
                {
                    "id": "ios",
                    "label": "iOS",
                    "count": randint(100, 500)
                },
                {
                    "id": "android",
                    "label": "Android",
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


class Ownerships:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "ownerships",
            "data": [
                {
                    "id": "cope",
                    "label": "COPE",
                    "count": randint(100, 500)
                },
                {
                    "id": "byod",
                    "label": "BYOD",
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


class UserGroups:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = {
            "filteredBy": "userGroups",
            "data": [
                {
                    "id": "sales",
                    "label": "Sales",
                    "count": randint(100, 500)
                },
                {
                    "id": "marketing",
                    "label": "Marketing",
                    "count": randint(100, 500)
                },
                {
                    "id": "engineering",
                    "label": "Engineering",
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

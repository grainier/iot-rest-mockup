#!/usr/bin/env python
import web
from random import sample, randint
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
    "/devices", "Devices",
    "/devicesCount", "DevicesCount",
    "/users/(.*)", "User"
)
app = web.application(urls, globals())


class SecurityConcerns:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        response = [
            {
                "context": "securityConcerns",
                "data": [
                    {
                        "group": "non-compliant",
                        "label": "Non Compliant",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "no-passcode",
                        "label": "No Passcode",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "no-encryption",
                        "label": "Non encrypted",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "unmonitored",
                        "label": "Unmonitored",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
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
        response = [
            {
                "context": "connectivityStatus",
                "data": [
                    {
                        "group": "active",
                        "label": "Active",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "blocked",
                        "label": "Blocked",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "inactive",
                        "label": "Inactive",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
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
        response = [
            {
                "context": "alerts",
                "data": [
                    {
                        "group": "critical",
                        "label": "Critical",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "high",
                        "label": "High",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "medium",
                        "label": "Medium",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "Normal",
                        "label": "Normal",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
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
        response = [
            {
                "context": "platforms",
                "data": [
                    {
                        "group": "ios",
                        "label": "iOS",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "android",
                        "label": "Android",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
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
        response = [
            {
                "context": "ownerships",
                "data": [
                    {
                        "group": "cope",
                        "label": "COPE",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "byod",
                        "label": "BYOD",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
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
        response = [
            {
                "context": "userGroups",
                "data": [
                    {
                        "group": "sales",
                        "label": "Sales",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "marketing",
                        "label": "Marketing",
                        "count": randint(100, 500)
                    },
                    {
                        "group": "engineering",
                        "label": "Engineering",
                        "count": randint(100, 500)
                    }
                ]
            }
        ]
        return json.dumps(response)

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        return True


class Devices:
    def POST(self):
        l = [
            {
                "id": "001",
                "label": "Nexus P",
                "status": "Blocked",
                "platform": "Android",
                "model": "HNP001",
                "actions": "Action",
            },
            {
                "id": "002",
                "label": "Galaxy Note 5",
                "status": "Unmonitored",
                "platform": "Android",
                "model": "SGN002",
                "actions": "Action",
            },
            {
                "id": "003",
                "label": "iPhone 6",
                "status": "Compliant",
                "platform": "iOS",
                "model": "AIP003",
                "actions": "Action",
            },
            {
                "id": "004",
                "label": "Galaxy S7",
                "status": "NonCompliant",
                "platform": "Android",
                "model": "SGS004",
                "actions": "Action",
            },
            {
                "id": "005",
                "label": "iPad Mini",
                "status": "Inactive",
                "platform": "iOS",
                "model": "IPM005",
                "actions": "Action",
            }
        ]
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        response = [
            {
                "context": "devices",
                "data": sample(l, randint(2, len(l)))
            }
        ]
        return json.dumps(response)

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header("Content-Type", "application/json")
        return True


class DevicesCount:
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header("Content-Type", "application/json")
        total_count = randint(200, 500)
        response = [
            {
                "context": "deviceCount",
                "data": [
                    {
                        "group": "totalCount",
                        "label": "Total Count",
                        "count": total_count
                    },
                    {
                        "group": "filteredCount",
                        "label": "Filtered Count",
                        "count": randint(100, total_count)
                    }
                ]
            }
        ]
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

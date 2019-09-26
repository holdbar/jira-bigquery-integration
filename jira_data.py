import os
import json
import requests
from requests.auth import HTTPBasicAuth


class JiraData:
    def __init__(self):
        self.jira_url = os.environ['JIRA_URL']
        self.jira_username = os.environ['JIRA_USERNAME']
        self.jira_api_token = os.environ['JIRA_API_TOKEN']

        self.url = f"{self.jira_url}/rest/api/2/search"

        self.auth = HTTPBasicAuth(username=self.jira_username, password=self.jira_api_token)

        self.params = {
            'fields': ['*all'],
            'expand': 'schema,names,transitions,operations,changelog,versionedRepresentations',
            'startAt': 0,
            'maxResults': 100
        }

    def __run_request(self):
        response = requests.request(
            "GET",
            self.url,
            headers={"Accept": "application/json"},
            params=self.params,
            auth=self.auth
        )

        return response

    def request(self):
        response = self.__run_request()
        data = json.loads(response.text)

        total_records = data['total']

        while self.params['startAt'] <= total_records:
            self.params['startAt'] += data['maxResults']
            response = self.__run_request()
            response_json = json.loads(response.text)
            data['issues'] += response_json['issues']

        return data

if __name__ == "__main__":
    data = JiraData().request()

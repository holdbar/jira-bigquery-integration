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
        self.data = {}

    def __run_request(self):
        response = requests.request(
            "GET",
            self.url,
            headers={"Accept": "application/json"},
            params=self.params,
            auth=self.auth
        )
        return response

    def get_data(self):
        response = self.__run_request()
        self.data = json.loads(response.text)

        total_records = self.data['total']

        while self.params['startAt'] <= total_records:
            self.params['startAt'] += data['maxResults']
            response = self.__run_request()
            response_json = json.loads(response.text)
            self.data['issues'] += response_json['issues']

        return self

    def make_schema(self):
        names = list(self.data['names'].values())
        names = [x.lower().replace(' ', '_') for x in names]

        return names


if __name__ == "__main__":
    jira_data = JiraData().get_data()
    print(jira_data.make_schema())

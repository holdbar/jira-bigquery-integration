# jira-bigquery-integration
Get the data from Jira API, organize it and insert to BigQuery

## Setup development environment

Using conda:
```
conda create -n yourenvname python=3.7
conda activate yourenvname
pip install -r requirements
```
Environment Variables:
```
export JIRA_URL=https://YOUR_URL.atlassian.net
export JIRA_USERNAME=YOUR_USERNAME
export JIRA_API_TOKEN=YOUR_API_TOKEN
```

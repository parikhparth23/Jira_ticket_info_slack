import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def without_id():
    error_response = {"response_type": "in_channel", "*Missing JIRA Ticket Number*": "Please enter a JIRA ticket number"}
    return jsonify(error_response)


@app.route("/<int:argv>")
def main(argv):
    mob = "JIRA PROJECT NAME-" + str(argv)
    jira_username = 'YOUR USERNAME'
    jira_password = 'YOUR PASSWORD'

    headers = {
        'Content-type': 'application/json',
    }

    url = 'JIRA URL' + mob + '?fields=summary,priority,assignee'

    r = requests.get(url,
                     headers=headers, auth=(jira_username, jira_password))

    jira_info = {"response_type": "in_channel", "*Title*: ": r.json()["fields"]["summary"], "*Priority*: ": r.json()["fields"]["priority"]["name"],
                 "*Assignee*: ": r.json()["fields"]["assignee"]["displayName"]}

    return jsonify(jira_info)


if __name__ == "__main__":
    app.run()

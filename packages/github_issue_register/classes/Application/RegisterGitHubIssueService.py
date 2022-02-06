import json

from packages.github_issue_register.classes.Domain.issue import Issue


class RegisterGitHubIssueService:
    def execute(self, url, session, issue: Issue):
        res = session.post(url, json.dumps({
            "title": issue.get_title(),
            "body": "",
            # TODO: 複数登録できるように
            "labels": [issue.get_label()],
        }))

        return res

from packages.github_issue_register.classes.Domain.issue import Issue


class IssueConverter:
    def to_issue(self,dict:dict):
        return Issue(title=dict["title"], label=dict["label"])
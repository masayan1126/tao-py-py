import io, sys
from pprint import pprint
import os
import requests
from packages.github_issue_register.classes.Application.IssueConverter import IssueConverter
from packages.github_issue_register.classes.Application.RegisterGitHubIssueService import RegisterGitHubIssueService

from shared.Domain.xcsv import XCsv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# issueのリスト(csv)を読み込み
filepath = 'C:\\Users\\nishigaki\\jupyter-lab\\packages\\github_issue_register\\issues.csv'
csv = XCsv()
issue_df = csv.read(filepath, encoding="shift-jis", header=0)

# GithubApiを叩く準備
GITHUB_USERNAME = "masayan1126"
GITHUB_REPO_OWNERNANE = "masayan1126"
GITHUB_REPO_NANE = "stocker"
# 事前にトークンを https://github.com/settings/tokens へ登録し、windowsの環境変数に追加しておくこと
GITHUB_PERSONAL_ACCESS_TOKENS = os.environ.get('GITHUB_PERSONAL_ACCESS_TOKENS')

session = requests.Session()
session.auth = (GITHUB_USERNAME, GITHUB_PERSONAL_ACCESS_TOKENS)
url = 'https://api.github.com/repos/%s/%s/issues' % (GITHUB_REPO_OWNERNANE, GITHUB_REPO_NANE)

# dfをissueオブジェクトに変換し、post
for issue_dict in issue_df.to_dict("index").values():
    issue = IssueConverter().to_issue(issue_dict)
    res = RegisterGitHubIssueService().execute(url, session,issue)

    if res.status_code == 201:
        pprint('Successfully created Issue "%s"' % issue.get_title())
    else:
        pprint('Could not create Issue "%s"' % issue.get_title())
import io, sys
from pprint import pprint
import os
import requests
from packages.github_issue_register.classes.Application.IssueConverter import (
    IssueConverter,
)
from packages.github_issue_register.classes.Application.RegisterGitHubIssueService import (
    RegisterGitHubIssueService,
)

from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr

# issueのリスト(csv)を読み込み
filepath = XFileSystemPath(
    XStr("packages/github_issue_register/issues.csv")
).to_absolute()
issue_df = XCsv().read(filepath, encoding="shift-jis", header=0)

# GithubApiを叩く準備
GITHUB_USERNAME = "masayan1126"
GITHUB_REPO_OWNERNANE = "masayan1126"
GITHUB_REPO_NANE = "tao-py-py"
# 事前にトークンを https://github.com/settings/tokens へ登録し、windowsの環境変数に追加しておくこと
# トークンには期限があるので注意
GITHUB_PERSONAL_ACCESS_TOKENS = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKENS")

session = requests.Session()
session.auth = (GITHUB_USERNAME, GITHUB_PERSONAL_ACCESS_TOKENS)
url = "https://api.github.com/repos/%s/%s/issues" % (
    GITHUB_REPO_OWNERNANE,
    GITHUB_REPO_NANE,
)

# dfをissueオブジェクトに変換し、post
for issue_dict in issue_df.to_dict("index").values():
    issue = IssueConverter().to_issue(issue_dict)
    res = RegisterGitHubIssueService().execute(url, session, issue)

    if res.status_code == 201:
        pprint('Successfully created Issue "%s"' % issue.get_title())
    else:
        pprint(res.reason)
        pprint('Could not create Issue "%s"' % issue.get_title())

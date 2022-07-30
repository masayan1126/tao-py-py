## 概要
各種作業自動化用 Python パッケージ

- 勤怠等の各種ブラウザ操作自動化
- Twitter 自動化
- WordPress 自動化
- LINE Notify による RSS 通知
- LINE Notify による Google カレンダー予定/タスク通知
- 今日の IP を通知
- その他情報収集、資料作成自動化

## 構成
- Python 3.10
- Pipenv(バージョン管理)
- Flake8, mypy(静的解析)
- Docker(Seleniumテスト用)
- Xserver(本番デプロイ先)
- pytest(単体テスト)
- CI/CD
  - GithubActions による自動 pytest および Xserver への sftp デプロイ

## 設計

- オブジェクト指向・ドメイン駆動設計
  - Domain
    - ドメインオブジェクト(・・・.py)
      - 画像、ブラウザなど
    - エンティティ(・・・.py)
    - ドメインサービス(・・・service.py)
      - ドメインオブジェクトに実装するにはやりすぎなメソッドを実装する。(※ただしユースケースほど複雑で具体的なロジックではない)
    - コマンド(・・・command.py)
  - Application
    - ユースケース(・・・usecase.py)
      - 上記ドメインクラスを使用して具体的な処理を実現する

## 使用デザインパターン

- Factory Method
  - 実際に生成するオブジェクトに依存しない、オブジェクト生成のインタフェースを提供
- Iterator

  - 集約オブジェクトを内包するオブジェクトが内部表現を公開することなく、その要素に順にアクセスする方法を提供

- Command

  - 命令・操作をクラス(オブジェクト)で表現し、そのオブジェクトを切り替えることで操作の切り替えを実現

- Strategy
  - アルゴリズム(戦略)をクラスを用いて部品化し、動的なアルゴリズムの切替えを可能とする
  <!-- - Loan -->

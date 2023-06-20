## Lambda サンプル集

### シンプルな Lambda 関数をマネジメントコンソールで作成してみよう


- マネジメントコンソールから Lambda 関数を作成
  - 関数名は `hello-world-function` を入力
  - Python 3.9 を選択
  - 実行ロールに `lambdaPollyRole` を使用します
    - ラボ環境の都合上、指定しないと進めないため指定します
- Lambda 関数のコードに [hello.py](https://github.com/shotagtag/devonaws/blob/main/samples/python/lambda/hello.py) のソースコードを転記
- `Deploy` ボタンでソースコードをデプロイします
- `Test` ボタンで Lambda 関数を実行します
  - 最初は新しいイベントを作成してください
  - イベント名は `mytest01` を入力
  - イベントJSONはそのままで大丈夫です
  - テストが完了すると、結果が出力されます

----

### Lambda 関数をマネジメントコンソールで作成してみよう

- マネジメントコンソールから Lambda 関数を作成
  - 関数名は `handson-ddb-query-function` を入力
  - Python 3.9 を選択
  - 実行ロールは既存の `lambdaPollyRole`  ロールを選択
    - ラボでも `lambdaPollyRole` を使用します。どんな権限がついているか確認しておきましょう
- Lambda 関数のコードに [aws/ddbquery.py](https://github.com/shotagtag/devonaws/blob/main/samples/python/lambda/ddbquery.py) のソースコードを転記
- `Deploy` ボタンでソースコードをデプロイします
- `Test` ボタンで Lambda 関数を実行します
  - 最初は新しいイベントを作成してください
  - イベント名は `mytest01` を入力
  - イベントJSONはそのままで大丈夫です
  - `保存` して、作成したイベントを指定してテストを実行してみましょう
  - `testuser` のデータが取得できれば成功です
    - DynamoDB の `Notes` テーブルの中身を確認してみましょう
- Lambda 関数のソースコードを見ると `Notes` テーブルを検索する `UserId` がハードコーディングされています
  - `UserId` をイベントで渡せるようにしてみましょう
    - Lambda 関数のソースコードを編集します
      - `UserId = "testuser"` を削除します
      - `# UserId = event["UserId"]` のコメントを外します。(Python では `#` があるとその先はコメントになります)
    - 更新を反映するために `Deploy` します
  - `UserId` をテストイベントで渡してみましょう
    - `Test` ボタンの▼を押して、 `Configure test event` を開きます
    - イベント JSON に `{ "UserId": "testuser" }` を指定して保存、実行してみましょう
    - `UserId` をハードコーディングしなくてもOKになりました
- Lambda 関数のソースコードを見ると `Notes` テーブル名がハードコーディングされています
  - テーブル名を環境変数を参照するようにしてみましょう
    - Lambda 関数の `コード` で
      - `ddbTable = "Notes"` を削除します
      - `# ddbTable = os.environ['TABLE_NAME']` のコメントを外します
    - 更新を反映するために `Deploy` します
  - `設定` → `環境変数` でテーブル名を設定してみましょう
    - `キー` : `TABLE_NAME`
    - `値` : `Notes`
  - テストを実行してみましょう

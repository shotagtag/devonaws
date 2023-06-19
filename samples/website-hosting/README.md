## S3でウェブサイトホスティングを有効化する

### 目的

S3にhtml,css,画像などのStatic ContentsをアップロードしてWebサイトとして利用したい

- S3バケットを作成する
- バケットポリシーでアクセスできるように設定
- ウェブサイトホスティングを有効化
- ブラウザからhtmlへアクセス
- 他、画像なども相対パスで埋め込まれていることがわかる

### マネジメントコンソール上での手順

1. S3バケット作成
   1. ブロックパブリックアクセスをOFF
2. assetsの中身をバケットへアップロード
3. index.htmlを「開く」でトークン付きで開く
   1. この時点でHTMLを開いてもCSSなどは反映されていない
4. バケットの「プロパティ」からウェブサイトホスティングを有効化するとURLが生成される
   1. URLにバケット名が付いているのもポイント
5. 生成されたURLにアクセスしても拒否される
6. policy.jsonを開いてポリシーのテンプレを確認
7. 「アクセス許可」「バケットポリシー」で作成したバケットにGetObjectできるポリシーをバケットポリシーへ設定
8. URLにアクセスするとWebページが表示されてS3でWebページのホスティングが完成！レンタルサーバーいらず！

### バケットポリシー([BUCKET]を作成したバケット名に変更する)

```json
{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::[BUCKET]/*"
    }]
}
```
# 依存関係を定義
import boto3

region = 'ap-northeast-1'
bucket_name = '好きなバケット名'
file_name = '../../data/mycat01.jpeg'
key = 'sample/mycat01.jpeg'

# s3クライアント作成
resource = boto3.resource('s3', region_name=region)
bucket = resource.Bucket(bucket_name)

# バケットへアップロード
print('S3バケットへアップロード')
bucket.upload_file(file_name, key)
print(f'./{file_name} -> s3://{bucket_name}/{key}\n')

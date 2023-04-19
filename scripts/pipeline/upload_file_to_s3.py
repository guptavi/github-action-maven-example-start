import boto3
import sys
import os

def main():
    if len(sys.argv) != 6:
        print('Error: Required 5 arguments.')
        # Checks for 6 because the script path is in position 0. So len is 6
        # for 5 arguments.
        sys.exit(1)

    bucket_name = sys.argv[1]
    aws_key = sys.argv[2]
    aws_access_key = sys.argv[3]
    aws_access_secret = sys.argv[4]
    local_path = sys.argv[5]

    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
    )
    client = session.client('s3')

    # enumerate local files recursively
    for root, dirs, files in os.walk(local_path):

        for filename in files:

            # construct the full local path
            local_path = os.path.join(root, filename)
            destination = aws_key

            # construct the full Dropbox path
            relative_path = os.path.relpath(local_path, local_path)
            s3_path = os.path.join(destination, relative_path)
            bucket = bucket_name
            # relative_path = os.path.relpath(os.path.join(root, filename))

            print('Searching "%s" in "%s"' % (s3_path, bucket))
            print(destination);
            print(local_path);
            print(relative_path);
            print(s3_path);
            print(bucket);
            client.upload_file(local_path, bucket, "data")


    # response = client.upload_file(
    #     Filename=local_path,
    #     Bucket=bucket_name,
    #     Key=aws_key
    # )
    print('Done uploading')


main()

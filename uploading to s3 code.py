import boto3
s3_client = boto3.client('s3')
response = s3_client.upload_file(r'/Users/san/Documents/data /part2/Splitting data Code.py.part2', 'private2proj', 'part2/randm.txt.part2')
response = s3_client.upload_file(r'/Users/san/Documents/data /part 1/Splitting data Code.py.part1', 'my-project02', 'part1/randm.txt.part1')
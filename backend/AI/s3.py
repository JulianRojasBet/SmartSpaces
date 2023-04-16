import boto3
import os

def upload_to_s3(list_of_files):

    secret_key = os.getenv('AWS_SECRET_KEY', 'xxx')
    access_key = os.getenv('AWS_ACCESS_KEY', 'xxx')

    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    nombre_bucket_s3 = 'nombre-de-tu-bucket-s3' # PONER EL BUCKET
    urls_images = []
    for file_path in list_of_files:
        if file_path.endswith('.jpg') or file_path.endswith('.png'):
            s3_object_name = os.path.basename(file_path)
            s3.upload_file(file_path, nombre_bucket_s3, s3_object_name)
            url_publica = s3.generate_presigned_url('get_object', Params={'Bucket': nombre_bucket_s3, 'Key': nombre_objeto_s3}, ExpiresIn=3600)
            urls_images.append(url_publica)

    return urls_images

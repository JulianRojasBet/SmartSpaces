import boto3
import os

def upload_to_s3(list_of_files):
    s3 = boto3.client('s3', aws_access_key_id='TU_ACCESS_KEY_ID', aws_secret_access_key='TU_SECRET_ACCESS_KEY')
    nombre_bucket_s3 = 'nombre-de-tu-bucket-s3' # PONER EL BUCKET
    urls_images = []
    for file_path in list_of_files:
        if file_path.endswith('.jpg') or file_path.endswith('.png'):
            s3_object_name = os.path.basename(file_path)
            s3.upload_file(file_path, nombre_bucket_s3, nombre_objeto_s3)
            url_publica = s3.generate_presigned_url('get_object', Params={'Bucket': nombre_bucket_s3, 'Key': nombre_objeto_s3}, ExpiresIn=3600)
            urls_images.append(url_publica)

    return urls_images

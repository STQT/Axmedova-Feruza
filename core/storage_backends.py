"""
Custom storage backends for Cloudflare R2
"""

from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Storage for static files on Cloudflare R2
    """
    location = 'static'
    default_acl = None
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    """
    Storage for media files on Cloudflare R2
    """
    location = 'media'
    default_acl = None
    file_overwrite = False


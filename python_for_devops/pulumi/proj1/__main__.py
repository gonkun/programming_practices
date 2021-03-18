import json
import mimetypes
import os
import pulumi

from pulumi import export, FileAsset
from pulumi_aws import s3
from pulumi_aws import acm
from pulumi_aws import route53

# Split a domain name into its subdomain and parent domain names.
# e.g. "www.example.com" => "www", "example.com".


def get_domain_and_subdomain(domain):
    names = domain.split(".")
    if len(names) < 3:
        return('', domain)
    subdomain = names[0]
    parent_domain = ".".join(names[1:])
    return (subdomain, parent_domain)


# proj1 is project name defined in Pulumi.yaml
config = pulumi.Config('proj1')

content_dir = config.require('local_webdir')
domain_name = config.require('domain_name')

web_bucket = s3.Bucket('s3-website-bucket',
                       website=s3.BucketWebsiteArgs(
                           index_document="index.html",
                       ))

cert = acm.Certificate(
    'certificate', domain_name=domain_name, validation_method='DNS')

# content_dir = "www"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = s3.BucketObject(file,
                          bucket=web_bucket.id,
                          source=FileAsset(filepath),
                          content_type=mime_type)


def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}/*",
            ]
        }]
    })


bucket_name = web_bucket.id
bucket_policy = s3.BucketPolicy("bucket-policy",
                                bucket=bucket_name,
                                policy=bucket_name.apply(public_read_policy_for_bucket))

(subdomain, parent_domain) = get_domain_and_subdomain(domain_name)
zone = route53.Zone("route53_zone", name=parent_domain)

# Export the name of the bucket
export('bucket_name', web_bucket.id)
export('website_url', web_bucket.website_endpoint)

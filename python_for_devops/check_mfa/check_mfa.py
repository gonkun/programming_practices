#!/usr/bin/env python3

"""
Command-line tool for check if MFA is enabled
"""
import click
import boto3


def createConn(profile):
    session = boto3.Session(profile_name=profile)
    conn = session.client('iam')
    return conn


@click.command()
@click.option('--profile', default='userzoom-iam', help='Set AWS profile for connect to AWS API')
# @click.option('--username', required=True, help='Set AWS IAM user for create its login profile')


def checkMFA(profile):
    conn = createConn(profile)
    iam_users = []
    response = conn.list_users()

    for user in response['Users']:
        iam_users.append(user['UserName'])

    no_mfa_users = []
    for iam_user in iam_users:
        response = conn.list_mfa_devices(UserName=iam_user)
        if not response['MFADevices']:
            no_mfa_users.append(iam_user)
    print(*no_mfa_users, sep='\n')


if __name__ == '__main__':
    checkMFA()

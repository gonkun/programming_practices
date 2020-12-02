#!/usr/bin/env python3

"""
Command-line tool for manage IAM Users login
"""
import click
import boto3
import string
import random
from botocore.exceptions import ClientError


def createConn(profile):
    session = boto3.Session(profile_name=profile)
    conn = session.client('iam')
    return conn


def randomPassword(length=12):

    # create alphanumerical from string constants
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    PUNCTUATION = string.punctuation

    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)

    return random_password


@click.command()
@click.option('--profile', default='userzoom-iam', help='Set AWS profile for connect to AWS API')
@click.option('--username', required=True, help='Set AWS IAM user for create its login profile')
def createLogin(profile, username):

    conn = createConn(profile)
    password = randomPassword()

    try:
        conn.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
        )
    except ClientError as error:
        if error.response['Error']['Code'] == 'EntityAlreadyExists':
            print('Login profile already exists')
            exit(1)
        else:
            print(
                'Unexpected error occured while creating login profile... hence cleaning up', error)
            return 'Login profile could not be create', error

    print(f'Login profile user: {username}')
    print(f'Temporary password: {password}')


if __name__ == '__main__':
    createLogin()

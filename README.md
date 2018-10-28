# snapshot4000
test exercise in writing python withboto3 for basic snapshot

## About

Exercise in leaning basics of EC2 management with python and noto3

## Configuration

Boto3ec2 uses the configuration file created by the AWS cli .e.g

'aws configure --profile Boto3'

## Running
'pipenv run python ./boto3ec2.py <command> <subcommand> <--project=projectname>'

*command* is instances, volumes and snapshots

*subcommand* - depends on command
                instances - list, start, stop, create_snapshots
                volumes - list
                snapshots - list

*project* is optional and works with wildcard *

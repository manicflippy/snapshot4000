# snapshot4000
Test exercise in writing python with boto3 for basic snapshots, following ACloudGuru tutorials

## About

Exercise in leaning basics of EC2 management with python and boto3

## Configuration

Boto3ec2 uses the configuration file created by the AWS cli .e.g

'aws configure --profile Boto3'

## Running
'pipenv run python ./boto3ec2.py command subcommand --project=projectname'

*command* - is instances, volumes and snapshots

*subcommand* - depends on command
                instances - list, start, stop, create_snapshots
                volumes - list
                snapshots - list, --all

*project* - is optional and works with wildcard *

import boto3
import click

session = boto3.Session(profile_name='Boto3')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances

@click.group()
def cli():
    """Boto3 manages snapshots"""
######################
@cli.group('volumes')
def volumes():
    """Commands for volumes"""
######
@volumes.command('list')
@click.option('--project', default=None,
    help='''Only volumes for project (tag Project:<name>) run with pipenv run "python boto3.py volumes list --project=<name>"''')
def list_volumes(project):
    "list EC2 volumes"
    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            tags = { t['Key']: t['Value'] for t in i.tags or []}
            print (", ".join((
                v.id,
                i.id,
                v.state,
                str(v.size) +"GiB",
                v.encrypted and "Encrypted" or "Not Encrypted",
                tags.get('Project', '<no project>')
                )))
    return
######################
@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""
#####
@snapshots.command('list')
@click.option('--project', default=None,
    help='''Only snapshots for project (tag Project:<name>) run with pipenv run "python boto3.py snapshots list --project=<name>"''')
def list_volumes(project):
    "list EC2 snapshots"
    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                tags = { t['Key']: t['Value'] for t in i.tags or []}
                print (", ".join((
                s.id,
                v.id,
                i.id,
                s.state,
                s.progess,
                s.start_time.strftime("%c")
                )))
    return
######################
@cli.group('instances')
def instances():
    """Commands for instances"""
#####
@instances.command('snapshots',
    help="Create snapshots of all volumes")
@click.option('--project', default=None,
    help='''Only volumes for project (tag Project:<name>) run with pipenv run "python boto3.py instances list --project=<name>"''')
def create_snapshots(project):
    "create snapshots of EC2 instances"
    instances = filter_instances(project)
    for i in instances:
            for v in i.volumes.all():
                print("Creating snapshot of {0}...".format(v.id))
                v.create_snapshot(Description="Created by Boto3EC2.py")
    return



@instances.command('list')
@click.option('--project', default=None,
    help='''Only instances for project (tag Project:<name>) run with pipenv run "python boto3.py instances list --project=<name>"''')
def list_instances(project):
    "list EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        print (','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))
    return
#########
@instances.command('stop')
@click.option('--project', default=None,
    help='''Only instances for project (tag Project:<name>) run with pipenv run "python stop --project=<name>"''')
def stop_instances(project):
    "list EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return
#####
@instances.command('start')
@click.option('--project', default=None,
    help='''Only instances for project (tag Project:<name>) run with pipenv run "python start --project=<name>"''')
def start_instances(project):
    "list EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return
#########################
#########################
if __name__ == '__main__':
    cli()

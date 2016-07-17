import boto3

'''

Purpose:

The purpose of this is to update R53 "A" records when a scale event happens so that
the record has the most up to date information on the instances it points to. This 
acts as a Lambda endpoint for ASG events (scale up/down) that get sent through SNS.

This is useful for those that use R53 as a load balancer instead of ELB.

Requirements:

1. Scale events go through an SNS topic which then call this lambda function.
2. Appropriate iam execution roles for all the things.

See README.md for more detailed instructions. 

Usage:

Simply add the following tags to an ASG (key: value) 
- RecordSync: True
- RecordName: <fqdn> (ex. hostname.yourdomain.com)
- AddressType: <internal|external>*
- HostedZoneId: XYZABC123

* Denotes wether sync should use public or internal IP's for a given instance 
when syncing records. 

Set the RecordSync tag to False if you want to turn off syncing for a particular ASG.

This works for all routing policies (weighted, failover, etc).

See README.md for build and deployment instructions.

'''


def asg_event(event, context):
    pass


def tag_lookup(asg_id):
    pass


def lookup_record(hosted_zone_id, record_name):
    pass


def validate_record():
    pass

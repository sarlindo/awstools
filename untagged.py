#!/usr/bin/env python

import skew

for instance in skew.scan('arn:aws:ec2:*:*:instance/*'):
    if not instance.tags:
        print('%s is untagged' % instance.arn)

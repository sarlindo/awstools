#!/usr/bin/env python

import skew

total_size = 0
total_volumes = 0

for volume in skew.scan('arn:aws:ec2:*:*:volume/*'):
    if not volume.data['Attachments']:
        total_volumes += 1
        total_size += volume.data['Size']
        print('%s: %dGB' % (volume.arn, volume.data['Size']))
print('Total unattached volumes: %d' % total_volumes)
print('Total size (GB): %d' % total_size)

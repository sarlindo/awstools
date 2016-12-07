#!/usr/bin/env python

import skew
from skew.arn import ARN
arn = ARN()
services=arn.service.choices()
services.sort()

print('Enumerating all resources in the following services: ' + ' '.join(services) + '\n')

for service in services:
     #skipping global services because the API endpoint fails due to it being a global service. Bug that needs fixing.
     if service == "iam" or service == "route53":
        print(service)  
        print('Skipping global services')
     else:
        uri = 'arn:aws:' + service + ':*:*:*/*'
        arn = skew.scan(uri)
        
        for resource in arn:
           if resource.tags and 'Project' in resource.tags.keys():
             if resource.tags.get('Project') == 'tmxdatascience': 
                print(resource.arn)
                print(resource.tags)

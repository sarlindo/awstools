ec2instancelist=$(aws ec2 describe-instances --filters Name=vpc-id,Values=vpc-4469ab23 --query 'Reservations[].Instances[].[InstanceId,Tags[?Key==`Name`] | [0].Value]' --output text)

while read -r line; do

	echo "Applying Alarms to EC2 instance $line."

        instanceid=$(echo $line | awk '{print $1}')
        instancename=$(echo $line | awk '{print $2}')
	
	aws cloudwatch put-metric-alarm --alarm-name ${instancename}-CPUUtilization --alarm-description "Alarm when CPU exceeds 80%" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold  --dimensions Name=InstanceId,Value=${instanceid} --evaluation-periods 2 --alarm-actions arn:aws:sns:us-east-1:143869307266:DEV-INFRA-COMMON-ALERTS --unit Percent

done <<< "$ec2instancelist"

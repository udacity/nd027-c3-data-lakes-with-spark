We'll be creating an EMR cluster for the exercise.
First, let's install `awscli`.
This will give you an access to create an EMR cluster, EC2 cluster (if you need it later), shows a status of all the clusters with your keys, etc. It does a ton of things!

Once it's installed, run the script below to launch your cluster. Be sure to revise anything in the `<>` to match your filename.

```
aws emr create-cluster --name <YOUR_CLUSTER_NAME> --use-default-roles  --release-label emr-5.28.0 --instance-count 2 --applications Name=Spark Name=Zeppelin  --bootstrap-actions Path=<YOUR_BOOTSTRAP_FILENAME> --ec2-attributes KeyName=<YOUR_KEY_NAME> --instance-type m5.xlarge --instance-count 3 --auto-terminate
```
```
YOUR_CLUSTER_NAME: required, anything you'd like!
YOUR_KEY_NAME: required, your IAM key name that is saved under .ssh/ directory
YOUR_BOOTSTRAP_FILENAME: optional, should be your bootstrap file, executable (.sh file) in an accessible S3 location. If you aren't going to use the bootstrap file, you can removed `--bootstrap-actions` tag.
```

This will give you something like this..

```
{
    "ClusterId": "j-2PZ79NHXO7YYX",
    "ClusterArn": "arn:aws:elasticmapreduce:us-east-2:027631528606:cluster/j-2PZ79NHXO7YYX"
}
`

Go to AWS EMR console from your web browser, then check if the cluster is showing up.

Or you can type

`aws emr describe-cluter --cluster-id <CLUSTER_ID FROM ABOVE>`

For example, I would do `aws emr describe-cluster --cluster-id j-2PZ79NHXO7YYX` to see if this cluster is ready to go.

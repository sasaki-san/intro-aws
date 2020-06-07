from aws_cdk import (
    core,
    aws_ec2 as ec2,
)
import os
from dataclasses import dataclass

@dataclass
class StackProps:
    key_name: str

class MyFirstEc2(core.Stack):

    def __init__(self, scope: core.App, name: str, props: StackProps, **kwargs) -> None:
        super().__init__(scope, name, **kwargs)

        vpc = ec2.Vpc(
            self, "MyFirstEc2-Vpc",
            max_azs=1,
            cidr="10.10.0.0/23",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name="private",
                    subnet_type=ec2.SubnetType.PRIVATE,
                )
            ],
            nat_gateways=0,
        )

        sg = ec2.SecurityGroup(
            self, "MyFirstEc2Vpc-Sg",
            vpc=vpc,
            allow_all_outbound=True,
        )
        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
        )

        # create a new EC2 instance
        host = ec2.Instance(
            self, "MyFirstEc2Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=sg,
            key_name=props.key_name
        )

app = core.App()
MyFirstEc2(
    app, "MyFirstEc2",
    props=StackProps(
        key_name=os.environ["KEY_NAME"],
    ),
    env={
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"],
    }
)

app.synth()

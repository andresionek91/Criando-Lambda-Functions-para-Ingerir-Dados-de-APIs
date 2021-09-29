from aws_cdk import core as cdk
from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_iam as iam
)


class LambdaFunctionsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = _lambda.Function(
            scope=self,
            id="LambdaHelloBeliscoCdk",
            runtime=_lambda.Runtime.PYTHON_3_9,
            timeout=cdk.Duration.seconds(amount=30),
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset("lambda_functions/code"),
        )

        # TODO: Agendar para rodar de dia em dia
        # TODO: Confuigurar memória, mudar descrição
        # TODO: Automatizar o deploy usando CI/CD (Github Actions, CircleCi, Jenkins)

        bucket = s3.Bucket(
            scope=self,
            id="bucket-mercado-bitcoin",
            bucket_name="belisco-cripto-milionario"
        )

        fn.add_to_role_policy(statement=iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:PutObject",
                "s3:ListBucket",
                "s3:PutObjectAcl"
            ],
            resources=[
                bucket.bucket_arn,
                f"{bucket.bucket_arn}/*"
            ]
        ))

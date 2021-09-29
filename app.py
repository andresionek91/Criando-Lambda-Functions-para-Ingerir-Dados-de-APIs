from aws_cdk import core

from lambda_functions.lambda_functions_stack import LambdaFunctionsStack


app = core.App()
LambdaFunctionsStack(app, "LambdaFunctionsStack")
app.synth()

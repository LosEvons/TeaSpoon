import sys
from invoke.tasks import task

@task
def debug(ctx):
    ctx.run("python teaspoon/index.py")

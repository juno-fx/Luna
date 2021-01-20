"""
Server init module
"""
# std imports
from pprint import pprint
import os
from typing import Optional

import docker
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from .server import APP


# data model
class Image(BaseModel):
    """
    Image model
    """
    tag: str
    repository: str
    message: str
    dry: Optional[bool] = False


# endpoint
@APP.post("/snapshot")
async def snapshot(image: Image):
    """
    Snapshot an image

    Example:

    .. code-block:: shell

        curl -X POST
            "http://localhost:3030/snapshot"
            -H  "accept: application/json"
            -H  "Content-Type: application/json"
            -d {
                "tag":"string",
                "repository":"string",
                "message":"string",
                "dry":false
            }

    :returns: bool

    """
    client = docker.DockerClient()

    # find our buddy
    workstation = None
    env_var = f"LUNA={os.environ['BUDDY']}"
    for container in client.containers.list():
        if env_var in container.attrs['Config']['Env']:
            workstation = container
            break

    if not workstation:
        return False

    # snapshot and push
    api = docker.APIClient()
    registry = os.environ.get('REG')
    if not registry:
        registry = "https://index.docker.io/v1"

    # daemon calls
    api.login(
        username=os.environ['USR'],
        password=os.environ['PAS'],
        registry=registry
    )

    api.commit(
        container=workstation.attrs['Id'],
        repository=image.repository,
        tag=image.tag,
        message=image.message
    )

    #  for testing
    if image.dry:
        return True

    rsp = api.push(
        repository=image.repository,
        tag=image.tag
    )

    if "error" in rsp:
        raise HTTPException(
            status_code=500,
            detail="Push failure"
        )
    return True

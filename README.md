# Buggy
[![Discord](https://img.shields.io/discord/366655480421941260)](https://discord.gg/f64hPv6Mxp)
[![Documentation Status](https://readthedocs.org/projects/hfx-buggy/badge/)](https://hfx-buggy.readthedocs.io/en/latest/)
[![Updates](https://pyup.io/repos/github/HatfieldFX/buggy/shield.svg)](https://pyup.io/repos/github/HatfieldFX/buggy/)
[![Python 3](https://pyup.io/repos/github/HatfieldFX/buggy/python-3-shield.svg)](https://pyup.io/repos/github/HatfieldFX/buggy/)
[![Docker Pulls](https://img.shields.io/docker/pulls/hatfieldfx/buggy.svg)](https://hub.docker.com/r/hatfieldfx/buggy)
[![Docker Size](https://img.shields.io/docker/image-size/hatfieldfx/buggy/latest)](https://hub.docker.com/r/hatfieldfx/buggy)

Sidecar container that deploys with an HFX Workstation. Luna binds to the docker.sock and
"snapshots" the assigned container using the `docker commit` command via a REST endpoint.
Once the snapshot is taken, the resulting image is tagged and `docker push` is executed,
which pushes the resulting image to the specified docker registry via the environment
configuration.

Please reference the [documentation](https://hfx-buggy.readthedocs.io/en/latest/) for
information on deployment via docker-compose and kubernetes.

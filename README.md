# Luna
[![Discord](https://img.shields.io/discord/366655480421941260)](https://discord.gg/f64hPv6Mxp)
[![Documentation Status](https://readthedocs.org/projects/hfx-buggy/badge/)](https://hfx-buggy.readthedocs.io/en/latest/)
[![Docker Pulls](https://img.shields.io/docker/pulls/junofx/luna.svg)](https://hub.docker.com/r/junofx/luna)
[![Docker Size](https://img.shields.io/docker/image-size/junofx/luna/latest)](https://hub.docker.com/r/junofx/luna)

Sidecar container that deploys with an HFX Workstation. Luna binds to the docker.sock and
"snapshots" the assigned container using the `docker commit` command via a REST endpoint.
Once the snapshot is taken, the resulting image is tagged and `docker push` is executed,
which pushes the resulting image to the specified docker registry via the environment
configuration.

Please reference the [documentation](https://hfx-buggy.readthedocs.io/en/latest/) for
information on deployment via docker-compose and kubernetes.

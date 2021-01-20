
Usage
=====

Luna can be deployed using either docker-compose or kubernetes. Luna finds its
"buddy" image via its hostname. You specify this int the environment configuration.

kubernetes deployment
---------------------

.. literalinclude:: ./examples/deployment.yaml
    :linenos:
    :language: yaml

docker-compose
--------------

.. warning::
    Luna was designed to be used in a kubernetes cluster. The `docker-compose` setup
    is mainly for testing.

.. literalinclude:: ./examples/docker-compose.yaml
    :linenos:
    :language: yaml

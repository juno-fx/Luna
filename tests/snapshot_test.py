import unittest

import luna
from fastapi.testclient import TestClient

client = TestClient(luna.APP)


class Snapshot(unittest.TestCase):

    @staticmethod
    def test_snapshot():
        response = client.post(
            "/snapshot",
            json={
                "tag": "latest",
                "repository": "test/test",
                "message": "testing message",
                "dry": True
            }
        )

        assert response.status_code == 200
        assert response.json() is True

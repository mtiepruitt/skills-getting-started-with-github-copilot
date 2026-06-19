from copy import deepcopy

from fastapi.testclient import TestClient
import pytest

import src.app as app_module


@pytest.fixture(scope="function")
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    snapshot = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(snapshot))
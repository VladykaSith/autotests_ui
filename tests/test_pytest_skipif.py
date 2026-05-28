import pytest

system_version = "v1.2.0"


@pytest.mark.skipif(system_version == "v1.3.0", reason="Version 1.3.0 not supported")
def test_feature_in_development1():
    pass

@pytest.mark.skipif(system_version == "v1.2.0", reason="Version 1.2.0 not supported")
def test_feature_in_development2():
    pass



import pytest
from lib.ConfigLoader import get_config
from lib.Utils import get_spark_session


@pytest.fixture(scope='session')
def spark():
    return get_spark_session("LOCAL")

def test_get_config(spark):
    conf_local = get_config("LOCAL")
    conf_qa = get_config('QA')
    assert conf_local['enable.hive'] == 'false'
    assert conf_qa['enable.hive'] == 'true'


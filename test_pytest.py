import pytest

from lib import DataLoader, Transformations
from lib.Utils import get_spark_session


@pytest.fixture(scope='session')
def spark():
    return get_spark_session("LOCAL")


def test_output_df(spark):
    expected_output = [('4558adc3-0637-45a8-9baa-534b2ebdadea', 1, 1, 1, 0),
                       ('1b90c7ca-b4b8-43ee-8bb1-18999bbfe4cd', 0, 1, 1, 0),
                       ('51bdd515-553c-454d-b28b-5857685e7571', 1, 1, 0, 0),
                       ('5cc351f3-887b-4bea-a681-f6f8432d117b', 0, 0, 0, 1),
                       ]
    current_df = DataLoader.read_input_file(spark)
    current_df = Transformations.transform_df(current_df)
    actual_output = [(r.unique_id, r.ex_1, r.ex_2, r.ex_3, r.ex_4) for r in current_df.collect()]
    assert expected_output == actual_output

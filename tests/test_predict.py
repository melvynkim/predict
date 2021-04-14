import predict
import pandas as pd


class TestPredict(object):
  def test_works(self):
    data = {'Sales': [1, 2, 2, 10, None], 'Revenue': [4, 5, 6, 7, 8]}
    df = pd.DataFrame.from_dict(data)
    pd = predict.Classifier(train_data=df, target_col='Revenue')
    info = pd._col_info(df['Sales'])
    assert info['column_type'] == 'category'
    assert info['total_count'] == 5
    assert info['unique_count'] == 4
    assert info['null_count'] == 1

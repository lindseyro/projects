test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> rookies_ = pd.read_csv('data/nba_rookies.csv');\n"
                                               ">>> rookies_ = rookies_.set_index('Name');\n"
                                               ">>> rookies_['TARGET_5Yrs'] = np.where(rookies_['TARGET_5Yrs'] == 'No', 0, 1) ;\n"
                                               ">>> X_ = rookies.drop('TARGET_5Yrs', axis = 1) ;\n"
                                               ">>> y_ = rookies['TARGET_5Yrs'];\n"
                                               '>>> pd.testing.assert_frame_equal(X_, X);\n'
                                               '>>> pd.testing.assert_series_equal(y_, y)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

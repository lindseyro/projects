test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> rookies_ = pd.read_csv('data/nba_rookies.csv');\n"
                                               ">>> rookies_ = rookies_.set_index('Name');\n"
                                               ">>> rookies_['TARGET_5Yrs'] = np.where(rookies_['TARGET_5Yrs'] == 'No', 0, 1) ;\n"
                                               '>>> pd.testing.assert_frame_equal(rookies, rookies_)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> rookies_ = pd.read_csv('data/nba_rookies.csv');\n"
                                               ">>> rookies_ = rookies_.set_index('Name');\n"
                                               '>>> pd.testing.assert_frame_equal(rookies, rookies_)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

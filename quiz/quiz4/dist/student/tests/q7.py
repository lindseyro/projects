test = {   'name': 'q7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> rookies_ = pd.read_csv('data/nba_rookies.csv');\n"
                                               ">>> rookies_ = rookies_.set_index('Name');\n"
                                               ">>> rookies_['TARGET_5Yrs'] = np.where(rookies_['TARGET_5Yrs'] == 'No', 0, 1) ;\n"
                                               ">>> X_ = rookies_.drop('TARGET_5Yrs', axis = 1) ;\n"
                                               ">>> y_ = rookies_['TARGET_5Yrs'];\n"
                                               '>>> X_train_, X_test_, y_train_, y_test_ = train_test_split(X_, y_, random_state = 22);\n'
                                               '>>> dtree_ = DecisionTreeClassifier(random_state = 22);\n'
                                               '>>> dtree_.fit(X_train_, y_train_);\n'
                                               '>>> predictions_ = dtree_.predict(X_test_);\n'
                                               '>>> np.testing.assert_array_equal(predictions, predictions_)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

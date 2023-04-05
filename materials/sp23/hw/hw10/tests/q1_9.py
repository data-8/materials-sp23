test = {   'name': 'q1_9',
    'points': [2, 3],
    'suites': [   {   'cases': [   {   'code': ">>> test_table = Table().with_columns('x', make_array(1, 2, 4), 'y', make_array(4, 5, 6))\n"
                                               ">>> np.all(np.isclose(predict(test_table, 'x', 'y'), make_array(4.14285714, 4.78571429, 6.07142857)))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> test_table_2 = Table().with_columns('x', make_array(-1, -3, -5), 'y', make_array(0, 3, 4))\n"
                                               ">>> np.all(np.isclose(predict(test_table_2, 'x', 'y'), make_array(0.33333333, 2.33333333, 4.33333333)))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

test = {   'name': 'q35',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # HINT: Check the order of your table. \n'
                                               ">>> np.isclose(round(farmers_markets_locations_by_latitude.column('y').item(1), 4), round(64.8459, 4))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

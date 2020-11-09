test = {
  'name': 'Question my_titles',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'my_titles'
          >>> 'my_titles' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'my_titles'
          >>> # from its initial state (of ...)
          >>> my_titles is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(my_titles, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(my_titles)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_titles[10]
          'Who cares?'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_titles = my_titles.copy()
          >>> more_titles[pct_profit < 100] = 'Who cares?'
          >>> np.all(my_titles == more_titles)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

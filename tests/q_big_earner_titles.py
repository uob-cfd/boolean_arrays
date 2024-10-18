test = {
  'name': 'Question big_earner_titles',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'big_earner_titles'
          >>> 'big_earner_titles' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'big_earner_titles'
          >>> # from its initial state (of ...)
          >>> big_earner_titles is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(big_earner_titles, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(big_earner_titles)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_earner_titles[0]
          'The Godfather'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_earner_titles[0]
          'The Godfather'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.all(big_earner_titles == titles[pct_profit > 500])
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

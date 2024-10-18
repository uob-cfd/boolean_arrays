test = {
  'name': 'Question relative_loser_titles',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'relative_loser_titles'
          >>> 'relative_loser_titles' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'relative_loser_titles'
          >>> # from its initial state (of ...)
          >>> relative_loser_titles is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert isinstance(relative_loser_titles, np.ndarray)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(relative_loser_titles)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> relative_loser_titles[0]
          'Fight Club'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.all(relative_loser_titles == titles[pct_profit < 100])
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

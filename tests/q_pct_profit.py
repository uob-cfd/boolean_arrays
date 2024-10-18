test = {
  'name': 'Question pct_profit',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'pct_profit'
          >>> 'pct_profit' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'pct_profit'
          >>> # from its initial state (of ...)
          >>> pct_profit is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(pct_profit, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(pct_profit)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.isclose(pct_profit[0], 113.365876)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.allclose(pct_profit, (gross_earnings / budgets) * 100)
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

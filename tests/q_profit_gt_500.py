test = {
  'name': 'Question profit_gt_500',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'profit_gt_500'
          >>> 'profit_gt_500' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'profit_gt_500'
          >>> # from its initial state (of ...)
          >>> profit_gt_500 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(profit_gt_500, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(profit_gt_500)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(profit_gt_500) == {True, False}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(profit_gt_500[:3] == [False, True, False])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(profit_gt_500 == (pct_profit > 500))
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

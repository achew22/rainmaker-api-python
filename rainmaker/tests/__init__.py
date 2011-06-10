import unittest
import doctest


def all_tests_suite():
    suite = unittest.TestLoader().loadTestsFromNames([
        'rainmaker.tests.do_lookup',
        'rainmaker.tests.helper',
    ])
    return unittest.TestSuite([suite])


def main():
    runner = unittest.TextTestRunner()
    suite = all_tests_suite()
    runner.run(suite)


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0,
        os.path.dirname( # 1
            os.path.dirname( # 2
                os.path.dirname( # 3 levels up
                    os.path.abspath(__file__)))))
    main()


class PytestTestRunner:
    """
    Runs pytest to discover and run tests.
    """

    def __init__(self, pattern=None, top_level=None, verbosity=1,
                 interactive=True, failfast=False, keepdb=False,
                 reverse=False, debug_mode=False, debug_sql=False, parallel=0,
                 tags=None, exclude_tags=None, **kwargs):

        self.pattern = pattern
        self.top_level = top_level
        self.verbosity = verbosity
        self.interactive = interactive
        self.failfast = failfast
        self.keepdb = keepdb
        self.reverse = reverse
        self.debug_mode = debug_mode
        self.debug_sql = debug_sql
        self.parallel = parallel
        self.tags = set(tags or [])
        self.exclude_tags = set(exclude_tags or [])

    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument(
            '-k', '--keepdb', action='store_true', dest='keepdb',
            help='Preserves the test DB between runs.'
        )
        parser.add_argument(
            '--tag', action='append', dest='tags',
            help='Run only tests with the specified tag. Can be used multiple times.',
        )
        parser.add_argument(
            '--exclude-tag', action='append', dest='exclude_tags',
            help='Do not run tests with the specified tag. Can be used multiple times.',
        )

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        """
        Run pytest and return the exitcode.
        It translates some of Django's test command option to pytest's.
        """
        import pytest
        argv = []

        if self.failfast:
            argv.append('--exitfirst')

        if self.verbosity == 0:
            argv.append('--quiet')
        elif self.verbosity == 2:
            argv.append('--verbose')
        elif self.verbosity == 3:
            argv.append('-vv')

        if self.keepdb:
            argv.append('--reuse-db')

        if self.parallel:
            argv.append('--numprocesses={}'.format(self.parallel))

        # #TODO: to check
        # if self.tags and not self.exclude_tags:
        #     argv.append("-m '{}'".format(self.tags))
        # elif not self.tags and self.exclude_tags:
        #     argv.append("-m '{}'".format('not '.join(self.exclude_tags)))
        # else:
        #     tags = '{} and'.format(self.tags)
        #     exclude_tags = 'not {} and'.join(self.exclude_tags)
        #     argv.append("-m '{} {}'".format(tags, exclude_tags))

        argv.extend(test_labels)
        return pytest.main(argv)

from django.test.runner import DiscoverRunner


class NoDBTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database destruction defined in parent class """
        pass

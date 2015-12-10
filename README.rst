pytest_sample
=============

Sample project for the article

Run tests
---------

Base

.. code:: bash

    $ py.test
        or
    $ python setup.py test

With pytest options. Please see `pytest --help` if you want to know the details of pytest options.

.. code:: bash

    $ py.test -v
        or
    $ python setup.py test --pytest-args='-v'

On Jenkins, it's better to run tests with `--capture=sys`. Due to this option, test report includes log in stdout.

.. code:: bash

    $ py.test --capture=sys
        or
    $ python setup.py test --pytest-args='--capture=sys'

You can run tests with several filters.

.. code:: bash

    # specified module
    $ py.test tests/test_calc.py

    # specified method
    $ py.test tests/test_calc.py::test_add

    # modules/methods including specified keyword
    $ py.test -k calc

    # tests with @pytest.mark.slow
    $ py.test -m slow

    # tests with both @pytest.mark.slow and @pytest.mark.httpaccess
    $ py.test -m 'slow and httpaccess'
    # tests with @pytest.mark.slow, but without @pytest.mark.httpaccess
    $ py.test -m 'slow and not httpaccess'

Others
------

This project uses following services.

- `httpbin(1) <https://httpbin.org/>`_

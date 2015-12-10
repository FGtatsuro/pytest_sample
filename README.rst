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

Others
------

This project uses following services.

- `httpbin(1) <https://httpbin.org/>`_

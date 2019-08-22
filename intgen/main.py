
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import IntGenError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('intgen')
CONFIG['intgen']['foo'] = 'bar'

# meta defaults
META = init_defaults('output.json')
META['output.json']['overridable'] = True


class IntGen(App):
    """Road intersection generator primary application."""

    class Meta:
        label = 'intgen'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        meta_defaults = META

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
            'json'
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'json'

        # register handlers
        handlers = [
            Base
        ]


class IntGenTest(TestApp,IntGen):
    """A sub-class of IntGen that is better suited for testing."""

    class Meta:
        label = 'intgen'


def main():
    with IntGen() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except IntGenError as e:
            print('IntGenError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()

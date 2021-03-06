import click, requests, os, sys

#options configuration
class Config():
    '''Options configuration'''

    def __init__(self, backend, url, output):
        self.backend = backend
        self.url = url
        self.output = output

# common decorator of stat and read commands
def check_response(func):
    def wrapper(*args, **kwargs):
        ctx = args[0]
        uuid = kwargs['uuid']

        # Trying to get request from the corresponding address. If it it's invalid,
        # then exeption is raised
        try:
            request_url = os.path.join(ctx.obj.url, 'file', uuid, func.__name__)
            response = requests.get(request_url)

            # if address not found then SystemExit is raised
            if response.status_code != 200:
                sys.exit(1)

            result = response.content
        except SystemExit:
            result = f'Request error!\n{response.status_code} status code\n'
            result = result.encode()
        except:
            result = f'Can\'t connect to the {ctx.obj.backend} server at address {ctx.obj.url}\n'
            result = result.encode()

        ctx.obj.output.write(result)

        return func(*args, **kwargs)
    return wrapper


@click.group(context_settings={'show_default': True}) # All option's default is showing
@click.option('--backend',  type=click.Choice(['django', 'flask'],
              case_sensitive=False), default='django',
              help='Set a backend to be used, choices are django and flask.')
@click.option('--django-server', default='localhost:8000',
              help='Set a host and port of the Django server.')
@click.option('--flask-server', default='127.0.0.1:5000',
              help='Set a host and port of the Flask server.')
@click.option('--output', default='-', type=click.File('wb'),
              help='Set the file where to store the output.')
@click.pass_context
def cli(ctx, backend, django_server, flask_server, output):
    if backend == 'django':
        url = django_server
    else:
        url = flask_server

    # appending http:// to the beginning of the address if it is not there
    url = url if url.startswith('http://') else ('http://' + url)
    # set the options configurations to the click context
    ctx.obj = Config(backend, url, output)

@cli.command('stat', help='Prints the file metadata in a human-readable manner.')
@click.argument('UUID', metavar='UUID')
@click.pass_context
@check_response
def stat(ctx, uuid):
    '''Prints the file metadata in a human-readable manner.'''
    ...


@cli.command('read', help='Outputs the file content.')
@click.argument('UUID', metavar='UUID')
@click.pass_context
@check_response
def read(ctx, uuid):
    '''Outputs the file content.'''
    ...


if __name__ == '__main__':
    res = cli()

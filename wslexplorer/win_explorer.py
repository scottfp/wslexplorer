import click, os, subprocess
from re import match

import wslexplorer.config

@click.command()
@click.argument('path', type=click.Path(resolve_path=True, exists=True),
                default='.', required=False)
@click.option('config_file', '--config', '-c',
              type=click.Path(resolve_path=True, exists=True),
              help="Config file to use instead of default")
def launch(path, config_file=None):
    """Open Windows NT File Explorer at PATH from Windows Subsystem for Linux.  Default PATH is current directory."""
    config = wslexplorer.config.Config(wslexplorer.config.DEFAULTS)
    if config_file:
        config.load_file(config_file)
    else:
        config_path = os.path.join(click.get_app_dir('wsl-explorer-launcher'),
                                   'config.yaml')
        if os.path.exists(config_path):
            config.load_file(config_path)
        else:
            click.echo("No configuration found.")
            config['user'] = click.prompt('Windows username',
                                          config['user'])
            config.save_file(config_path)
            click.echo("Config saved to {}".format(config_path))

    #Convert POSIX path inside Windows WSL to a Windows path
    path = path.replace('/', '\\')
    reg_string = r'\\mnt\\([{}\z])'.format(''.join(config['drives']))
    m = match(reg_string, path)
    if m:
        prefix = '{}:'.format(m.group(1).upper())
        path = path[6:]
    else:
        prefix = config['lxss_path']
    
    with open(os.devnull, 'w') as FNULL:
        subprocess.call([config['explorer_path'], prefix + path],
                        stdout=FNULL, stderr=subprocess.STDOUT)

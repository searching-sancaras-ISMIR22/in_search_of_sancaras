import click

from src.core import run_pipeline
from src.io import load_yaml

@click.group()
def cli():
    pass

@cli.command(name="mask")
@click.option('--conf-path', type=str, default='conf/mask.yaml', required=False)
def cmd_mask(conf_path):
    """
    Extract silence/stability mask for pitch track, <pitch_track> using
	parameters in <conf_path>
    """
    conf = load_yaml(conf_path)


@cli.command(name="selfsim")
@click.option('--conf-path', type=str, default='conf/mask.yaml', required=False)
def cmd_selfsim(audio, mask, conf_path):
    """
    Extract masked self similarity matrix for audio, <audio> and silence/stability
    mask, <mask> using parameters in <conf_path>
    """
    conf = load_yaml(conf_path)


@cli.command(name="pattern")
@click.option('--conf-path', type=str, default='conf/mask.yaml', required=False)
def cmd_pattern(conf_path):
    """
    Run pattern finding pipeline according to parameters in <conf_path>
    """
    conf = load_yaml(conf_path)


if __name__ == '__main__':
    cli()


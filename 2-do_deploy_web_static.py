from fabric.api import env, run, put
from os.path import basename

env.hosts = ['54.173.83.155', '100.26.165.205']

def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not archive_path.exists():
        return False
    archive_name = basename(archive_path)
    target_folder = '/data/web_static/releases/' + archive_name.split('.')[0]
    put(archive_path, '/tmp/')
    run(f'unzip /tmp/{archive_name} -d {target_folder}')
    run(f'rm /tmp/{archive_name}')
    run('rm -rf /data/web_static/current')
    run(f'ln -s {target_folder} /data/web_static/current')
    return True

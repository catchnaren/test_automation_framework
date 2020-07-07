class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['test', 'stage', 'prod']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment')

        self.base_url = {
            'test': 'https://test.cflowapps.com/cflowtest/',
            'stage': 'https://cflow.cavintek.com/new-stage/',
            'prod': 'https://cflow.cavintek.com/cflownew/'
        }[env]

        self.app_port = {
            'test': '',
            'stage': '',
            'prod': ''
        }[env]

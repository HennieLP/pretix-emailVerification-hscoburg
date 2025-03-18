from setuptools import setup, find_packages

setup(
    name='pretix-emailChecker',
    version='1.0.0',
    description='A pretix plugin for email checking',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pretix>=4.0.0'],
    entry_points={
        'pretix.plugin': [
            'pretix_emailChecker=pretix_emailChecker:PretixPluginMeta',
        ],
    }
)

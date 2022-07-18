from setuptools import setup, find_packages

setup(
    name='q2-samtools',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='Apache-2.0',
    author='Chase Ridenour',
    author_email='cridenour@tgen.org',
    description='Samtools wrapper',
    entry_points={
        'qiime2.plugins': ['q2-samtools=q2_samtools.plugin_setup:plugin']
    },
    zip_safe=False
)

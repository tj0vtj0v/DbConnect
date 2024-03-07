from distutils.core import setup

setup(
    name='DbConnectTjorven',
    packages=['DbConnectTjorven'],
    version='1.0',
    license='GNU',
    descriptoin='test',
    author='Tjorven Burdorf',
    author_email='BurdorfTjorven@gmail.com',
    url='https://github.com/tj0vtj0v/DbConnect',
    download_url='https://github.com/tj0vtj0v/DbConnect/archive/refs/tags/v_1.1.tar.gz',
    keywords=['MYSQL', 'Database', 'Connector', 'Private'],
    install_requires=['mysql-connector-python'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Just Author',
        'Topic :: Development Aid',
        'License :: GNU V3.0',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

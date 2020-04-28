from setuptools import setup


setup(name='joinmarketbitcoin',
      version='0.7.0dev',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/Joinmarket-Org/joinmarket-clientserver/jmbitcoin',
      author='',
      author_email='',
      license='GPL',
      packages=['jmbitcoin'],
      python_requires='>=3.6',
      install_requires=['coincurve', 'python-bitcointx>=1.0.5', 'pyaes', 'urldecode'],
      zip_safe=False)

from distutils.core import setup
setup(
  name = 'PVPolyfit',
  packages = ['PVPolyfit'],
  version = '0.4',
  license='MIT',
  description = 'A high-resolution multiple linear regression algorithm used to analyze PV output with a few inputs',
  author = 'Michael Hopwood',
  author_email = 'mwhopwood@gmail.com',
  url = 'https://github.com/MichaelHopwood/PVPolyfit',
  download_url = 'https://github.com/MichaelHopwood/PVPolyfit/archive/v_04.tar.gz',
  keywords = ['Multiple linear regression', 'Multiple linear', 'PV', 'Photovoltaic', 'solar'],
  install_requires=[
          'numpy',
          'matplotlib',
          'datetime',
          'pandas',
          'sklearn',
          'pvlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

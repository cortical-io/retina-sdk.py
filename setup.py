from setuptools import setup, find_packages
import retinasdk

long_description = """
**Cortical.io's Retina API** allows the user to perform semantic operations on text. One can 
for example:

* measure the semantic similarity between two written entities
* create a semantic classifier based on positive and negative example texts
* extract keywords from a text
* divide a text into sub-sections corresponding to semantic changes
* extract terms from a text based on part of speech tags

The meaning of terms and texts is stored in a sparse binary representation that allows the user to apply logical 
operators to refine the semantic representation of a concept.

You can read more about the technology at the `documentation page <http://documentation.cortical.io/intro.html>`_.

To access the API, you will need to register for an `API key  <http://www.cortical.io/resources_apikey.html>`_.
"""

setup(
    name='retinasdk',
    version=retinasdk.__version__,
    description="Client library for accessing Cortical.io's Retina API.",
    long_description=long_description,
    keywords='semantic text processing language',
    url='https://github.com/cortical-io/retina-sdk.py',
    author='cortical.io Team',
    author_email='teamvienna@cortical.io',
    license='BSD',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
      ],
)

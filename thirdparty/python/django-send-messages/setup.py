# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'django-send-messages',
    version = '1.0.0',
    license='BSD',
    description = 'A simple API to send messages, includes Yunpian backend and Wechat(weixin) backend.',
    long_description=open('README.md').read(),
    author='Leon Liu',
    author_email='liuyong@hwbuluo.com',
    url='https://github.com/hwbuluo/django-send-messages',
    packages=find_packages(),
    include_package_data=True,
    extras_require = {
      'django': ['Django'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

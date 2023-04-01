from setuptools import setup, find_packages

setup(
    name='django-model-history-tracker',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django utility to track changes to model instances and save the history of updates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django_model_history_tracker',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='django model history tracker auditing',
    install_requires=[
        'Django>=2.2',
    ],
)
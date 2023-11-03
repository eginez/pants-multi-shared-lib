from setuptools import setup, find_packages

print(find_packages())
setup(
    name='desk-dist',
    version='1.0',
    #packages=['core', 'apps'],
    packages=find_packages(exclude=("apps",)),
    #packages=find_packages(),  # This will discover all Python packages in your project directory
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)
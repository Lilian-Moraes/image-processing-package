from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open ("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='image-processing-package',  # Nome do pacote
    version='0.0.1',  # Versão do seu pacote
    author='Lilian-Moraes',  # Nome
    author_email='lilianfranca@hotmail.com',  # Email
    description='Image Processing Package',  # Uma breve descrição
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lilian-Moraes/image-processing-package",
    packages=find_packages(),  # Encontra automaticamente os pacotes
    install_requires=requirements,  # Dependências do seu pacote
    python_requires='>=3.5'
)


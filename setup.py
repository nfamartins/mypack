#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 18:58:01 2023

@author: nfamartins
"""
from setuptools import setup, find_packages

setup(
    name="mypack",
    version="0.0",
    description="Um pacote com funções (não tão) úteis. Um teste para criação de pacotes",
    author="Nath",
    author_email="nathalia@akaua.com.br",
    packages=find_packages(),
		install_requires=[
        'pandas',
        'numpy'
    ],
)

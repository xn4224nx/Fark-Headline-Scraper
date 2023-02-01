# Fark Headline Scraper

## Introduction

This package is designed to retrieve the headline and their associated metadata
from the website [Fark.com](https://www.fark.com/). It is designed to search
the archive site linked [here](https://www.fark.com/archives/) and extract 
the link's metadata.

The aim of this package is to create a machine learning dataset for use in text
classification and clustering problems in future problems. 

## Package Development Plan

The general plan for the package development is as follows:

1) Access the website
2) Download all the archive html pages
3) Parse the webpage data and extract the headline data
4) Save the data to disk in a structured format.

There are also other ongoing tasks during development to create a fully rounded
packages. Primaraly the creation of documentation, mainly docstrings for usage 
by Sphinx.

Another background task will be the creation of unit tests for each created 
function.  
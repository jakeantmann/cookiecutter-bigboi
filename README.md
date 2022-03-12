<!-- markdownlint-disable MD014 -->

# Cookiecutter BigBoi

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) combining all the best QA features I can find for developing python packages.

## 🛠️ Getting Started

1. Install `cookiecutter` with:

    ```shell
    $ pip install cookiecutter
    ```

2. Run `cookiecutter` with:

    ```shell
    $ cookiecutter https://github.com/jakeantmann/cookiecutter-bigboi
    ```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers, and underscores.

4. If you're working under version control, copy the repository into your folder tracked under git, commit the files, and push to your remote.

## ❓ Why make the biggest boi?

As a learning project! I'm building a python package + corresponding cookiecutter, with the following goals:

- Learn about the various tools and best practises for python package development
- Familiarise myself with CI
- Learn to use cookiecutter for future templating needs

To achieve these goals, I am adding as many interesting-looking tools as possible to my package, especially QA tools like linters, testers etc. These all get added to this cookiecutter, along with reference files that I might find useful - eg an example test file with various methods of testing that I add as I go.

## 💪 Current features

- src layout
  - TODO Add link to explainer
- Large, versatile .gitignore that should cover most data science-related purposes. Includes a link to the site used to build it.
- Several open-source licenses
  - TODO Add link to explainer
- Configuration with pyproject.toml and setup.cfg
  - TODO: Add links to explainer/documentation for notation + each part
  - TODO: Move metadata to pyproject.toml
- Test orchestration with tox
  - TODO Add link to explainer
  - Package metadata completeness checked with pyroma
    - TODO Link to documenation
  - Config linting with Nitpick
    - TODO Link to documentation
  - Docstring coverage checked with docstr-coverage
    - TODO Link to documentation + alternative
  - Linting with flake8 (wemake-python-styleguide)
    - TODO Add links to explainer/documentation. Justify wemake as choice
  - Testing with pytest
    - TODO Link to documentation
  - Type hint checks with mypy
    - TODO Link to documentation
- CI with GitHub Actions
  - .github folder with basic workflow
    - TODO Ask about python versions (min, max) + OSs
    - TODO Add link to explainer

## 🏃 Upcoming features

### 📖 Documentation

- Template readme upgrades
  - Badges for everyone!
  - Other important sections (need to research)
- Prevent empty package names etc
- This readme
  - Steps for what to do after you've run cookiecutter:
    - Metadata (TODO move from setup.cfg to pyproject.toml)
    - [classifiers](https://pypi.org/classifiers/)
      - Development Status changes
      - Environment(s)
      - Intended Audience(s)
      - Operating System(s)
      - Framework(s)
      - Python version(s)
    - Keywords
  - Add further explanations for my choices
- A directory structure

### 🔨 Tools

- pre-commit
- Code coverage (need to research - coveragepy?)
- bump(2)version (Version management)
- click (cmd line tool builder) (including badge?)
- PyPi
  - automatically push latest code to PyPi, a standard Python public code library
  - Link to docs (can this be automated?)
- Documentation
  - sphinx
  - readTheDocs
  - Add to tox
  - Add documentation status badge [![https://readthedocs.org/projects/df_typecheck/badge/?version=latest](https://df_typecheck.readthedocs.io/en/latest/?badge=latest)](Documentation Status - readthedocs)
- BitBucket Pipeline integration

## 🔭 Future exploration

### 📁 Generic files

- Contributing.md (See contributor covenant badge)
- Code of conduct

### 🧦 More linting tools

- [import-linter](https://import-linter.readthedocs.io/en/stable/) checks your intra-package imports
- [dlint](https://github.com/dlint-py/dlint) checks security and coding best practises - complements bandit
- [Flakehell](https://wemake-python-stylegui.de/en/0.16.0/pages/usage/integrations/flakehell.html) Legacy-first linting
- [bellybutton](https://github.com/hchasestevens/bellybutton) custom, project-specific linting using regex or ast

### ❓ Other tools to consider using

These tools might be included for reporting purposes. Those reports might be automateable or made simpler by including them in a template.

- [Cohesion](https://github.com/mschwager/cohesion) Checks class cohesion. Use as a reporting tool
- [vulture](https://github.com/jendrikseipp/vulture) finds unused code

## 🍪 Cookiecutter Acknowledgement

This package was created with [@audreyr](https://github.com/audreyr)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter). I've learned a lot and included bits and pieces from the following cookiecutters:

- [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [cookiecutter-snekpack](https://github.com/audreyfeldroy/cookiecutter-pypackage) (this was a big inspiration - check out the accompanying blog posts etc., lots of useful information)
- [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)

and others. If you want more inspiration, check out this [list of alternative cookiecutters](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates)

## ⚖️ License

This cookiecutter package is licensed under the MIT License.

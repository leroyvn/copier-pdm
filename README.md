# Copier template for PDM projects

[Copier](https://github.com/copier-org/copier) template for projects managed with [PDM](https://pdm.fming.dev/).
Inspired by [Frost Ming](https://github.com/pdm-project/copier-pdm)'s and [pawamoy](https://github.com/pawamoy/copier-pdm)'s templates.

## Features

* **Package manager**:
  This template uses [PDM](https://pdm.fming.dev/), pre-configured in `pyproject.toml`.
* **Tests**:
  Tests run with [pytest](https://pytest.org/) ([xdocstest](https://xdoctest.readthedocs.io/) plugin activated).
  Multi-environment testing is implemented with [Nox](https://nox.thea.codes/).
* **Documentation**:
  An optional documentation template can be generated.
  It uses [Sphinx](https://sphinx-doc.org/) ([Furo](https://pradyunsg.me/furo/) theme, [MyST parser](https://myst-parser.readthedocs.io/) plugin activated).
  Default API documentation is generated using a recursive `autosummary` setup.
  Writing docstrings with the [Numpydoc](https://numpydoc.readthedocs.io/) format is encouraged.
* **CI and automation**
  GitHub Actions are configured and will automatically execute tests upon commit (except for draft PRs).
  By default, automatic upload to PyPI is active upon tagging.

## Requirements

* Python 3
* Git
* Copier

## References and notes

* Good practice guide: [Scikit-HEP dev guide](https://scikit-hep.org/developer)
* Use PEP 621 (metadata in `pyproject.toml`) and a compatible build backend (options: PDM with [pdm-publish](https://github.com/branchvincent/pdm-publish), [Flit](https://flit.readthedocs.io/en/latest/), setuptools through [ppsetuptools](https://github.com/TheCleric/ppsetuptools))
* About version capping: <https://iscinumpy.dev/post/bound-version-constraints/#tldr>

## Roadmap

* [ ] Replace coverage fail threshold with badge (*e.g.* using [genbadge](https://smarie.github.io/python-genbadge/))
* [ ] Add publication to Anaconda Cloud
* [ ] Add pre-commit hooks
* [ ] Replace makefile-based tasks with PDM tasks
* [x] Add publication to PyPI
* [x] Add Read the Docs configuration file template

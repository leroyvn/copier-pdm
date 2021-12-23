# Copier template for PDM projects

[Copier](https://github.com/copier-org/copier) template for projects managed with [PDM](https://pdm.fming.dev/). Inspired by [Frost Ming](https://github.com/pdm-project/copier-pdm)'s and [pawamoy](https://github.com/pawamoy/copier-pdm)'s templates.

## To do

- [ ] Add `copier.yml` based on existing templates
- [ ] Add `pyproject.toml` template
- [ ] Document option to use an env manager
- [ ] Add Conda dependency lock using [conda-lock](https://github.com/conda-incubator/conda-lock) (supports PEP 621 AFAIK, can also lock reliably Pip deps using the Poetry solver)
- [ ] Implement task automation with [duty](https://github.com/pawamoy/duty)
- [ ] Add documentation framework: Sphinx with [Furo theme](https://pradyunsg.me/furo/), [Numpy docstring format](http://numpydoc.readthedocs.io/)
- [ ] Add tools: isort, Black, mypy, flake8 (and pre-commit hooks)
- [ ] Add testing framework: pytest (with [xdoctest](https://github.com/Erotemic/xdoctest), [coverage](https://coverage.readthedocs.io/en/6.2/)), [nox](https://nox.thea.codes/en/stable/)
- [ ] Add changelog management: generate from commits using [git-changelog](https://github.com/pawamoy/git-changelog)
- [ ] CI: GitHub Actions, Read the Docs

## Desing notes

- Good practice guide: [Scikit-HEP dev guide](https://scikit-hep.org/developer)
- Use PEP 621 (metadata in `pyproject.toml`) and a compatible build backend (options: PDM with [pdm-publish](https://github.com/branchvincent/pdm-publish), [Flit](https://flit.readthedocs.io/en/latest/), setuptools through [ppsetuptools](https://github.com/TheCleric/ppsetuptools))
- About version capping: https://iscinumpy.dev/post/bound-version-constraints/#tldr

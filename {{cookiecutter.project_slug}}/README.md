# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

# TODO: Create pypi project for `release` job to work:  https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/ `Workflow name: build.yml` `Environment name: release`

## Features

* Feature 1
* Feature 2
* ...

## Development

For details on setting up the development environment and contributing, see CONTRIBUTING.md.

## Credits

This package was created with [The Hatchlor] project template.

[The Hatchlor]: https://github.com/bartosz121/the-hatchlor
[hatch]: https://hatch.pypa.io/
{%- if cookiecutter.lock_file_support %}
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
{%- endif %}

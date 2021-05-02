# Car UI Demo

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=for-the-badge)](#contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/DylanGore-FYP/car-ui-demo/Lint%20Code?label=Lint%20Status&logo=github&style=for-the-badge)](https://github.com/DylanGore-FYP/car-ui-demo/actions/workflows/lint.yml)

A proof of concept and demonstration UI for the in-vehicle portion of the project - [https://github.com/DylanGore-FYP/Car](https://github.com/DylanGore-FYP/Car).

## Requirements

- Python 3
- [eel](https://github.com/ChrisKnott/Eel)
- [chromedriver](https://chromedriver.chromium.org/)
- [Chromium Browser](https://www.chromium.org/Home) (Linux Only)

**Note:** The Chromium browser is required on Linux as it is possible to programmatically launch it in full screen mode whereas this was not working when using ChromeDriver. The code can be modified to use ChromeDriver on Linux if required.

## Running

```bash
pip3 install -r requirements.txt
```

```bash
python3 demo_ui.py
```

## Commit Message Convention

This project uses [Gitmoji](https://gitmoji.dev/) for commit organisation. For more details see the [Gitmoji Repository](https://github.com/carloscuesta/gitmoji).

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/DylanGore"><img src="https://avatars.githubusercontent.com/u/2760449?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dylan Gore</b></sub></a><br /><a href="https://github.com/DylanGore-FYP/car-ui-demo/commits?author=DylanGore" title="Code">💻</a> <a href="https://github.com/DylanGore-FYP/car-ui-demo/commits?author=DylanGore" title="Documentation">📖</a> <a href="#ideas-DylanGore" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/mohittaneja7"><img src="https://avatars.githubusercontent.com/u/4126813?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohit Taneja</b></sub></a><br /><a href="#ideas-mohittaneja7" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.

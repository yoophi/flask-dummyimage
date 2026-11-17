Dependabot security maintenance
===============================

Review date: 2026-11-17. Scope: PR #17, all earlier Dependabot PRs in
``yoophi/flask-dummyimage``, and all pages of the repository's open alerts.

Findings and response
---------------------

There were 101 open alerts affecting 11 distinct packages in ``uv.lock``.
The replacement lock file contains no version matching any of those 101
GitHub advisory ranges. Alerts are not dismissed: GitHub must re-evaluate
the default branch after the update is merged.

.. list-table:: Patched locked versions
   :header-rows: 1

   * - Package
     - Locked version
   * - Pillow
     - 13.0.0
   * - urllib3
     - 2.8.0
   * - cryptography
     - 50.0.2
   * - Werkzeug
     - 3.1.9
   * - virtualenv
     - 21.15.7
   * - filelock
     - 4.2.10
   * - certifi
     - 2026.10.23
   * - idna
     - 3.20
   * - requests
     - 2.34.2
   * - Pygments
     - 2.21.0
   * - pytest
     - 9.2.0

The original PR upgraded urllib3 to 2.7.0 but also selected Requests 2.15.1
and Twine 1.15.0 on Python 3.9. These fallback versions are removed.
The current urllib3 advisories require 2.8.0, and the current Pillow
advisories require 13.0.0. Pillow 13 requires Python >=3.11, so the project
now requires Python >=3.11 rather than silently keeping vulnerable packages
for older interpreters. Published runtime requirements include patched
Pillow and Werkzeug floors; uv constraints protect development dependencies.

Earlier PR history
------------------

* #1 (Flask 1.0) and #4 (Pillow 8.3.2) were merged in 2021.
* #2 and #3 (earlier Pillow fixes), #5 (pip), #6, #7 and #8 (Pillow),
  and #9 (wheel) were already closed without merging. Their old versions
  are not restored; the current dependency and build-tool configuration
  supersedes those historical upgrades.
* #11 and #14 (cryptography 46.0.5 / 46.0.6) were already closed without
  merging. #16 (46.0.7) remained open, but is superseded by 50.0.2 here.
* #15 (Pygments 2.20.0) remained open, but is superseded by 2.21.0 here.
* #17 is expanded into this combined security update instead of merging
  stale, overlapping lock-file updates separately.

Validation and ongoing checks
-----------------------------

* Seven PNG generation and sizing tests pass on Python 3.11 and 3.14.
* ``pip-audit`` reports zero known vulnerabilities in the exported locked
  runtime and development dependencies on both Python versions.
* Every locked version was compared with every applicable range in the
  101 original open GitHub alerts, including alternate Python resolutions.
* Source and wheel builds are checked. The wheel includes the bundled
  font and templates, and an installed-wheel PNG request is tested.
* Dependabot runs weekly and groups security updates.

Sources
-------

* `Repository security alerts <https://github.com/yoophi/flask-dummyimage/security/dependabot>`_
* `Dependabot PR #17 <https://github.com/yoophi/flask-dummyimage/pull/17>`_
* `Pillow 13 package metadata <https://pypi.org/project/pillow/13.0.0/>`_
* `urllib3 security advisories <https://github.com/urllib3/urllib3/security/advisories>`_

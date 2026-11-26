# Git Branching Strategy

## Branches

- `main`: Stable and deployable application code.
- `develop`: Integration branch for completed features.
- `feature/*`: Individual development tasks created from `develop`.

## Workflow

1. Create a feature branch from `develop`.
2. Implement and test the feature.
3. Commit changes with meaningful messages.
4. Push the feature branch to GitHub.
5. Open a pull request targeting `develop`.
6. Review the changes and add a genuine review comment.
7. Merge the pull request after verification.
8. Merge `develop` into `main` through a pull request when ready for release.

No direct development commits should be made to `main` or `develop`.

## Commit History

Maintain at least 10 meaningful commits. Preserve all feature branches, pull requests and Git history.

## Release Tags

- `v1.0.0`: Docker deployment verified.
- `v1.1.0`: Kubernetes deployment verified.

Both must be annotated tags.

## Recommendation for a Five-Person Team

Use a shared `develop` integration branch and separate feature branches for individual tasks. Protect `main` and `develop` with pull-request reviews and required checks where available. This helps team members work independently while keeping releases stable.

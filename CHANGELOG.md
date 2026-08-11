# CHANGELOG

<!-- version list -->

## v1.2.0 (2026-08-11)

### Features

- **database**: Add unique github_event_id to Event model and implement deduplication in event
  fetching
  ([`9513921`](https://github.com/pirlo47/Github-UserActivity/commit/9513921cec2685ead479d622556efa79c28664a2))


## v1.1.0 (2026-08-11)

### Chores

- **.gitignore**: Add entry for virtual environment files
  ([`3278645`](https://github.com/pirlo47/Github-UserActivity/commit/32786459ab1b6b07879ff68eb3e089901b22e16e))

- **database**: Add PostgreSQL database dump and initial schema setup
  ([`83a928c`](https://github.com/pirlo47/Github-UserActivity/commit/83a928c0b13b928fa9196b6fbcc8ba907bd40c68))

- **migrations**: Alembic successfully connected to your Postgres container and ran the migrations
  ([`3d11224`](https://github.com/pirlo47/Github-UserActivity/commit/3d112244988a75e0e236220973e5fe57905ca781))

### Features

- Add helper function to parse GitHub timestamps and integrate it into event creation
  ([`6c97bef`](https://github.com/pirlo47/Github-UserActivity/commit/6c97bef3804371a40dd749ff033e3c8807ffbd41))


## v1.0.0 (2025-08-27)

### Bug Fixes

- **githubActions**: Allow tagging and pushing
  ([`09708dc`](https://github.com/pirlo47/Github-UserActivity/commit/09708dc0746bdd0c912e8281644bc6ebfd3b1e73))

- **githubActions**: Ensures semnatic-release can see all commits & tags
  ([`e093862`](https://github.com/pirlo47/Github-UserActivity/commit/e0938621859921851ce78dc52fa15a6730d6b0cb))

### Chores

- Correct spelling of semantic-release in workflow steps
  ([`f40a71f`](https://github.com/pirlo47/Github-UserActivity/commit/f40a71fe3238c97256b9d4cf45bce9e0d67ec641))

- Python version to 3.13, supported release
  ([`b1a013d`](https://github.com/pirlo47/Github-UserActivity/commit/b1a013d8122a01ee05fef12e21496f513d5634aa))

- Update Python version to 3.14.0 in release workflow
  ([`65f6420`](https://github.com/pirlo47/Github-UserActivity/commit/65f6420a7835127e56af4d7fc4d24bfff0a6e995))

- Update release workflow and configuration for semantic-release
  ([`b8b9bc0`](https://github.com/pirlo47/Github-UserActivity/commit/b8b9bc0b2d9e5317e5c7c3beb18ae556e36238c4))

### Documentation

- Add Conventional Commit Cheat Sheet for semantic-release guidelines
  ([`ed895bf`](https://github.com/pirlo47/Github-UserActivity/commit/ed895bf15d7e5b3545345efd028262be9b070fdb))


## v0.0.0 (2025-08-27)

- Initial Release

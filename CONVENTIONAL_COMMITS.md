# 📝 Conventional Commit Cheat Sheet

This cheat sheet helps you write commit messages compatible with **semantic-release**, so your versioning is automatic.

---

## 🔹 Commit Message Format

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

- **type**: category of the change  
- **scope**: area of the project affected (optional)  
- **description**: short, imperative summary  

---

## 🔹 Types and Version Impact

| Type       | When to use                          | Version Bump |
|------------|-------------------------------------|--------------|
| `feat`     | New feature (backward-compatible)   | Minor        |
| `fix`      | Bug fix (backward-compatible)       | Patch        |
| `docs`     | Documentation only                  | None         |
| `style`    | Formatting, whitespace, etc.        | None         |
| `refactor` | Code change, not feature/fix        | None         |
| `test`     | Adding or modifying tests           | None         |
| `chore`    | Maintenance tasks (deps, scripts)   | None         |
| `BREAKING CHANGE` | Any breaking change           | Major        |

---

## 🔹 Examples

### Minor Release (feat → v0.0.x → v0.1.0)
```
feat(api): add endpoint to list user repositories
feat(events): add pagination support for user events
feat(db): integrate PostgreSQL for data storage
```

### Patch Release (fix → v0.1.0 → v0.1.1)
```
fix(api): handle missing user gracefully
fix(db): correct SQLite connection path
```

### Major Release (breaking change → v0.1.1 → 1.0.0)
```
feat!: switch database from SQLite to PostgreSQL
refactor(api)!: change event response format
```

### Other (no version bump)
```
docs(readme): update setup instructions
style: reformat code with black
test(events): add unit tests for event fetching
chore: update dependencies
```

---

## 🔹 Tips
- Keep subject line < 72 characters  
- Use **imperative mood**: “Add”, “Fix”, “Update”  
- Optional body can explain why the change was made  
- For breaking changes, either use `!` after type/scope or add `BREAKING CHANGE:` in the footer

---

## 🔹 Quick Reference Table

| Type       | Scope Example | Description Example                      | Version Bump |
|------------|---------------|-----------------------------------------|--------------|
| feat       | api           | add new user endpoint                     | Minor        |
| fix        | db            | correct unique constraint error          | Patch        |
| docs       | readme        | update setup instructions                 | None         |
| style      | -             | reformat code with black                  | None         |
| refactor   | events        | move event logic into separate service    | None         |
| test       | events        | add unit tests for fetching events        | None         |
| chore      | dependencies  | update dependencies                       | None         |
| feat!      | db            | switch SQLite → PostgreSQL                | Major        |

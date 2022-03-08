# Version control extensions

Git support is included out of the box, see https://code.visualstudio.com/docs/editor/versioncontrol

## Local History

When working on prototypes, it's difficult to commit often small changes. There are roughly two schools:

- Commit often in bulk with a "WIP" commit message. Then squash (or not!) the series of WIP commits before pushing to the remote repository.

- Not committing often, and then intermediate work can be lost if the code is not in a folder with frequent backups (DropBox, Time Machine etc).

For people not committing often, there is an extension that will save your life.

https://marketplace.visualstudio.com/items?itemName=xyz.local-history

Command: CTRL+P and `ext install xyz.local-history`

This extension will create a `.history` subfolder in any folder opened in VS Code, where copies of text files are regularly stored.

The extension adds a command `Local history: Show all` which enable the user to navigate to previous version of the current file.

It also adds a "LOCAL HISTORY" pane to the EXPLORER pane (first icon on the left). Clicking on any version opens a window highlighting the changes.

When installing this extension, one should additionally.

1. Exclude the `.history/` subfolder from the VS Code explorer by adding it to the `files.exclude` setting
  to the user JSON settings:

```json
    "files.exclude": {
        ".history/": true,
    },
```

2. Exclude the `.history/` subfolder from Git by adding the following line in `.gitignore`:
```
.history/
```

## Git History

A good extension for history navigation, both for the whole source code, or for an individual file.

Website: https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory

Command: CTRL+P and `ext install donjayamanne.githistory`

Example use:

CTRL+SHIFT+P, `Git: View History (git log)` to open the repository history window.

or try `Git: View File History` on an open file.

## GitHub Pull Requests and Issues

To contribute or maintain mature projects. Not necessary at first.

https://marketplace.visualstudio.com/items?itemName=GitHub.
vscode-pull-request-github

## Conventional commits

We'll discuss later how to use Commitizen to manage commit messages, version bumps and release notes.

TODO: link to the project management advice

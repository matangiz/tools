Roof Of Factories CLI Tool
======================================================

## Basic Usage
Directories structure under secure_factory_latest.tar downloaded file:

```
<secure_factory_latest.tar>
├── rof
│   ├── src
│   ├── hsm-luna
│   ├── hsm-db
│   └── version.properties
│   └── docker-compose.yml
│   └── rof.py
├── workstation
└── prod
└── docs
```


## Usage

This section describes detailed usages for each operation.

* [Start](#Starts root of factories services)
* [Create](#Creates root of factories certificate authority)
* [Sign](#Creates sign certificate using roof of factory certificate)
* [Stop](#Stops root of factories services)
* [Status](#Outputs status of the roof of factories services)



### Start root of factories services

For example,

```
$ notes new blog how-to-handle-files golang,file
```

```markdown
how-to-handle-files
===================
- Category: blog
- Tags: golang, file
- Created: 2018-10-28T07:19:27+09:00

```

Please do not remove `- Category: ...`, `- Tags: ...` and `- Created: ...` lines and title.
They are used by `notes` command (modifying them is OK).
Default title is file name. You can edit the title and body of note as follows:

```markdown
How to handle files in Go
=========================
- Category: blog
- Tags: golang, file
- Created: 2018-10-28T07:19:27+09:00

Please read documentation.
GoDoc explains everything.
```

Note that every note is under the category directory of the note. When you change a category of note,
you also need to adjust directory structure manually (move the note file to new category directory).

For more details, please check `notes new --help`.


###  Creates root of factories certificate authority

Let's say to open some notes you created.

You can show the list of note paths with:

```
$ notes list # or `notes ls`
```

For example, now there is only one note so it shows one path

```
/Users/me/.local/share/notes-cli/blog/how-to-handle-files.md
```

Note that `/Users/<NAME>/.local/share` is a default XDG data directory on macOS or Linux and you can
change it by setting `$NOTES_CLI_HOME` environment variable.

To open the listed notes with your editor, `--edit` (or `-e`) is a quickest way.

```
$ notes list --edit
$ notes ls -e
```



### Creates sign certificate using roof of factory certificate

`notes list` also can show brief of notes to terminal.

You can also show the full information of notes on terminal with `--full` (or `-f`) option.

```
$ notes list --full
```

For example,

```
/Users/me/.local/share/notes-cli/blog/how-to-handle-files.md
- Category: blog
- Tags: golang, file
- Created: 2018-10-28T07:19:27+09:00

How to handle files in Go
=========================

Please read documentation.
GoDoc explains everything.

```

It shows

- Full path to the note file
- Metadata `Category`, `Tags` and `Created`
- Title of note
- Body of note (up to 10 lines)

with colors.

When output is larger and whole output cannot be shown in screen at once, `list` does paging for the
output using `less` command (if available). This behavior can be customized by `$NOTES_CLI_PAGER`.

When there are many notes, it outputs many lines. In the case, a pager tool like `less` is useful
You can also use `less` with pipe explicitly to see the output per page. `-A` global option is short
of `--always-color`.

```
$ notes -A ls --full | less -R
```

When you want to see the all notes quickly, `--oneline` (or `-o`) may be more useful than `--full`.
`notes ls --oneline` shows one brief of note per line.

For example,

```
blog/how-to-handle-files.md golang,file How to handle files in Go
```

- 1st field indicates a relative path of note file from home directory with different colors.
  The first part of the path is the category in green, and the second part is the file name in yellow.
- 2nd field indicates comma-separated tags of the note. When note has no tag, it leaves as blank.
- 3rd field is the title of note

This is useful for checking many notes at a glance. When output is larger, `less` is used for paging
the output if available.

For more details, please see `notes list --help`.


### Stops root of factories services

You can create a template of note at each category directory or at root. When `.template.md` file
is put in a category directory or home, it is automatically inserted on `notes new`.

For example, when `HOME/minutes/.template.md` is created with following content:

```markdown
---

- Agenda: 
- Attendee: 


```

Executing `notes new minutes weekly-meeting-2018-11-07` will create a new note with inserting the
template like:

```markdown
weekly-meeting-2018-11-07
=========================
- Category: minutes
- Tags:
- Created: 2018-11-07T14:19:27+09:00

---

- Agenda: 
- Attendee: 
```

Template file at category directory is prioritized. For example, when `notes new minutes weekly-meeting-2018-11-07`
is run in following situation,

```
HOME
├── .template.md
└── minutes
    └── .template.md
```

`HOME/minutes/.template.md` is used rather than `HOME/.template.md`.


### Outputs status of the roof of factories services

Finally you can save your notes as revision of Git repository.

```
$ notes save
```

It saves all your notes under your `notes-cli` directory as Git repository.
It adds all changes in notes and automatically creates commit.

By default, it only adds and commits your notes to the repository. But if you set `origin` remote to
the repository, it automatically pushes the notes to the remote.

For more details, please see `notes save --help`.


### Configure behavior with environment variables

As described above, some behavior can be configurable with environment variables. Here is a table of
all environment variables affecting behavior of `notes`. Variables starting with `$NOTES_` are dedicated
for `notes` command. Others are general environment variables affecting `notes` behavior.
When you want to disable integration of Git, an editor or a pager, please set empty string to the
corresponding environment variable like `export NOTES_CLI_PAGER=`.

| Name                | Default                                    | Description                                                                |
|---------------------|--------------------------------------------|----------------------------------------------------------------------------|
| `$NOTES_CLI_HOME`   | `notes-cli` under [XDG data dir][xdg-dirs] | Home directory of `notes`. All notes are stored in sub directories         |
| `$NOTES_CLI_EDITOR` | None                                       | Your favorite editor command. It can contain options like `"vim -g"`       |
| `$NOTES_CLI_GIT`    | `"git"`                                    | Git command path. It is used for saving notes as Git repository            |
| `$NOTES_CLI_PAGER`  | `"less -R -F -X"`                          | Pager command for paging long output from `notes list`                     |
| `$XDG_DATA_HOME`    | None                                       | When `$NOTES_CLI_HOME` is not set, it is used for home                     |
| `$APPLOCALDATA`     | None                                       | Even if `$XDG_DATA_HOME` is not set, it is used for home on Windows        |
| `$EDITOR`           | None                                       | When `$NOTES_CLI_EDITOR` is not set, it is referred to pick editor command |
| `$PAGER`            | None                                       | When `$NOTES_CLI_PAGER` is not set, it is referred to pick pager command   |

You can see the configurations by `notes config` command.


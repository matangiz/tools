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

* [Start](#start)
* [Create](#flexibly-open-notes-you-created)
* [Sign](#check-notes-you-created-as-list)
* [Stop](#note-templates)
* [Status](#save-notes-to-git-repository)



### start

For example,

```
$ notes new blog how-to-handle-files golang,file
```

creates a note file at `<HOME>/notes-cli/blog/how-to-handle-files.md`. The home directory is automatically
created.

Category is `blog`. Every note must belong to one category. Category can be nested with `/`. For example,
if have multiple blogs Blog A and Blog B, you may want to categorize blog posts with categories like
`blog/A`, `blog/B`.

Tags are `golang` and `file`. Tags are labels to organize notes and to make search notes easier.
Tags can be omitted.

Category and file name cannot start with `.` not to make hidden files/directories.

If you set your favorite editor to `$NOTES_CLI_EDITOR` environment variable, it opens the newly
created note file with it. You can seamlessly edit the file. (If it is not set, `$EDITOR` is also
referred.)

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


###  Flexibly open notes you created

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

When there are multiple notes, note is output per line. So you can easily retrieve some notes from
them by filtering the list with `grep`, `head`, `peco`, `fzf`, ...

```
$ notes ls | grep -l file | xargs -o vim
```

Or following also works.

```
vim $(notes ls | xargs grep file)
```

And searching notes is also easy by using `grep`, `rg`, `ag`, ...

```
$ notes ls | xargs ag documentation
```

When you want to search and open it with Vim, it's also easy.

```
$ notes ls | xargs ag -l documentation | xargs -o vim
```

`notes ls` accepts `--sort` option and changes the order of list. By default, the order is created
date time of note in descending order. By ordering with modified time of note, you can instantly
open last-modified note as follows since first line is a path to the note most recently modified.

```
$ note ls --sort modified | head -1 | xargs -o vim
```

For more details, please check `notes list --help`.


### Check notes you created as list

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


### Note Templates

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


### Save notes to Git repository

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


### Extend `notes` command by adding new subcommands

Yes. Like [Git](https://git-scm.com/), `notes` command tries to run external subcommands when user
specifies unknown subcommand. For example, when entering `notes foo`, `notes` command notices that
it is not a built-in subcommand. Then it attempts to execute `notes-foo` with the same arguments.

Following arguments are passed to underlying external subcommand:

```
{full path to notes} {global options...} {subcommand} {local options...}
```

For example, let's say following script is put in your `$PATH` as `notes-hello`.

```sh
#!/bin/sh
echo "Hello! $*"
```

And hit `notes hello`. It outputs `Hello! /path/to/bin/notes hello` since given argument `hello` is
simply passed to executed underlying subcommand with full path of `notes`.
So, when hit `notes --no-color hello --foo`, it outputs `Hello! /path/to/bin/notes --no-color hello --foo`.
By forwarding all arguments, subcommand can refer global options specified before subcommand.

This external subcommand support is useful when you want to extend `notes` functionality to fit your
usage. For example:

- You can create your own command to upload your blog notes to your blog services.
- You can create your own alias command like `ls -o -s modified` -> `lsmod`.


### Shell Completions

- For zsh:

Please put `_notes` completion script to your completion directory.

```
$ git clone https://github.com/rhysd/notes-cli.git
$ cp nodes-cli/completions/zsh/_notes /path/to/completion/dir/
```

The completion directory must be listed in `$fpath`.

```
fpath=(/path/to/completion/dir $fpath)
```

- For bash:

Please add following line to your `.bashrc`.

```
$ eval "$(notes --completion-script-bash)"
```

- For fish:

Please add the completion script under `completions/fish/` to your completions directory.

```
$ git clone https://github.com/rhysd/notes-cli.git
$ cp nodes-cli/completions/fish/notes.fish ~/.config/fish/completions/
```


### Setup `man` manual

`notes` command can generate `man` manual file.

```
$ notes --help-man > /usr/local/share/man/man1/notes.1
```


### Update itself

`notes` has the ability to update the executable by itself.

```
$ notes selfupdate
```

Before updating, you can only check if the latest version is available by `--dry` option.


### Use from Go program

This command can be used from Go program as a library. Please read [API documentation][doc] to know
the interfaces.



## FAQ

### Can I specify `/path/to/dir` as home?

Please set it to environment variable.

```sh
export NOTES_CLI_HOME=/path/to/dir
```


### How can I grep notes?

Please combine grep tools with `notes list` on your command line. For example,

```sh
$ grep -E some word $(notes list)
$ ag some word $(notes list)
```

If you want to filter with categories or tags, please use `-c` and/or `-t` of `list` command.


### How can I filter notes interactively and open it with my editor?

Please pipe the list of paths from `notes list`. Following is an example with `peco` and Vim.

```sh
$ notes list | peco | xargs -o vim --not-a-term
```


### Can I open the latest note without selecting it from list?

Output of `notes list` is sorted by created date time by default. By using `head` command, you can
choose the latest note in the list.

```sh
$ vim "$(notes list | head -1)"
```

If you want to access to the last modified note, sorting by `modified` and taking first item by `head`
should work.

```sh
$ vim "$(notes list --sort modified | head -1)"
```

By giving `--sort` (or `-s`) option to `notes list`, you can change how to sort. Please see
`notes list --help` for more details.


### How can I remove some notes?

Please use `rm` and `notes list`. Following is an example that all notes of specific category `foo`
are removed.

```sh
$ rm $(notes list -c foo)
```

Thanks to Git repository, this does not remove your notes completely until you run `notes save`
next time.


### I don't want to show the metadata in note. Can I hide them?

Metadata can be commented out as follows:

```markdown
some title
==========
<!--
- Category: cat
- Tags:
- Created: 2018-11-09T02:14:27+09:00
-->

Body
```

The closing comment `-->` is not included in note body. Commented metadata are not rendered and read
only by `notes` command.


### Can I hide metadata by default?

Yes. When `.template.md` starts with `-->` (closing comment), `notes` automatically consider that you
expect to hide metadata and insert `<!--` proper position.

For example, if you have `category1/.template.md`,

```markdown
-->

```

`notes new` will create a new note as follows:

```markdown
some-title
==========
<!--
- Category: category1
- Tags:
- Created: 2018-11-15T23:14:27+09:00
-->

```


### How image resources are managed?

I recommend to create a directory for resources under home.

All non-markdown resources (are ignored by `notes` command. So you can freely put your `.png` or `.jpg`
files in the same directory as note markdown files.

Or you can use a separate directory dedicated for images like `HOME/images/` or `HOME/category1/images`.
This option may be better than mixing many pictures and note files in the same directory when you use
`grep`.

If you want to differentiate images directory from other category directories, please give `.` prefix
like `HOME/.images` since category directories cannot have `.` prefix as their names.


### Is it possible to use `--color-always` by default?

Please use shell's alias feature as follows:

```sh
alias notes='notes --color-always'
```


### How can I migrate from [memolist.vim](https://github.com/glidenote/memolist.vim)?

Please try [migration script](./scripts/migrate-from-memolist.rb).

```
$ git clone https://github.com/rhysd/notes-cli.git
$ cd ./notes-cli
$ ruby ./scripts/migrate-from-memolist.rb /path/to/memolist/dir /path/to/note-cli/home
```


### How can I integrate with Vim?

You can try [Vim plugin for notes-cli](https://github.com/rhysd/vim-notes-cli)

If you feel the plugin is too much, you can also try following configuration. Please write following
code in your `.vimrc`.

```vim
function! s:notes_grep(args) abort
    let idx = match(a:args, '\s\+\ze/[^/]\+/')
    if idx <= 0
        " When :NotesGrep /pat/
        let paths = join(split(system('notes list'), '\n'), ' ')
        execute 'vimgrep' a:args paths
        return
    endif

    " When :NotesGrep {args} /pat/
    let paths = join(split(system('notes list ' . a:args[:idx]), '\n'), ' ')
    if paths ==# ''
        echohl ErrorMsg | echo 'No file found' | echohl None
        return
    endif
    let pat = a:args[idx:]
    execute 'vimgrep' pat paths
endfunction
command! -nargs=+ NotesGrep call <SID>notes_grep(<q-args>)

function! s:notes_new(...) abort
    if has_key(a:, 1)
        let cat = a:1
    else
        let cat = input('category?: ')
    endif
    if has_key(a:, 2)
        let name = a:2
    else
        let name = input('filename?: ')
    endif
    let tags = get(a:, 3, '')
    let cmd = printf('notes new --no-inline-input %s %s %s', cat, name, tags)
    let out = system(cmd)
    if v:shell_error
        echohl ErrorMsg | echomsg string(cmd) . ' failed: ' . out | echohl None
        return
    endif
    let path = split(out)[-1]
    execute 'edit!' path
    normal! Go
endfunction
command! -nargs=* NotesNew call <SID>notes_new(<f-args>)

function s:notes_last_mod(args) abort
    let out = system('notes list --sort modified ' . a:args)
    if v:shell_error
        echohl ErrorMsg | echomsg string(cmd) . ' failed: ' . out | echohl None
        return
    endif
    let last = split(out)[0]
    execute 'edit!' last
endfunction
command! -nargs=* NotesLastMod call <SID>notes_last_mod(<q-args>)
```

- `:NotesGrep [args] /pat/`: It searches notes by `:vimgrep` with given `/pat/`. Thanks to `:vimgrep`,
  the search result is stored to a quickfix list. You can easily check matches and open the file from
  the list by open quickfix window with `:copen`.
- `:NotesNew [args]`: It creates a new note and opens it with a new buffer. `args` is the same as
  `notes new` but category and file name can be empty. In the case, Vim ask you to input them after
  starting the command.
- `:NotesLastMod [args]`: It opens the last modified note in new buffer. When `args` is given, it
  is passed to underlying `notes list` command execution so you can filter result by categories
  and/or tags with `-c` or `-t`.



## License

[MIT License](LICENSE.txt)




[ag]: https://github.com/ggreer/the_silver_searcher
[rg]: https://github.com/BurntSushi/ripgrep
[fzf]: https://github.com/junegunn/fzf
[peco]: https://github.com/peco/peco
[xdg-dirs]: https://wiki.archlinux.org/index.php/XDG_Base_Directory
[appveyor-badge]: https://ci.appveyor.com/api/projects/status/5pbcku1buw8gnqu9/branch/master?svg=true
[appveyor]: https://ci.appveyor.com/project/rhysd/notes-cli
[travisci-badge]: https://travis-ci.org/rhysd/notes-cli.svg?branch=master
[travisci]: https://travis-ci.org/rhysd/notes-cli
[codecov-badge]: https://codecov.io/gh/rhysd/notes-cli/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/rhysd/notes-cli
[doc-badge]: https://godoc.org/github.com/rhysd/notes-cli?status.svg
[doc]: http://godoc.org/github.com/rhysd/notes-cli

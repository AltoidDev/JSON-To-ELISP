# JSON To ELISP Converter
A python script to convert JSON files into ELISP configs for emacs.

* ELISP config files built to be viewed with org mode.
* Requires latest python:
  * Should work with versions >= 3.10, but only tested on 3.13.7 as of now.
  * In future, will only be tested on the latest version at the time.
---
How to use:

JSON config is written in standard JSON syntax.
Every entry in the base dict is treated as a "setting" in the config, with the key being the org mode header, and the value being the actual config. If something begins with #l, it becomes a literal (The script puts a ` before it)

For example:
```
{
  "Example setting":["example function","#lliteral"]
}
```
Would be converted to:
```
* Example setting
  #+BEGIN_SRC emacs-lisp
  (example function `literal)
  #+END_SRC
```


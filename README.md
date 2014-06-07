Sublime Parametrize
===================

> ### A plugin to add a Parametrize Command to Sublime Text


### About

This plugin for SublimeText adds a menu commands to "parametrize" the selected text.

### What does it do?


This function is named `parameterize` or `parametrize` in Rails and it:

> Replaces special characters in a string so that it may be used as part of a ‘pretty’ URL.

In Wordpress this is known as creating a "slug" and is done with the "sanitize_title" function:

	sanitize_title('This Long Title is what My Post or Page might be');

returns:

	this-long-title-is-what-my-post-or-page-might-be

### How do I use it?

1. Select text in Sublime Text
2. Open the command palette
3. Choose either `Parametrize` or `Parametrize with Underscore`
4. Your selection will be converted accordingly


### Notes


This is based on `transform.py` from the Sublime Default Commands package.


### How to Install

1. Install [Package Control for Sublime Text](https://sublime.wbond.net/installation)
2. Add this repository - [see notes on adding a repository](https://sublime.wbond.net/docs/usage)
3. From the command palette choose `install package` and then choose `Sublime Parametrize`
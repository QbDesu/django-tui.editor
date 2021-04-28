# Django-TUI.Editor

> Django WYSIWYG markdown editor that supports GFM

This is a django app that adds a markdown widget utilizing the [TOAST UI Editor](https://ui.toast.com/tui-editor/). Among other things it also adds a `MarkdownField` type that is an extension of the `TextField` but will use a WYSIWYG Markdown editor in the admin interface. The editor allows editing the markdown source code with a preview on the side.

## How it works

The module adds 3 widgets based on django's own widget API:

1. **MarkdownEditorWidget:** A WYSIWYG editor that also supports Markdown source code editing with syntax highlighting and a preview of the rendered implemented using the TOAST UI Editor
2. **MarkdownViewerWidget:** A markdown viewer also implemented using the TOAST UI Editor which falls back to statically rendered markdown
3. **StaticMarkdownViewerWidget:** A statically rendered markdown viewer that should work on all browsers without any javascript

## On NoScript support

The rendering supports both a fancy viewer and editor in script-enabled environments but allows falling back to statically rendered elements if scripts are not supported or disabled. For static rendering of the viewer the python bindings for Github's GFM Markdown implementation [cmark-gmf](https://github.com/github/cmark-gfm/) are used while the editor falls back to a simple text area input.

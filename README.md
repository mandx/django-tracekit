# django-tracekit

Django server-side support for [TraceKit](https://github.com/occ/TraceKit/)

## Features
- Record the exact stack information TraceKit gives.
- Browseable from the admin, expandable right in the error list.
- Bundled TraceKit.js and other JS libraries, but with configurable references for each one (other bundled libraries are [JSON3](http://bestiejs.github.com/json3/) and [reqwest](https://github.com/ded/reqwest); jQuery is only used in the admin interface and the version bundled with Django is used).
- The templatetag used to include the TraceKit initialization uses a template, so you can easily redefine how to initialize/load, post errors, etc.

## TODO
- Better display of the stack information in the admin changelist, like rendering a nice stack tree.
- Add Haystack search support

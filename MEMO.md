# Bottle Tutorial
Reference: [Tutorial](https://bottlepy.org/docs/dev/tutorial.html#installation)  
`@route()` decorator binds a piece of code to an URL path.  
`run()` call in the last line starts a built-in development server. stop comond -> ctrl+c  
`<name:fileter>`or`<name:filter:coonfig>`  
Example of filter:  

1. `:int` matches (signed) digits only and converts the value to integer.
1. `:float `similar to :int but for decimal numbers.
1. `:path` matches all characters including the slash character in a non-greedy way and can be used to match more than one path segment.
1. `:re `allows you to specify a custom regular expression in the config field. The matched value is not modified.

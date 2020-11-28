#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) How to add a command
    2) How to add help for that command
    3) Persistent history
    4) How to run an initialization script at startup
    5) How to add custom command aliases using the alias command
    6) Shell-like capabilities
"""
from thgcmd.thgcmd import ThgCmd, with_category, with_argparser


class BasicApp(ThgCmd):
    CUSTOM_CATEGORY = 'My Custom Commands'

    def __init__(self):
        super().__init__(persistent_history_file='thg_history.dat',
                         startup_script='scripts/startup.txt', use_ipython=True)

        self.intro =  ' 😀'

        # Allow access to your application in py and ipy via self
        self.self_in_py = True

        # Set the default category name
        self.default_category = 'thg Built-in Commands'

    with_category(CUSTOM_CATEGORY)
    def thg_intro(self, _):
        """Display the intro banner"""
        self.poutput(self.intro)

    with_category(CUSTOM_CATEGORY)
    def thg_echo(self, arg):
        """Example of a multiline command"""
        self.poutput(arg)


if __name__ == '__main__':
    app = BasicApp()
    app.cmdloop()
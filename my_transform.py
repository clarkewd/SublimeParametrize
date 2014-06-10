# run_multiple_commands.py
import string
import sublime
import sublime_plugin
import re

class MyTransformer(sublime_plugin.TextCommand):
    def run(self, edit):
        self.transform(self.transformer[0], self.view, edit)

    def transform(self, f, view, edit):
        for s in view.sel():
            if s.empty():
                s = view.word(s)

            txt = f(view.substr(s),self)
            view.replace(edit, s, txt)

    def my_parametrize(self,s,char):
        r = s.lower()
        r = re.sub('[^0-9a-zA-Z]+', char, r)
        r = r.strip( '-' )
        return r


class ParametrizeCommand(MyTransformer):
    transformer = lambda s,self: self.my_parametrize(s,'-'),

class ParametrizeWithUnderscoreCommand(MyTransformer):
    transformer = lambda s,self: self.my_parametrize(s,'_'),

class ParametrizeWithSpace(MyTransformer):
    transformer = lambda s,self: self.my_parametrize(s,' '),


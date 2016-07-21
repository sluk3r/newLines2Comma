import sublime, sublime_plugin,re

class N2cCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		vw = self.view
		region = sublime.Region(0, vw.size ())
		text = vw.substr(region)


		p = re.compile('\\n', re.VERBOSE)
		text = p.sub(',', text)

		vw.replace(edit, region, text)
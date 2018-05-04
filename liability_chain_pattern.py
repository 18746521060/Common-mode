#!/usr/bin/python3

# 责任链模式


class Event:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


class Widget:
	def __init__(self, parent=None):
		self.parent = parent

	def handle(self, event):
		handler = "Handle_{}".format(event)
		if hasattr(self, handler):
			method = getattr(self, handler)
			method(event)
		elif self.parent:
			self.parent.handle(event)
		elif hasattr(self, "handle_default"):
			self.handle_default(event)


class MainWindow(Widget):
	def handle_close(self, event):
		print("\n Send the event '{}' from handle_close to {}".format(event, self))

	def handle_default(self, event):
		print("\n Send the event '{}' from handle_default to {}".format(event, self))

	def __str__(self):
		return "MainWindow"


class SendDialog(Widget):
	def handle_paint(self, event):
		print("\nSend the event '{}' from handle_paint to {}".format(event, self))

	def __str__(self):
		return "SendDialog"


class MsgText(Widget):
	def handle_down(self, event):
		print("\nSend the event '{}' from handle_down to {}".format(event, self))

	def __str__(self):
		return "MsgText"


def main():
	mw = MainWindow()
	sd = SendDialog(mw)
	mt = MsgText(mw)

	for e in ("down", "paint", "unhandled", "close"):
		evt = Event(e)
		mw.handle(evt)
		print("-" * 50)
		sd.handle(evt)
		print("*" * 50)
		mt.handle(evt)
		print("#" * 50)


if __name__ == "__main__":
	main()

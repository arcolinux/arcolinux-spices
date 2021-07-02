#                #=======================================================
#                #=     Author: Brad Heffernan - Erik Dubois            =
#                #=======================================================

import gi
import os
import subprocess
import threading
import GUI
try:
    gi.require_version('Gtk', '3.0')
    gi.require_version('Gdk', '3.0')
except:  # noqa
    pass
from gi.repository import Gtk, Gdk, GLib  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class Spices(Gtk.Window):
    def __init__(self):
        super(Spices, self).__init__()
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)

        GUI.GUI(self, Gtk)

    def on_btn1_clicked(self, widget):
        line = ["pkexec", "sh", base_dir + "/scripts/get-the-keys-and-repos.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def run_script(self, command):
        with subprocess.Popen(command, bufsize=1, stdout=subprocess.PIPE, universal_newlines=True) as p:
            for line in p.stdout:
                GLib.idle_add(self.lbl_status.set_text, line.strip())


if __name__ == "__main__":
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path(base_dir + "/att.css")

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    w = Spices()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()

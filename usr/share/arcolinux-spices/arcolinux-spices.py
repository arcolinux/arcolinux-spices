
import gi
import os
import subprocess
import threading
import GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class Spices(Gtk.Window):
    def __init__(self):
        super(Spices, self).__init__()
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)

        GUI.GUI(self, Gtk)

    def on_btn1_clicked(self, widget):
        line = ["pkexec", "sh", base_dir + "/scripts/trust-key.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def on_btn2_clicked(self, widget):
        line = ["pkexec", "sh", base_dir + "/scripts/add-keyservers-for-key-importing.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def on_btn3_clicked(self, widget):
        line = ["pkexec", "sh", base_dir + "/scripts/add-arcolinux-repo-to-pacman-conf.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def on_btn4_clicked(self, widget):
        line = ["pkexec", "sh", base_dir + "/scripts/install-software-arcolinux-uses-in-bashrc.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def on_btn5_clicked(self, widget):
        line = ["sh", base_dir + "/scripts/get-the-latest-arcolinux-bashrc.sh"]
        t = threading.Thread(target=self.run_script, args=(line,))
        t.daemon = True
        t.start()

    def run_script(self, command):
        with subprocess.Popen(command, bufsize=1, stdout=subprocess.PIPE, universal_newlines=True) as p:
            for line in p.stdout:
                GLib.idle_add(self.lbl_status.set_text, line.strip())


if __name__ == "__main__":
    w = Spices()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()

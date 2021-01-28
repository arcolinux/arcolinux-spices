

def GUI(self, Gtk):

    # ========================================
    #               HEADER WINDOW
    # ========================================
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "ArcoLinux Spices Application"
    hb.props.subtitle = "Importing all ArcoLinux packages on Arch Linux"
    self.set_titlebar(hb)

    # ========================================
    #               MAIN WINDOW
    # ========================================
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_size_request(600, 200)
    self.add(vbox)

    # ========================================
    #               GLOBALS
    # ========================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # ========================================
    #               BUTTONS
    # ========================================

    btn1 = Gtk.Button(label="1. Fix keyserver connection")
    btn2 = Gtk.Button(label="2. Add and trust ArcoLinux key (takes a while)")
    btn3 = Gtk.Button(label="3. Add ArcoLinux repos")
    btn4 = Gtk.Button(label="4. Add software used in .bashrc")
    btn5 = Gtk.Button(label="5. Improve /etc/makepkg.conf")
    btn6 = Gtk.Button(label="6. Install polkit agent")
    btn7 = Gtk.Button(label="7. Get the latest ArcoLinux .bashrc and replace current one")


    btn1.connect("clicked", self.on_btn1_clicked)
    btn2.connect("clicked", self.on_btn2_clicked)
    btn3.connect("clicked", self.on_btn3_clicked)
    btn4.connect("clicked", self.on_btn4_clicked)
    btn5.connect("clicked", self.on_btn5_clicked)
    btn6.connect("clicked", self.on_btn6_clicked)
    btn7.connect("clicked", self.on_btn7_clicked)

    hbox1.pack_start(btn1, True, True, 0)
    hbox2.pack_start(btn2, True, True, 0)
    hbox3.pack_start(btn3, True, True, 0)
    hbox4.pack_start(btn4, True, True, 0)
    hbox5.pack_start(btn5, True, True, 0)
    hbox6.pack_start(btn6, True, True, 0)
    hbox7.pack_start(btn7, True, True, 0)

    self.lbl_status = Gtk.Label(label="Application to import ArcoLinux packages on Arch Linux")
    self.lbl_nonroot = Gtk.Label(label="Run this as user")
    self.lbl_root = Gtk.Label(label="Run these as root")

    vbox.pack_start(self.lbl_root, False, False, 0)
    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_start(hbox2, False, False, 0)
    vbox.pack_start(hbox3, False, False, 0)
    vbox.pack_start(hbox4, False, False, 0)
    vbox.pack_start(hbox5, False, False, 0)
    vbox.pack_start(hbox6, False, False, 0)
    vbox.pack_start(self.lbl_nonroot, False, False, 0)
    vbox.pack_start(hbox7, False, False, 0)
    vbox.pack_end(self.lbl_status, False, False, 0)

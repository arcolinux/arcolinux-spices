

def GUI(self, Gtk):

    # ========================================
    #               HEADER WINDOW
    # ========================================
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "ArcoLinux Spices Application"
    hb.props.subtitle = "bring in all the spices for ArcoLinux"
    self.set_titlebar(hb)

    # ========================================
    #               MAIN WINDOW
    # ========================================
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    self.add(vbox)

    # ========================================
    #               GLOBALS
    # ========================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # ========================================
    #               BUTTONS
    # ========================================

    btn1 = Gtk.Button(label="Add pacman repos")
    btn2 = Gtk.Button(label="Add bashrc software")
    btn3 = Gtk.Button(label="Add keyserver")
    btn4 = Gtk.Button(label="Add trust key")

    btn1.connect("clicked", self.on_btn1_clicked)
    btn2.connect("clicked", self.on_btn2_clicked)
    btn3.connect("clicked", self.on_btn3_clicked)
    btn4.connect("clicked", self.on_btn4_clicked)

    hbox1.pack_start(btn1, True, True, 0)
    hbox1.pack_start(btn2, True, True, 0)
    hbox1.pack_start(btn3, True, True, 0)

    hbox2.pack_start(btn4, False, False, 0)

    self.lbl_status = Gtk.Label(label="TESTING")

    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_start(hbox2, False, False, 0)
    vbox.pack_end(self.lbl_status, False, False, 0)

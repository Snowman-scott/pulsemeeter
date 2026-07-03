import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    
    scale = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL)
    scale.set_range(0, 100)
    scale.set_value(50)
    scale.set_draw_value(True)
    scale.set_format_value_func(lambda s, v: "-31.45\ndB")
    
    child = scale.get_first_child()
    while child is not None:
        print("Found child:", type(child))
        if hasattr(child, 'set_justify'):
            child.set_justify(Gtk.Justification.CENTER)
            print("Set justify!")
        child = child.get_next_sibling()

    box.append(scale)
    win.set_child(box)
    win.present()

app = Gtk.Application(application_id='com.test.child')
app.connect('activate', on_activate)
app.run(None)

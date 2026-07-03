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
    scale.set_format_value_func(lambda s, v: "-120.45 dB")
    
    css = b"scale > value { font-size: 10px; }"
    provider = Gtk.CssProvider()
    provider.load_from_data(css)
    ctx = scale.get_style_context()
    ctx.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
    box.append(scale)
    win.set_child(box)
    win.present()

app = Gtk.Application(application_id='com.test.css')
app.connect('activate', on_activate)
app.run(None)

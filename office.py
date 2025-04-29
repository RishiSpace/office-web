import gi

# Try importing GTK 4 first, fall back to GTK 3 if not available
try:
    gi.require_version('Gtk', '4.0')
    gi.require_version('WebKit', '6.0') # WebKit for GTK 4
    from gi.repository import Gtk, WebKit
    print("Using GTK 4 and WebKit 6")
    GTK_VERSION = 4
except ValueError:
    try:
        gi.require_version('Gtk', '3.0')
        gi.require_version('WebKit2', '4.0') # WebKit2 for GTK 3
        from gi.repository import Gtk, WebKit2 as WebKit
        print("Using GTK 3 and WebKit2 4")
        GTK_VERSION = 3
    except ValueError:
        print("Neither GTK 4/WebKit 6 nor GTK 3/WebKit2 4 found. Please install them.")
        exit()

# Define the URL you want to wrap
WEBSITE_URL = "https://office.com/signin" # You can change this to any URL

def create_webview_window(app):
    """Creates the main application window with a WebView."""

    # Create a new window
    if GTK_VERSION == 4:
        window = Gtk.ApplicationWindow.new(app) # For GTK 4, window needs an application
    else:
        window = Gtk.Window() # For GTK 3

    window.set_title("Microsoft Excel (Online)") # Set the window title
    window.set_default_size(800, 600) # Set default window size

    # Create a WebView widget
    webview = WebKit.WebView()

    # Load the specified URL
    webview.load_uri(WEBSITE_URL)

    # Add the WebView to the window
    if GTK_VERSION == 4:
        window.set_child(webview) # For GTK 4, use set_child
    else:
        window.add(webview) # For GTK 3, use add

    # Connect the 'destroy' signal to quit the GTK main loop
    # This ensures the application exits when the window is closed
    if GTK_VERSION == 3:
        window.connect("destroy", Gtk.main_quit)

    # Show all widgets in the window (GTK 3) or present the window (GTK 4)
    if GTK_VERSION == 3:
        window.show_all()
    elif GTK_VERSION == 4:
        window.present()


if __name__ == "__main__":
    if GTK_VERSION == 4:
        # For GTK 4, create a Gtk.Application
        app = Gtk.Application()
        # Pass the application instance to the window creation function
        app.connect("activate", create_webview_window)
        app.run(None)
    else:
        # For GTK 3, just call the function and start the main loop
        create_webview_window(None) # Pass None as app for GTK 3
        Gtk.main() # Start the GTK main loop


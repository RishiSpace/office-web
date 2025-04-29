# Office Web App for Linux

**Introduction**
===============

This Python application utilizes the GTK library to create a web browser window. The application attempts to use GTK 4 with WebKit 6, falling back to GTK 3 with WebKit2 4 if the primary option is not available. The main functionality is to load a specified URL (in this case, Microsoft Excel online) into the web view.

**Overview of the Application Structure**
-----------------------------------------

The application is structured into the following main components:

*   **GTK Version Detection**: The application first attempts to import GTK 4 and WebKit 6. If this fails, it falls back to GTK 3 and WebKit2 4.
*   **Window Creation**: A function is defined to create the main application window with a web view. This function takes an application instance as a parameter (for GTK 4) or `None` (for GTK 3).
*   **Main Application Loop**: The application enters its main loop, where it waits for events and updates the GUI.

**Detailed Functionality**
-------------------------

### create_webview_window Function

*   **Purpose**: Creates the main application window with a web view.
*   **Parameters**:
    *   `app`: The application instance (for GTK 4) or `None` (for GTK 3).
*   **Functionality**:
    *   Creates a new window with a specified title and default size.
    *   Creates a web view widget and loads the specified URL.
    *   Adds the web view to the window.
    *   Connects the 'destroy' signal to quit the GTK main loop (for GTK 3).
    *   Shows all widgets in the window (GTK 3) or presents the window (GTK 4).

### GTK Version Detection and Fallback

*   **Purpose**: Attempts to import GTK 4 and WebKit 6, falling back to GTK 3 and WebKit2 4 if necessary.
*   **Functionality**:
    *   Tries to import GTK 4 and WebKit 6. If successful, sets `GTK_VERSION` to 4.
    *   If the above fails, tries to import GTK 3 and WebKit2 4. If successful, sets `GTK_VERSION` to 3.
    *   If both attempts fail, prints an error message and exits the application.

### Main Application Loop

*   **Purpose**: Enters the main application loop, waiting for events and updating the GUI.
*   **Functionality**:
    *   For GTK 4, creates a `Gtk.Application` instance and connects the "activate" signal to the `create_webview_window` function.
    *   For GTK 3, calls the `create_webview_window` function with `None` as the application instance and starts the GTK main loop using `Gtk.main()`.
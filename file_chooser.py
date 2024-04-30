import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def choose_file():
    native = Gtk.FileChooserNative(
        title="Open File",
        action=Gtk.FileChooserAction.OPEN,
        accept_label="_Open",
        cancel_label="_Cancel",
    )

    pdf_filter = Gtk.FileFilter()
    pdf_filter.set_name("PDF files")
    pdf_filter.add_mime_type("application/pdf")
    native.add_filter(pdf_filter)

    response = native.run()
    if response == Gtk.ResponseType.ACCEPT:
        file_path = native.get_filename()
    else:
        file_path = None
    native.destroy()
    return file_path

if __name__ == "__main__":
    file_path = choose_file()
    if file_path is not None:
        print("Chosen file:", file_path)
    else:
        print("No file selected.")

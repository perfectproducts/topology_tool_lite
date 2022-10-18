import omni.ext
import omni.ui as ui
from omni.kit.window.filepicker import FilePickerDialog

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def import_topology_from_excel(stage, path):
    print(f"import topology from excel {path}")
    

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def show_xls_load_dialog(self): 
        heading = "Select Xls File..."
        dialog = FilePickerDialog(
            heading,
            allow_multi_selection=False,
            apply_button_label="select excel file",
            click_apply_handler=lambda filename, dirname: self.on_excel_file_selected(dialog, dirname, filename),
            file_extension_options = [("*.xlsx", "Excel")]            
        )            
        dialog.show()

    def on_excel_file_selected(self, dialog, dirname:str, filename: str):        
        print(f"selected {filename}")
        filepath = f"{dirname}/{filename}"
        if filename.endswith(".xlsx"):            
            import_topology_from_excel(omni.usd.get_context().get_stage(), filename)
        dialog.hide()    
    

    def on_startup(self, ext_id):
        print("[ai.synctwin.topology_tool_lite] startup")

        self._count = 0

        self._window = ui.Window("SyncTwin Topology Tool Lite", width=300, height=100)
        with self._window.frame:
            with ui.VStack():
                
                def on_import_excel_clicked():
                    self.show_xls_load_dialog()
                    
                def on_export_excel_clicked():
                    pass 

                
                ui.Button("Import Xls...", clicked_fn=on_import_excel_clicked, height=30)
                ui.Button("Export Xls...", clicked_fn=on_export_excel_clicked, height=30)

    def on_shutdown(self):
        print("[ai.synctwin.topology_tool_lite] MyExtension shutdown")

import maya.cmds as cmds
import maya.mel as mel

# BICK Export Import Tool
# Temp_mesh file path
path = r"C:/temp/temp_mesh.obj"

# Get select shelf tab path
gShelfTopLevel = mel.eval('$temp=$gShelfTopLevel')
shelf_tab_name = cmds.shelfTabLayout(gShelfTopLevel, query=True, selectTab=True)
shelf_tab_path = gShelfTopLevel+'|'+shelf_tab_name


# Create shelf button on select tab
def create_shelf_button(
                    command = '',
                    annotation = '',
                    name = '',
                    image = '',
                    label_name = '',
                    label_color = (1,0.487,0.487),
                    label_transparency = 0.7
                    ):

    if not name:
        name = label_name
        
    if not image:
        image = 'render_useBackground'

    return cmds.shelfButton(
                        command = command,
                        annotation = annotation,
                        label = name,
                        parent = shelf_tab_path,
                        image = image,
                        width = 32,
                        height = 32,
                        align = 'center',
                        imageOverlayLabel = label_name,
                        overlayLabelColor = label_color,
                        overlayLabelBackColor = (0,0,0,label_transparency),
                        )
                        

# Create separator on select tab                        
def create_shelf_separator():
    cmds.setParent(shelf_tab_name)
    cmds.separator(width=12, height=35, style='shelf', hr=0)
                          

create_shelf_separator()
                          
# Import the temp_mesh                          
create_shelf_button(
                command = 'cmds.file(path, i=True)',
                annotation = 'import the temp_mesh',
                name = 'import',
                label_name = 'imp',
                )
                  
# Export select mesh to temp folder                          
create_shelf_button(
                command = 'cmds.file(path, force = True, exportSelected=True, type="OBJexport")',
                annotation = 'export select mesh to temp folder',
                name = 'export',
                label_name = 'exp',                
                )
                
create_shelf_separator()

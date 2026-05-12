import os


def create_symlinks(scenes_folder):
    if not os.path.exists(scenes_folder):
        raise FileNotFoundError(f"scenes_folder {scenes_folder} not found!")

    models_dir = os.path.abspath(os.path.join(scenes_folder, 'models'))
    scenes_dir = os.path.abspath(os.path.join(scenes_folder, 'scenes'))
    materials_dir = os.path.abspath(os.path.join(scenes_folder, 'Materials'))
	
    def add_link_according_to_different_cases(link_type:str, link_path, dir_relpath):
        if not os.path.islink(link_path):
            if os.path.isfile(link_path):  # in case of when “Materials" or "model" is a file
                os.remove(link_path)
                os.symlink(dir_relpath, link_path)
            elif os.path.isdir(link_path): # in case of "Materials" or "model" is the true Material/model folder
                pass
            else:  # in case of some files are missing "Materials"/"model" file, or other irrelevant folder . You need to check manually according to the log. 
                print(f"No **{link_type}** file or link in {root}, please check manually")

    
    # create "Materials" symlink in models_dir
    for root, _, files in os.walk(models_dir):
        for _ in files:
            materials_link_path = os.path.join(root, "Materials")
            materials_dir_relpath = os.path.relpath(materials_dir, root)
            add_link_according_to_different_cases(link_type="Materials", link_path=materials_link_path, dir_relpath=materials_dir_relpath)


    # create "Materials" and "models" symlink in scenes_dir
    for root, _, files in os.walk(scenes_dir):
        for _ in files:
            materials_link_path = os.path.join(root, "Materials")
            materials_dir_relpath = os.path.relpath(materials_dir, root)
            add_link_according_to_different_cases(link_type="Materials", link_path=materials_link_path, dir_relpath=materials_dir_relpath)

            models_link_path = os.path.join(root, "models")
            models_dir_relpath = os.path.relpath(models_dir, root)
            add_link_according_to_different_cases(link_type="models", link_path=models_link_path, dir_relpath=models_dir_relpath)



if __name__ == '__main__':
    SCENES_FOLDER = '/home/zwc/lhd_Navigation/assets/scenes/GRScenes-100/home_scenes'
    create_symlinks(SCENES_FOLDER)

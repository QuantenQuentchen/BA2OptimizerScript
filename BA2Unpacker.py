import os
import subprocess as sbp
import yaml

with open(r'Q:\New folder\config.yaml', 'r') as file:
    try:
        config = yaml.load(file, Loader=yaml.CLoader)
    except yaml.YAMLError as exc:
        
        print(f"There's been an Error during Yaml loading... \n To be more precise this:\n{exc}")

print(config)

MODS_DIR = fr"{config['StagingDirectory']}"
BSAB_DIR = os.path.join(fr"{config['BSABrowserDirectory']}", "bsab.exe")

FileAndSizeMap = config["FilesandSizes"]

def main():
    for root, dirs, files in os.walk(MODS_DIR):
        for file in files:
            for name, size in FileAndSizeMap.items():
                if file.endswith(name) and not file.startswith(f"Fallout4 {name}") and os.path.getsize(os.path.join(root, file)) < size*1000000:
                    stdout = sbp.run([BSAB_DIR, "-e", os.path.join(root,file), os.path.join(root,"")])

                    print(stdout)
                    new_file = file.replace(name, f"{name}.bak")
                    if not os.path.isfile(os.path.join(root, new_file)):
                        os.rename(os.path.join(root, file), os.path.join(root, new_file))
                    
main()
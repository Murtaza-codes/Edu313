import os
import polib

def compile_po_files():
    """Manually compile .po files to .mo files using polib."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base_dir, 'locale')
    
    # Walk through all directories in locale directory
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po'):
                po_file_path = os.path.join(root, file)
                mo_file_path = os.path.join(root, file.replace('.po', '.mo'))
                
                try:
                    print(f"Compiling {po_file_path} to {mo_file_path}")
                    po = polib.pofile(po_file_path)
                    po.save_as_mofile(mo_file_path)
                    print(f"Successfully compiled {mo_file_path}")
                except Exception as e:
                    print(f"Error compiling {po_file_path}: {e}")

if __name__ == "__main__":
    compile_po_files()
    print("Message compilation complete!") 
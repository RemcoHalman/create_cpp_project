import os
import argparse
import sys  # Needed for sys.exit()

def create_folder_structure(project_name, setup_type='full'):
    """
    Creates a directory structure for a new C++ project with the specified project name.
    
    :param project_name: Name of the project for which to create the structure.
    :param setup_type: Type of setup ('full' or 'simple')
    """

    project_path = os.path.abspath(project_name)

    # Check if the directory already exists
    if os.path.exists(project_path):
        print(f"Error: Folder already exists at {project_path}")
        sys.exit(1)  # Exit with an error code

    # Define the directories for both setup types
    base_directories = [
        f"{project_name}/src",
        f"{project_name}/include",
        f"{project_name}/scripts"
    ]
    
    full_directories = [
        f"{project_name}/lib",
        f"{project_name}/bin",
        f"{project_name}/obj",
        f"{project_name}/test",
        f"{project_name}/docs"
    ]

    # Create base directories
    directories = base_directories + full_directories if setup_type == 'full' else base_directories

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        if directory in [f"{project_name}/lib", f"{project_name}/bin", f"{project_name}/obj"]:
            with open(os.path.join(directory, "README.md"), "w") as f:
                f.write(f"This directory stores {directory.split('/')[-1]}.")

        # Create initial README.md for the project
    with open(f"{project_name}/README.md", "w") as f:
        f.write(f"# {project_name}\n\nThis is the base directory for the {project_name} project. \nSetup type: {setup_type}")

    # Create other specific files (Makefile, main.cpp, etc.)
    with open(f"{project_name}/src/main.cpp", "w") as f:
        f.write("#include <iostream>\n\nusing namespace std;\n\nint main() {\n    std::cout << \"Hello, world!\" << std::endl;\n    return 0;\n}")
    
    with open(f"{project_name}/Makefile", "w") as f:
        f.write(f"all:\n\tg++ -o {project_name}/bin/{project_name} {project_name}/src/*.cpp")

    with open(f"{project_name}/scripts/build.sh", "w") as f:
        f.write("#!/bin/sh\nmake\n")
        os.chmod(f"{project_name}/scripts/build.sh", 0o755)  # Make the script executable

    with open(f"{project_name}/scripts/clean.sh", "w") as f:
        f.write("#!/bin/sh\nrm -rf bin/* obj/*\n")
        os.chmod(f"{project_name}/scripts/clean.sh", 0o755)  # Make the script executable

def main():
    """
    Main function to handle command line arguments and create the project structure.
    """
    parser = argparse.ArgumentParser(description="Create C++ project structure.")
    parser.add_argument("project_name", type=str, help="Name of the project")
    parser.add_argument("--setup_type", type=str, choices=['full', 'simple'], default='full', help="Type of project setup (full or simple)")

    args = parser.parse_args()
    
    create_folder_structure(args.project_name, args.setup_type)
    print(f"Project '{args.project_name}' with setup type '{args.setup_type}' created successfully.")

if __name__ == "__main__":
    main()


# import os
# import sys

# def create_folder_structure(project_name):
#     """
#     Creates a directory structure for a new C++ project with the specified project name.
    
#     :param project_name: Name of the project for which to create the structure.
#     """


#     directories = [
#         f"{project_name}/src",
#         f"{project_name}/include",
#         f"{project_name}/lib",
#         f"{project_name}/bin",
#         f"{project_name}/obj",
#         f"{project_name}/test",
#         f"{project_name}/docs",
#         f"{project_name}/scripts"
#     ]
    
#     for directory in directories:
#         os.makedirs(directory, exist_ok=True)
#         if directory in [f"{project_name}/lib", f"{project_name}/bin", f"{project_name}/obj"]:
#             with open(os.path.join(directory, "README.md"), "w") as f:
#                 f.write(f"This directory stores {directory.split('/')[-1]}.")
#         if directory in [f"{project_name}/src"]:
#             with open(os.path.join(directory, "main.cpp"), "w") as f:
#                 f.write("""
# #include <iostream>

# using namespace std;

# int main(){
#     cout << "Default template" << endl;
#     return 0;
# }        
#                 """)        
#     with open(f"{project_name}/README.md", "w") as f:
#         f.write(f"# {project_name}\n\nThis is the base directory for the {project_name} project.")

# def main():
#     """
#     Main function to handle command line arguments and create the project structure.
#     """
#     if len(sys.argv) < 2:
#         print("Usage: create_cpp_project <project_name>")
#         sys.exit(1)
    
#     project_name = sys.argv[1]
#     # project_style = sys.argv[2]
#     create_folder_structure(project_name)
#     print(f"Project '{project_name}' created successfully.")

# if __name__ == "__main__":
#     main()

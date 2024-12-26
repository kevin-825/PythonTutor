
# Step 1: Navigate to your project directory
$my_project_path=$(pwd)

echo my_project_path:$my_project_path.path

cd $my_project_path.path

# Step 2: Create a virtual environment
python3 -m venv .myenv

# Step 3: Activate the virtual environment
#source .myenv/bin/activate  # macOS/Linux
.myenv\Scripts\activate     # Windows

# Step 4: Install necessary packages
#pip install requests
pip install requests
pip install pyttsx3
# Step 5: Your project's code can now use the installed packages
#python my_script.py

# Step 6: Deactivate the virtual environment when done
#deactivate

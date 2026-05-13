Execution output in the VS Code terminal. The output verifies that the virus_script.py has successfully identified web02_backup.py as a target and performed the injection process ('Infected: web02_backup.py')."
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/46453542-d086-4341-99fa-9c6d74c1d483" />
Implementation of the malware trigger mechanism within the web application. The subprocess.Popen command is integrated into the search() route in web02.py, allowing the execution of the self-replicating script when the search function is triggered by a user.
<img width="975" height="564" alt="image" src="https://github.com/user-attachments/assets/255c6059-4c3a-4074-a801-0a84d1d1606b" />

Image Description: "Verification of the successful malware replication. The infected file web02_backup.py now includes the # VIRUS SAYS HI! signature at the very first line of the code, confirming that the self-replicating logic successfully modified the target file."
<img width="975" height="530" alt="image" src="https://github.com/user-attachments/assets/9d24096c-64c3-4a81-878c-e7443518f406" />

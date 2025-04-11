# Email-Manager
A Python script that helps with managing your Gmail!

Are you tired of the endless scrolling of emails from the same 30 companies?  
Fear not, this script will help you with that!

### Requirements:
- Your Gmail account must have 2FA (Two-Factor Authentication) enabled.
- Python 3.x installed
- Necessary Python packages (`imaplib`, `pandas`, `yaml`, `json`)

### Setup Instructions:

1. **Generate an App Password for Gmail**:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords) and add a new password for applications. This is needed for the script to work.
   
   ![image](https://github.com/user-attachments/assets/79e7daba-f2f9-4a10-91fd-262b6e23c27a)

2. **Save the App Password and Email in `credentials.yaml`**:
   - After generating the app password, you will receive a 4-word password that you need to input in the `credentials.yaml` file along with your email address.
   
   ![image](https://github.com/user-attachments/assets/41173fda-b867-4c16-870d-cbc0b4c0614b)

3. **Update the List of Emails**:
   - Modify the list of emails that you want to delete or leave marked as "seen" in the appropriate section of the script. This list will be stored in a JSON file.
   
   ![image](https://github.com/user-attachments/assets/8b490d07-74a5-46f0-808a-3f547598ef2b)

4. **(Optional) Change the Path in `main.py`**:
   - Modify the path in the `main.py` file to match the location of your `credentials.yaml` file and the JSON file containing the list of emails to be deleted or marked.

### Usage:

Run the script by executing `main.py`:

```bash
python3 main.py

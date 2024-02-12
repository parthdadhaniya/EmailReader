# EmailReader

## Overview

This project allows you to read unread emails from a Gmail account, store them in a database, and search for predefined keywords within the email bodies. It utilizes Django for the web framework and Celery for task management.

## Prerequisites

Before using this application, you need to generate an app-specific password for your Gmail account. Follow these steps:

1. **Sign in to your Google Account**: Go to your [Google Account settings page](https://myaccount.google.com/) and sign in if you aren't already.

2. **Security Settings**: Once you're logged in, navigate to the "Security" section. You can find it on the left-hand side menu.

3. **App Passwords**: Look for the option labeled "App passwords" or something similar. Click on it.

4. **Authenticate**: You may need to re-enter your password to proceed.

5. **Generate App Password**: Find the option to generate a new app password. Select the app and device for which you want to generate the password. If Gmail is not listed, you can choose "Other (Custom name)".

6. **Generate**: Click on the "Generate" button. Google will create a unique app password for the selected app and device.

7. **Copy the Password**: Once the password is generated, you'll see it displayed on the screen. Copy this password as you'll need it to configure your app.

8. **Configure Your App**: Open the app (in this case, the Gmail app), and when prompted for your password, use the app password you just generated instead of your regular Google Account password.

9. **Save the Password**: Some apps may provide an option to save the app password. Make sure to do this if you don't want to re-enter the password each time you use the app.

10. **Finish**: Once you've entered the app password and configured your app, you should be all set. Your Gmail account will now be accessible through the app using the app-specific password.

## Features

- **Read Unread Emails**: Automatically fetches unread emails from a Gmail account.
- **Store Emails in Database**: Stores the fetched emails in a database for future reference.
- **Keyword Search**: Searches for predefined keywords within the email bodies.
- **Django Web Interface**: Provides a web interface built with Django for managing the email processing tasks.
- **Celery Task Management**: Utilizes Celery for handling asynchronous tasks such as fetching emails and keyword searches.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/parthdadhaniya/EmailReader.git
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django and Celery Settings**:

   - Update `settings.py` with your email configuration details.
   - Update `settings.py` with your celery configuration details.

4. **Make Migrations**:

   ```bash
   python manage.py makemigrations
   ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Start Celery Worker**:

   ```bash
   celery -A your_project worker --loglevel=info
   ```

7. **Start Django Development Server**:
   ```bash
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)

## Authors

- [Parth Dadhaniya](https://github.com/parthdadhaniya)

## Contact

For any inquiries or feedback, feel free to contact [parthdadhaniya079@gmail.com](mailto:parthdadhaniya079@gmail.com).

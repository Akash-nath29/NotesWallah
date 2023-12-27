# NotesWallah - Class Notes and Study Music Sharing Platform 📚🎶

[![GitHub stars](https://img.shields.io/github/stars/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/network)
[![GitHub issues](https://img.shields.io/github/issues/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/pulls)
[![GitHub license](https://img.shields.io/github/license/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/Akash-nath29/NotesWallah.svg?style=flat-square)](https://github.com/Akash-nath29/NotesWallah/graphs/contributors)

NotesWallah is a feature-rich Flask-based platform designed for sharing class notes and study music. It provides a seamless and secure environment for students to collaborate, learn, and enjoy music tailored to their study sessions.

![notesWallahHomePage](https://github.com/Akash-nath29/NotesWallah/assets/100131577/64af0b32-69c1-4f1f-a779-b6a17431e750)


## Key Features 🚀

- **User Authentication System:** A robust user authentication system ensures secure access to the platform. Users can create accounts, log in, and manage their profiles effectively.

- **File Preview and Download System:** Users can preview files directly on the platform before deciding to download them. This feature enhances the user experience by providing a quick overview of the content.

- **Embedded YouTube Videos in Music Section:** The music section allows users to share study playlists by embedding YouTube videos. This feature adds a dynamic and engaging element to the platform.

- **User Profile Control:** Users have control over their profiles, including the ability to update personal information such as name and email, upload a profile picture, and change their passwords.

- **Highest User Data Security:** The platform prioritizes user data security by implementing password hashing. This ensures that user passwords are securely stored.

- **Scalability:** NotesWallah is designed with scalability in mind, allowing it to accommodate a growing user base and expanding content seamlessly.

## Getting Started 🛠️

To run the NotesWallah platform locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Akash-nath29/NotesWallah.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database settings
    Open command prompt, and follow the following commands
    ```bash
    flask shell
    ```
    ```bash
    from app import db
    ```
    ```bash
    db.create_all()
    ```
    ```bash
    exit()
    ```

4. Run the application:

   ```bash
   python app.py
   ```

   The platform will be accessible at [http://127.0.0.1:6010](http://127.0.0.1:6010).

## Contributing 🤝

Contributions are welcome! To contribute to NotesWallah, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Submit a pull request.

## Community and Support 🌐

- **Report Issues:** If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/Akash-nath29/NotesWallah/issues).

- **Community:** Join the community discussions and get support on [GitHub Discussions](https://github.com/Akash-nath29/NotesWallah/discussions).

## License 📝

NotesWallah is open-source and available under the [MIT License](https://github.com/Akash-nath29/NotesWallah/blob/main/LICENSE).

---

Feel free to explore, contribute, and make NotesWallah your own! Happy learning and studying! 📚🎶


# Music Streaming App

This is a music streaming application built with a Flutter frontend and a FastAPI backend. The app uses PostgreSQL as the database and Cloudinary to store media files (songs and thumbnails). The frontend allows users to select songs, which are fetched from the backend, and then plays them via Cloudinary URLs.

## Project Structure

- **Frontend**: Built with Flutter (Dart) and uses various dependencies like Riverpod, Hive, and Just Audio for state management, local storage, and audio playback.
- **Backend**: Built with FastAPI (Python), connected to a PostgreSQL database. The backend stores URLs of songs and thumbnails stored in Cloudinary.

---

## Prerequisites

- **Flutter** (For frontend)
- **Python** (For backend)
- **PostgreSQL** (Database)
- **Cloudinary Account** (For media storage)
- **Emulator or Device** (For running the app)

---

## Frontend Setup (Flutter)

### Dependencies

Ensure the following dependencies are added to your `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.6
  http: ^1.2.1
  fpdart: ^2.0.0-dev.3
  flutter_riverpod: ^2.5.1
  riverpod_annotation: ^2.3.5
  shared_preferences: ^2.2.3
  dotted_border: ^2.1.0
  flex_color_picker: ^3.5.0
  file_picker: ^8.0.3
  audio_waveforms: ^1.0.5
  just_audio: ^0.9.38
  hive: ^4.0.0-dev.2
  isar_flutter_libs: ^4.0.0-dev.13
  path_provider: ^2.1.0
  just_audio_background: ^0.0.1-beta.12
```

### Installation & Running

1. **Install Dependencies**:
   ```bash
   flutter pub get
   ```

2. **Build and Watch for Code Changes**:
   This command runs the code generator if you’re using Riverpod or Hive for type generation.
   ```bash
   dart run build_runner watch -d
   ```

3. **Run the App**:
   Make sure you have a connected device or emulator.
   ```bash
   flutter run
   ```

### Notes

- The app uses `just_audio` and `just_audio_background` for playing audio in the background.
- Make sure to configure Cloudinary URLs correctly in the backend response so that the frontend can play the songs seamlessly.

---

## Backend Setup (FastAPI + PostgreSQL)

### Dependencies

Create a `requirements.txt` file with the following:

```plaintext
fastapi
uvicorn
sqlalchemy
psycopg2-binary
cloudinary
python-dotenv
```

### Installation & Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Create a `.env` file for database and Cloudinary configuration:
   ```env
   DATABASE_URL=postgresql://<username>:<password>@localhost:<port>/<database>
   CLOUDINARY_CLOUD_NAME=<your_cloud_name>
   CLOUDINARY_API_KEY=<your_api_key>
   CLOUDINARY_API_SECRET=<your_api_secret>
   ```


---

## Database (PostgreSQL)

1. Create a PostgreSQL database for the app.
2. Set up tables for storing song metadata and URLs (if using SQLAlchemy, create models accordingly).
3. Ensure the database URL is correctly set in the `.env` file in the backend.

---

## Cloudinary Setup

1. Sign up for a Cloudinary account.
2. Configure Cloudinary in the backend using environment variables.
3. Store songs and thumbnails on Cloudinary. The URLs should be saved in PostgreSQL, which will be retrieved by the frontend.

---

## Usage

1. **Start the Backend**:
   ```bash
   fastapi dev main.py
   ```

2. **Start the Frontend**:
   ```bash
   dart run build_runner watch -d
   flutter run
   ```

3. Connect to an emulator or device, and the app should be ready for use.

---

## Troubleshooting

- Ensure your PostgreSQL and Cloudinary credentials are correctly set.
- Verify Cloudinary URLs are accessible and valid.
- Confirm that the `build_runner` is active and dependencies are up-to-date in Flutter.

---

## Future Improvements

- Add more audio features (e.g., playlists, favorites).
- Improve caching and offline capabilities using Hive.
- Implement user authentication and user-specific libraries.

---

## License

This project is open-source and available under the MIT License.

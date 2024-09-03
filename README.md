# Django Music App

A simple Django application for managing and displaying a collection of music albums. This app allows users to browse a list of albums, view details of individual albums, and see the songs associated with each album.

## Features

- **Album List**: Display a list of music albums with cover images, titles, artists, genres, and release dates.
- **Album Detail**: View detailed information about an album, including a larger cover image, description, and a list of songs.
- **Filter Functionality**: Filter albums by genre, artist, or title to easily find specific albums.
- **Data Initialization**: Includes sample data for albums and songs to get started quickly.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone hhttps://github.com/suchockipawel/musicproject.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd musicproject
   ```

3. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Load Initial Data**:
   ```bash
   python manage.py loaddata music/fixtures/initial_data.json
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the App**:
   Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Directory Structure

- `music/`: The Django app directory containing models, views, and templates for managing music data.
- `media/`: Directory where album cover images are stored.
- `templates/`: HTML templates for rendering album lists and details.

## Usage

- **View Albums**: Access the list of albums at the homepage.
- **View Album Details**: Click on an album to view more information and its songs.

## Contributing

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/yourusername/musicapp).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

---

Feel free to adjust the `git clone` URL, repository name, and other specific details according to your actual project setup.

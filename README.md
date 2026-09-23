# File-Organizer-In-Python
A smart Python script that automatically organizes messy folders by file types. It creates separate folders for Images, Documents, Videos etc. and moves files automatically.

# 📁 File Organizer in Python

A simple and powerful Python automation script to organize your messy folders. Just run the script and it will automatically create separate folders based on file extensions and move files into them.

No more cluttered Downloads or Desktop folders!

### ✨ Features
- Automatically detects file types (Images, Docs, Videos, etc.)
- Creates folders like `Images`, `Documents`, `Videos`, `Music`, `Archives` etc.
- Moves files safely using `shutil`
- Handles duplicate file names
- Works on any folder - just give the path

### 📂 How it Works
Example:
Before:
/MyFolder
- vacation.jpg
- report.pdf
- song.mp3
- notes.txt
- movie.mp4

After Running Script:
/MyFolder
/Images
- vacation.jpg
/Documents
- report.pdf
- notes.txt
/Music
- song.mp3
/Videos
- movie.mp4

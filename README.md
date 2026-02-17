# Notes App - Django

A feature-rich notes management application built with Django that allows users to create, edit, and manage notes with a robust recycle bin system.

## Key Features

- 📝 **Create & Edit Notes** - Write and modify notes with ease
- 🗑️ **Recycle Bin** - Deleted notes are moved to recycle bin instead of permanent deletion
- ♻️ **Restore Functionality** - Retrieve notes from recycle bin anytime
- ⏰ **Auto-Deletion** - Notes in recycle bin are automatically deleted after 15 days
- 🔍 **View Notes** - Clean and intuitive interface for reading notes

## Tech Stack

- Django
- Python
- HTML/CSS
- Bootstrap (if used)
- SQLite/PostgreSQL

## How It Works

When a user deletes a note, it's not permanently removed. Instead, it's moved to the recycle bin where users can:
- Restore notes back to active status
- Permanently delete notes immediately
- Wait for automatic deletion after 15 days

This safety net ensures no important notes are accidentally lost forever.

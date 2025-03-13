import sqlite3

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               content TEXT NOT NULL
    )
''')
conn.commit()

# Function to add a new note
def add_note(title, content):
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("✅ Note added successfully!")

# Function to view all notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    if not notes:
        print("📜 No notes found.")
    else:
        for note in notes:
            print(f"\n📝 ID: {note[0]}\n📌 Title: {note[1]}\n📖 Content: {note[2]}\n")

# Function to update a note
def update_note(note_id, new_title, new_content):
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
    conn.commit()
    print("✏️ Note updated successfully!")

# Function to delete a note
def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("🗑️ Note deleted successfully!")

# CLI Menu
def menu():
    while True:
        print("\n📒 Notes Manager CLI")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Update Note")
        print("4️⃣ Delete Note")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            add_note(title, content)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            note_id = int(input("Enter note ID to update: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            update_note(note_id, new_title, new_content)
        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(note_id)
        elif choice == "5":
            print("👋 Exiting Notes Manager.")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

# Run the CLI
if __name__ == "__main__":
    menu()

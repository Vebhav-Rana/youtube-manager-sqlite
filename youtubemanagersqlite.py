import sqlite3

DB_NAME = "youtubesqlite.db"

conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()

# create table
curr.execute("""
CREATE TABLE IF NOT EXISTS youtubevideos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration TEXT NOT NULL
)
""")
conn.commit()


def add_video():
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    curr.execute(
        "INSERT INTO youtubevideos (name, duration) VALUES (?, ?)",
        (name, duration)
    )
    conn.commit()
    print("Video added successfully.")


def list_all_videos():
    curr.execute("SELECT * FROM youtubevideos")
    rows = curr.fetchall()

    if not rows:
        print("No videos available.")
        return []

    videos = []
    for row in rows:
        video_str = f"{row[0]}. {row[1]} -> {row[2]}"
        videos.append(video_str)

    return videos


def delete_video():
    videos = list_all_videos()
    if not videos:
        return

    for item in videos:
        print(item)

    try:
        video_id = int(input("Enter the ID of the video to delete: "))
        curr.execute("DELETE FROM youtubevideos WHERE id = ?", (video_id,))
        conn.commit()
        print("Video deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")


def update_video():
    videos = list_all_videos()
    if not videos:
        return

    for item in videos:
        print(item)

    try:
        video_id = int(input("Enter the ID of the video to update: "))
        new_name = input("Enter new video name: ")
        new_duration = input("Enter new video duration: ")

        curr.execute(
            "UPDATE youtubevideos SET name = ?, duration = ? WHERE id = ?",
            (new_name, new_duration, video_id)
        )
        conn.commit()
        print("Video updated successfully.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nChoose an option:")
        print("1. Add a video")
        print("2. Delete a video")
        print("3. Update a video")
        print("4. List all videos")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                add_video()
            case 2:
                delete_video()
            case 3:
                update_video()
            case 4:
                videos = list_all_videos()
                for v in videos:
                    print(v)
            case 5:
                print("Exiting program...")
                break
            case _:
                print("Invalid choice.")

    conn.close()


if __name__ == "__main__":
    main()

# === Git Auto Update Script ===
cd "C:\Users\nafiz\Desktop\CP"

# Stage all changes
git add .

# Create a commit message with date and time
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto update on $timestamp"

# Push to GitHub
git push

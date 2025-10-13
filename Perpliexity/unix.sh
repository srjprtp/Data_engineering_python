#renaming files with current date
for f in *.ipynb; do
    mv "$f" "$(date -r "$f" +"%d%b%Y")_$f"
done

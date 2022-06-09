while read p; do
  echo "$p"
  ls "$p/Accepted" |wc -l
done <all_files

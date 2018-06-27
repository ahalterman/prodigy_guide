prodigy db-out <name-of-dataset> .

curl -X POST https://content.dropboxapi.com/2/files/upload \
    --header "Authorization: Bearer <OATH TOKEN HERE>" \
    --header "Dropbox-API-Arg: {\"path\": \"/<DROPBOX FOLDER NAME>/<NAME OF EXPORTED DATASET.jsonl>\"}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @<NAME OF EXPORTED DATASET.jsonl

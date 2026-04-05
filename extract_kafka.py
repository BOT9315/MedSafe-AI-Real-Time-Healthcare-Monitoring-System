import tarfile
# Replace this path with your uploaded file
tgz_file = r"C:\kafka_2.13-4.2.0\kafka_2.13-4.2.0\site-docs\kafka_2.13-4.2.0-site-docs.tgz"
extract_path = r"C:\kafka_extracted"

with tarfile.open(tgz_file, "r:gz") as tar:
    tar.extractall(path=extract_path)

print("Extraction complete")

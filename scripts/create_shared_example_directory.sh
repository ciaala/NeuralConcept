#!/bin/sh
ROOT=${SHARED_PATH:-./shared}
mkdir -p ${ROOT}
echo "Creating example files in the folder ${ROOT}"
./scripts/create_file.sh ${ROOT}/image_512.png 512
./scripts/create_file.sh ${ROOT}/image_1024.png 1024
./scripts/create_file.sh ${ROOT}/image_2048.png 2048
./scripts/create_file.sh ${ROOT}/text_512.txt 512
./scripts/create_file.sh ${ROOT}/text_1024.txt 1024
./scripts/create_file.sh ${ROOT}/text_2048.txt 2048
./scripts/create_file.sh ${ROOT}/video_512.mkv 512
./scripts/create_file.sh ${ROOT}/video_1024.mkv 1024
./scripts/create_file.sh ${ROOT}/video_2048.mkv 2048
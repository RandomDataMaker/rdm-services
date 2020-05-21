
#! /bin/sh 
echo "Waiting 15s for DB" 
sleep 15 
echo "Done waiting for DB" 

python3 manage.py makemigrations 
python3 manage.py migrate 

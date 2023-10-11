call conda activate
echo conda activated!

call pip3 install -r requirements.txt

call python -m uvicorn main:app --reload --workers 1 --host 10.185.78.54 --port 8008

call conda deactivate
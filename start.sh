echo "Cloning Repo...."
git clone https://github.com/LPSMOVIES/chklinks /chklinks
cd /chklinks
pip3 install -r requirements.txt
echo "Starting Bot....GreyMatter_Bots"
python3 main.py

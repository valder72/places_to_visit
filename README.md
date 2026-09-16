Installation and Setup

1. Clone the repository
git clone [https://github.com/valder72/places_to_visit.git](https://github.com/valder72/places_to_visit.git)
cd places_to_visit
2. Create and activate a virtual environment
Windows (cmd / PowerShell):
python -m venv venv
venv\Scripts\Activate.ps1

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the development server
python manage.py runserver

Author:
Student: Volodymyr Pohribnyi
Creation date: September 15, 2026
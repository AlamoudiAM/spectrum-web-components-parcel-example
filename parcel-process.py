from subprocess import run
from pathlib import Path
from http import server

# project path
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# find html files to be processed with parcel
find = run("find {} -name *.html ! -path '*/node_modules/*' ! -path '*/dist/*'".format(BASE_DIR),
              shell=True,
              capture_output=True)
find_err = find.stderr.decode('utf-8')
find_out = find.stdout.decode('utf-8').split('\n')

# clean dist
run(['rm', '-rf', '{}/dist/'.format(BASE_DIR)])

# run html files in parcel
parcel = run(['yarn', 'parcel', 'build'] + find_out,
              capture_output=True)
parcel_err = parcel.stderr.decode('utf-8')
parcel_out = parcel.stdout.decode('utf-8')
print(parcel_err)
print(parcel_out)

run(['python3', '-m', 'http.server', '8000', '--directory', '{}/dist/'.format(BASE_DIR)])

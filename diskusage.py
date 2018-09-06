#exec(open('/Users/admin/diskusage.py').read())
import os
import sys
import pprint

def get_disk_usage(mp, FILES=[]):
	items = [ f for f in os.listdir(mp) if not f.startswith('.')]
	files = [f for f in items if os.path.isfile(os.path.join(mp, f))]
	folders = list(set(items)-set(files))

	for file in files:
		full_path = os.path.join(mp, file)
		FILES.append([full_path, os.path.getsize(full_path)])

	for folder in folders:
		full_path = os.path.join(mp, folder)
		return get_disk_usage(full_path, FILES)

	return FILES


def help():
	print('USAGE: python diskusage.py <mountpoint>')

try:
	mountp = sys.argv[1] # checking sufficient params are given or not
except:
	print('Argument missing. Aborting:')
	help()
	exit(0)

fs = get_disk_usage(mountp)
pprint.pprint(fs)

import pkg_resources
import subprocess
import sys
from packaging import version

def get_latest_version(name):
    latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(name)], capture_output=True, text=True))
    latest_version = latest_version[latest_version.find('(from versions:')+15:]
    latest_version = latest_version[:latest_version.find(')')]
    latest_version = latest_version.replace(' ','').split(',')[-1]

    return latest_version
package_name = "plot4d"

try:
    installed_version = pkg_resources.get_distribution(package_name).version
    latest_version = get_latest_version(package_name)
    
    installed_version = version.parse(installed_version)
    latest_version = version.parse(latest_version)
    if installed_version < latest_version:
        print(f"There's a new version of {package_name} available ({latest_version}), you're running {installed_version}. To upgrade: pip install {package_name} --upgrade")
except pkg_resources.DistributionNotFound:
    print(f"{package_name} is not installed.")

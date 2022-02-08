# Uninstall Microsoft Edge In Windows 10 And Windows 11

# Imports
import subprocess
import os
import sys

# Change Directory To Microsoft Edge
os.chdir("C:\\Program Files (x86)\\Microsoft\\Edge\\Application")
EDGE_VERSIONS = os.listdir()
try:
    EDGE_VERSIONS.remove("msedge.exe")
    EDGE_VERSIONS.remove("pwahelper.exe")
    EDGE_VERSIONS.remove("msedge_proxy.exe")
    EDGE_VERSIONS.remove("SetupMetrics")
    EDGE_VERSIONS.remove("delegatedWebFeatures.sccd")
    EDGE_VERSIONS.remove("msedge.VisualElementsManifest.xml")
except:
    EDGE_VERSIONS.remove("msedge.exe")
    EDGE_VERSIONS.remove("pwahelper.exe")
    EDGE_VERSIONS.remove("msedge_proxy.exe")
    EDGE_VERSIONS.remove("SetupMetrics")
    EDGE_VERSIONS.remove("msedge.VisualElementsManifest.xml")

# Ask The User What Version To Uninstall
versionnumbers = -1
for version in EDGE_VERSIONS:
    versionnumbers += 1
    print(f"[{versionnumbers}]" + version)

versionnumbers += 1
last_versionnumber = versionnumbers
print(f"\n[{versionnumbers}] Uninstall All Versions")

try:
    uninstall = int(input("Enter The Version Number To Uninstall Microsoft Edge: "))
except:
    print("Input Must Be A Number.")
    sys.exit(1)

# If uninstall is not equal to the last version number, then uninstall the version

if uninstall != last_versionnumber:
    # Check If The Version Exists
    if uninstall > versionnumbers:
        print("Version Does Not Exist.")
        sys.exit(1)

    # Check If The Number Is A Nagative Number
    elif uninstall < 0:
        print("Number Must Be Positive.")
        sys.exit(1)

    else:
        pass
    try:
        print("\nUninstalling...")
        try:
            os.chdir(
                f"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\{EDGE_VERSIONS[uninstall]}\\Installer")
        except:
            print("ERROR: directory not found.")
            sys.exit(1)

        try:
            subprocess.call("cmd /c taskkill /im msedge.exe /f 2> NUL")
        except:
            pass
        subprocess.call(
            "setup.exe --uninstall --force-uninstall --system-level")
    except:
        print("ERROR: setup.exe not found.")

# Else If uninstall is equal to the last version number, then uninstall all versions

elif uninstall == last_versionnumber:
    for version in EDGE_VERSIONS:
        try:
            os.chdir(
                f"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\{version}\\Installer")
        except:
            print(f"ERROR: directory for version {version} not found.")
        subprocess.call("cmd /c taskkill /im msedge.exe /f 2> NUL")
        try:
            subprocess.call(
                "setup.exe --uninstall --force-uninstall --system-level")
        except:
            print(f"ERROR: setup.exe not found for version {version}.")

os.system("pause")

# End Of Script

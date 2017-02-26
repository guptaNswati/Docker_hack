#!/usr/bin/python3
from subprocess import check_output, CalledProcessError
import re

def meaningful_info (install_dict):
    packages = install_dict.keys()
    packages_by_size = dict()
    for package in packages:
        try:
            package_size = check_output("apt-cache --no-all-versions show " + package + " | grep \'^Size: \'", shell=True)
            package_size = package_size.split()
            package_size = package_size[1].decode("utf-8")
            packages_by_size[package] = package_size
        except CalledProcessError as e:
            packages_by_size[package] = "E: no package found"
            continue;
        except Exception as e:
            print("this is exception", e)
    total_bytes = 0
    for package in packages:
        try:
            bytes_saved = int(packages_by_size[package]) * (install_dict[package] - 1)
            total_bytes += bytes_saved
            print("for package {}, potential bytes saved {:d}".format(package, bytes_saved))
        except Exception as e:
#            print("this is the package", package, "this is exception", e)
            continue;

    print("possible total bytes save {:d} if docker image relayered".format(total_bytes))

#meaningful_info({"perl":2, "ruby": 3, "\tapt-utils": 2})

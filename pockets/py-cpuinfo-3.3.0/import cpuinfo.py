import cpuinfo

#print(cpuinfo.get_cpu_info())

import subprocess
subprocess.Popen('wmic cpu get L3CacheSize')

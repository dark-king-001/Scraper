import subprocess
pool = []
def Worker(command):
    f = open("WorkerLog/Output_log.txt",'ab')
    open("WorkerLog/Command_log.txt",'a').write(command+"\n")
    p = subprocess.Popen([command],stdout=f,shell=True)
    pool.append((p, f))
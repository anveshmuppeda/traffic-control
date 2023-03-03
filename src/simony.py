from sumolib import checkBinary
import traci
import plot_metrics
import array

tswitch = 12
ttrains = 4
occ = 70.0
thlow = 30.0
sides = 15
lanes = [3, 2, 3, 2, 3, 2, 3 ]
IDStl = ["gneJ20", "gneJ18", "151147259", "gneJ69"]

sumoBinary = checkBinary('sumo-gui')
first_act_of_run = 0
skip_time = 0
t = 0

statecurrent = array.array('f', [0] * sides)
stateprevios = array.array('f', [0] * sides)

def newrun(run):
    global statecurrent, stateprevios, intn_prev_action, first_act_of_run, skip_time, qlenfile
    statecurrent = array.array('f', [0] * sides)
    stateprevios = array.array('f', [0] * sides)
    intn_prev_action = [1, 5, 9, 13]
    first_act_of_run = 0
    skip_time = 0

    if run == 0:
        plot_metrics.init(ttrains + tswitch)

    if platform.system() == 'Linux':
        os.system("python \"$SUMO_HOME/tools/randomTrips.py\" -n ../scripts/txmap.net.xml --trip-attributes=\"type=\\\"light_norm_heavy\\\"\" "
            "-a ../scripts/txmap.add.xml -r ../scripts/txmap.rou.xml -e 12000 -p 0.75 --binomial=5 -L")
        os.system("rm \"../scripts/txmap.rou.alt.xml\"")
        os.system("rm trips.trips.xml")

    traci.start([sumoBinary, "-c", "../scripts/txmap.sumocfg", "--gui-settings-file", "../scripts/guisettings.xml",
                 "--start", "--quit-on-end", "--no-warnings"])
    qlenfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n\n")
    qlenfile.write("<qlengths>" + '\n')
    qlenfile.flush()
    return
  
def currentstate():
    state = array.array('f', [0] * sides)
    for i in range(sides):
        n = 0.0
        for j in range(lanes[i]):
            n = max(n, traci.lanearea.getLastStepOccupancy("e2det_N"+str(i+1)+"_"+str(j)))
        state[i] = n
    return state

def guimode(mode):
    global sumoBinary
    if mode == 1:
        sumoBinary = checkBinary('sumo-gui')
    else:
        sumoBinary = checkBinary('sumo')
    return

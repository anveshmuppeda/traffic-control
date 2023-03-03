from sumolib import checkBinary
import traci
import plot_metrics
import array

T_SWITCH = 12
T_TRANS = 4
OCC_TH_HIGH = 70.0
OCC_TH_LOW = 30.0
NUM_INTN_SIDES = 15
NUM_LANES = [3, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 1, 2, 1, 2]

TL_IDS = ["gneJ20", "gneJ18", "151147259", "gneJ69"]        # Intersection traffic light IDs

# Intersection phases
TL_PHASES = {'N1_G': 0, 'N1_Y': 1, 'N2_G': 2, 'N2_Y': 3, 'N3_G': 4, 'N3_Y': 5, 'N4_G': 6, 'N4_Y': 7,
             'N5_G': 0, 'N5_Y': 1, 'N6_G': 2, 'N6_Y': 3, 'N7_G': 4, 'N7_Y': 5, 'N8_G': 6, 'N8_Y': 7,
             'N9_G': 0, 'N9_Y': 1, 'N10_G': 2, 'N10_Y': 3, 'N11_G': 4, 'N11_Y': 5, 'N12_G': 6, 'N12_Y': 7,
             'N13_G': 0, 'N13_Y': 1, 'N14_G': 2, 'N14_Y': 3, 'N15_G': 4, 'N15_Y': 5}


sumoBinary = checkBinary('sumo-gui')
first_act_of_run = 0
skip_time = 0
t = 0

curr_state = array.array('f', [0] * NUM_INTN_SIDES)
prev_state = array.array('f', [0] * NUM_INTN_SIDES)

def start_new_run(run):

    global curr_state, prev_state, intn_prev_action, first_act_of_run, skip_time, qlenfile

    curr_state = array.array('f', [0] * NUM_INTN_SIDES)
    prev_state = array.array('f', [0] * NUM_INTN_SIDES)
    intn_prev_action = [1, 5, 9, 13]
    first_act_of_run = 0
    skip_time = 0

    if run == 0:
        plot_metrics.init(T_TRANS + T_SWITCH)

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
  
def get_current_state():
    state = array.array('f', [0] * NUM_INTN_SIDES)
    for i in range(NUM_INTN_SIDES):
        n = 0.0
        for j in range(NUM_LANES[i]):
            n = max(n, traci.lanearea.getLastStepOccupancy("e2det_N"+str(i+1)+"_"+str(j)))
        state[i] = n
    return state

def endis_sumo_guimode(mode):
    global sumoBinary
    if mode == 1:
        sumoBinary = checkBinary('sumo-gui')
    else:
        sumoBinary = checkBinary('sumo')
    return

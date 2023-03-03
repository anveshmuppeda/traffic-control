import simenv
import numpy as np

def signalling(totalRuns):
    print("Running Static signalling")
    for run in range(totalRuns):
        print("Run " + str(run + 1))
        simenv.start_new_run(run)
        first_state()
        curr_a = 1
        t = 0
        counter = [1, 0, 0, 0]
        while True:
            next_inter = (t + 1) % 4
            if next_inter == 3:
                a_space = [13, 14, 15]
            else:
                a_space = [4 * next_inter + 1, 4 * next_inter + 2, 4 * next_inter + 3,
                           4 * next_inter + 4]
            next_a = a_space[counter[next_inter]]
            if counter[next_inter] != len(a_space) - 1:
                counter[next_inter] += 1
            else:
                counter[next_inter] = 0
            env_param = simenv.take_action(curr_a)
            r = env_param['rwd']
            if r == -100:
                print("Last simulation: " + str(t))
                break
            curr_a = next_a
            t += 1
    return
def first_state():
    for j in range(np.random.choice([4, 8, 12, 16, 20])):
        env_dict = simenv.take_action(0)
    return env_dict['next_state']
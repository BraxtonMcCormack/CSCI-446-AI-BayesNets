import os
import timeit

from bif_parser import parse_bif

def alarm_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the .bif file
    bif_path = os.path.join(current_dir, 'data', 'alarm.bif')

    # Parse the .bif file and create a Bayesian Network
    bayesian_network = parse_bif(bif_path)

    # Print the resulting Bayesian Network
    bayesian_network.print_details()
    # print(bayesian_network)
    # bayesian_network.print_network()

    query_node = 'HYPOVOLEMIA'

    print("\nLittle Evidence: HRBP=HIGH; CO=LOW; BP=HIGH")

    evidence = {
        'HRBP': 'HIGH',
        'CO': 'LOW',
        'BP': 'HIGH'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'LVFAILURE'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'ERRLOWOUTPUT'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'HYPOVOLEMIA'

    print("\nModerate Evidence: HRBP=HIGH; CO=LOW; BP=HIGH; HRSAT=LOW; HREKG=LOW;HISTORY=TRUE")

    evidence = {
        'HRBP': 'HIGH',
        'CO': 'LOW',
        'BP': 'HIGH',
        'HRSAT': 'LOW',
        'HREKG': 'LOW',
        'HISTORY': 'TRUE'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'LVFAILURE'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'ERRLOWOUTPUT'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

def child_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the .bif file
    bif_path = os.path.join(current_dir, 'data', 'child.bif')

    # Parse the .bif file and create a Bayesian Network
    bayesian_network = parse_bif(bif_path)

    # Print the resulting Bayesian Network
    bayesian_network.print_details()
    # print(bayesian_network)
    # bayesian_network.print_network()

    query_node = 'Disease'

    print("\nLittle Evidence: LowerBodyO2=“<5”; RUQO2=“>=12”; CO2Report=“>=7.5”; XrayReport=Asy/Patchy")

    evidence = {
        'LowerBodyO2': '<5',
        # 'RUQO2': '>=12',
        'CO2Report': '>=7.5',
        'XrayReport': 'Asy/Patchy'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    print("\nModerate Evidence: LowerBodyO2=“<5”; RUQO2=“>=12”; CO2Report=“>=7.5”; XrayRe-port=Asy/Patchy; GruntingReport=Yes; LVHReport=Yes; Age=“11-30 Days”")

    evidence = {
        'LowerBodyO2': '<5',
        # 'RUQO2': '>=12',
        'CO2Report': '>=7.5',
        'XrayReport': 'Asy/Patchy',
        'GruntingReport': 'Yes',
        'LVHReport': 'Yes',
        'Age': '11-30 Days'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

def hailfinder_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the .bif file
    bif_path = os.path.join(current_dir, 'data', 'hailfinder.bif')

    # Parse the .bif file and create a Bayesian Network
    bayesian_network = parse_bif(bif_path)

    # Print the resulting Bayesian Network
    bayesian_network.print_details()
    # print(bayesian_network)
    # bayesian_network.print_network()

    query_node = 'SatContMoist'

    print("\nLittle Evidence: RSFcst=XNIL; N32StarFcst=XNIL; MountainFcst=XNIL; AreaMoDryAir=VeryWet")

    evidence = {
        'RSFcst': 'XNIL',
        'N32StarFcst': 'XNIL',
        'MountainFcst': 'XNIL',
        'AreaMoDryAir': 'VeryWet'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'LLIW'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")


    query_node = 'SatContMoist'

    print("\nModerate Evidence: RSFcst=XNIL; N32StarFcst=XNIL; MountainFcst=XNIL; AreaMoD-ryAir=VeryWet; CombVerMo=Down; AreaMeso_ALS=Down; CurPropConv=Strong")

    evidence = {
        'RSFcst': 'XNIL',
        'N32StarFcst': 'XNIL',
        'MountainFcst': 'XNIL',
        'AreaMoDryAir': 'VeryWet',
        'CombVerMo': 'Down',
        'AreaMeso_ALS': 'Down',
        'CurPropConv': 'Strong'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'LLIW'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

def insurance_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the .bif file
    bif_path = os.path.join(current_dir, 'data', 'insurance.bif')

    # Parse the .bif file and create a Bayesian Network
    bayesian_network = parse_bif(bif_path)

    # Print the resulting Bayesian Network
    bayesian_network.print_details()
    # print(bayesian_network)
    # bayesian_network.print_network()

    query_node = 'MedCost'

    print("\nittle Evidence: Age=Adolescent; GoodStudent=False; SeniorTrain=False; DrivQuality=Poor")

    evidence = {
        'Age': 'Adolescent',
        'GoodStudent': 'False',
        'SeniorTrain': 'False',
        'DrivQuality': 'Poor'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'ILiCost'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'PropCost'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'MedCost'

    print("\nModerate Evidence: Age=Adolescent; GoodStudent=False; SeniorTrain=False; DrivQual-ity=Poor; MakeModel=Luxury; CarValue=FiftyThousand; DrivHistory=Zero")

    evidence = {
        'Age': 'Adolescent',
        'GoodStudent': 'False',
        'SeniorTrain': 'False',
        'DrivQuality': 'Poor',
        'MakeModel': 'Luxury',
        # 'CarValue': 'FiftyThousand',
        'DrivHistory': 'Zero'
    }

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print("Here")
    print(result_factor)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'ILiCost'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

    query_node = 'PropCost'

    result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)

    print(f"\nQuery result for the state of {query_node} given the evidence:")
    for state, prob in result_factor.cpt.items():
        print(f"State {state} has a probability of {prob:.4f}")

def win95pts_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the .bif file
    bif_path = os.path.join(current_dir, 'data', 'win95pts.bif')

    # Parse the .bif file and create a Bayesian Network
    bayesian_network = parse_bif(bif_path)

    # Print the resulting Bayesian Network
    bayesian_network.print_details()

    # List of problems to report
    problems_to_report = ['Problem1', 'Problem2', 'Problem3', 'Problem4', 'Problem5', 'Problem6']
    
    # List of evidence pieces, in order
    evidence_list = [
        ('Problem1', 'No_Output'),
        ('Problem2', 'Too_Long'),
        ('Problem3', 'No'),
        ('Problem4', 'No'),
        ('Problem5', 'No'),
        ('Problem6', 'Yes')
    ]

    # Start with an empty evidence dictionary
    evidence = {}

    # Iterate over each piece of evidence and update the dictionary
    for ev, state in evidence_list:
        evidence[ev] = state
        print(f"\nAdded Evidence: {ev}={state}")

        # After each new piece of evidence, report on all problems
        for problem in problems_to_report:
            print(f"\nReporting on {problem} with current evidence:")
            result_factor = bayesian_network.variable_elimination(query=[problem], evidence=evidence)
            for state, prob in result_factor.cpt.items():
                print(f"  State {state} has a probability of {prob:.4f}")

if __name__ == "__main__":

    alarm_test()
    child_test()      
    hailfinder_test()
    insurance_test()  
    win95pts_test()  

    # repeats = 10  # Number of repetitions for each test
    # results = []

    # # Measure each test function and add the result to the 'results' list
    # alarm_time = timeit.timeit('alarm_test()', globals=globals(), number=repeats) / repeats
    # results.append(f"alarm_test took an average of {alarm_time:.5f} seconds to run")

    # child_time = timeit.timeit('child_test()', globals=globals(), number=repeats) / repeats
    # results.append(f"child_test took an average of {child_time:.5f} seconds to run")

    # hailfinder_time = timeit.timeit('hailfinder_test()', globals=globals(), number=repeats) / repeats
    # results.append(f"hailfinder_test took an average of {hailfinder_time:.5f} seconds to run")

    # insurance_time = timeit.timeit('insurance_test()', globals=globals(), number=repeats) / repeats
    # results.append(f"insurance_test took an average of {insurance_time:.5f} seconds to run")

    # win95pts_time = timeit.timeit('win95pts_test()', globals=globals(), number=repeats) / repeats
    # results.append(f"win95pts_test took an average of {win95pts_time:.5f} seconds to run")

    # # Now print the accumulated results
    # print("\n".join(results))